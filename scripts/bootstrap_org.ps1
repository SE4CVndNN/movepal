[CmdletBinding()]
param(
    [switch]$Apply,
    [switch]$SkipBacklogImport,
    [switch]$UpdateExistingIssues,
    [switch]$InviteMissingMembers,
    [string]$RootPath = (Split-Path -Parent $PSScriptRoot)
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
$ApiVersion = "2022-11-28"
$Mode = if ($Apply) { "APPLY" } else { "DRY-RUN" }
$RootPath = (Resolve-Path $RootPath).Path
$ConfigPath = Join-Path $RootPath "config/bootstrap_config.json"
$MetadataPath = Join-Path $RootPath "config/project_metadata.json"
$BacklogPath = Join-Path $RootPath "backlog/product_backlog.json"

function Write-Step { param([string]$Message) Write-Host "`n==> $Message" -ForegroundColor Cyan }
function Write-Info { param([string]$Message) Write-Host "[INFO] $Message" }
function Write-Warn { param([string]$Message) Write-Host "[WARN] $Message" -ForegroundColor Yellow }

function Require-Command {
    param([string]$Name)
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command '$Name' was not found in PATH."
    }
}

function Invoke-Checked {
    param([string]$Command, [string[]]$Arguments, [switch]$AllowFailure)

    # Windows PowerShell 5.1 can convert stderr from native programs into a
    # NativeCommandError when the script-wide ErrorActionPreference is Stop.
    # Several idempotency checks intentionally expect non-zero exits, such as
    # a GitHub API 404 when a team or repository does not exist yet. Temporarily
    # use Continue so the native exit code can be handled below.
    $previousErrorActionPreference = $ErrorActionPreference
    try {
        $ErrorActionPreference = "Continue"
        $output = & $Command @Arguments 2>&1
        $exitCode = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }

    if ($exitCode -ne 0 -and -not $AllowFailure) {
        throw "Command failed: $Command $($Arguments -join ' ')`n$(($output | Out-String).Trim())"
    }
    return [PSCustomObject]@{ ExitCode = $exitCode; Output = ($output | Out-String).Trim() }
}

function Invoke-Mutation {
    param([string]$Description, [string]$Command, [string[]]$Arguments)
    if (-not $Apply) {
        Write-Host "[DRY-RUN] $Description"
        return
    }
    Write-Host "[APPLY] $Description"
    Invoke-Checked -Command $Command -Arguments $Arguments | Out-Null
}

function Get-PythonInvocation {
    if (Get-Command "py" -ErrorAction SilentlyContinue) {
        $version = Invoke-Checked -Command "py" -Arguments @("-3.11", "--version") -AllowFailure
        if ($version.ExitCode -eq 0) { return [PSCustomObject]@{ Command = "py"; Prefix = @("-3.11") } }
    }
    if (Get-Command "python" -ErrorAction SilentlyContinue) {
        $versionText = (Invoke-Checked -Command "python" -Arguments @("--version")).Output
        if ($versionText -match "Python 3\.11") { return [PSCustomObject]@{ Command = "python"; Prefix = @() } }
        throw "Python is present but Python 3.11 is required. Found: $versionText"
    }
    throw "Python 3.11 was not found."
}

function Invoke-PythonScript {
    param([PSCustomObject]$Python, [string]$ScriptPath, [string[]]$Arguments)
    $all = @($Python.Prefix) + @($ScriptPath) + $Arguments
    $result = Invoke-Checked -Command $Python.Command -Arguments $all
    if (-not [string]::IsNullOrWhiteSpace($result.Output)) { Write-Host $result.Output }
}

function Test-GhResource {
    param([string]$Endpoint)
    $result = Invoke-Checked -Command "gh" -Arguments @("api", $Endpoint, "-H", "X-GitHub-Api-Version: $ApiVersion", "--silent") -AllowFailure
    return $result.ExitCode -eq 0
}

function Ensure-Team {
    param([string]$Organization, [PSCustomObject]$Team)
    if (Test-GhResource "orgs/$Organization/teams/$($Team.name)") {
        Write-Info "Team '$($Team.name)' already exists."
        return
    }
    Invoke-Mutation -Description "Create team '$($Team.name)'." -Command "gh" -Arguments @(
        "api", "-X", "POST", "orgs/$Organization/teams",
        "-H", "X-GitHub-Api-Version: $ApiVersion",
        "-f", "name=$($Team.name)", "-f", "description=$($Team.description)", "-f", "privacy=closed"
    )
}

function Get-MembershipState {
    param([string]$Organization, [string]$Username)
    $result = Invoke-Checked -Command "gh" -Arguments @(
        "api", "orgs/$Organization/memberships/$Username",
        "-H", "X-GitHub-Api-Version: $ApiVersion", "--jq", ".state"
    ) -AllowFailure
    if ($result.ExitCode -eq 0) { return $result.Output.Trim() }

    $pending = Invoke-Checked -Command "gh" -Arguments @(
        "api", "orgs/$Organization/invitations?per_page=100",
        "-H", "X-GitHub-Api-Version: $ApiVersion", "--jq", ".[] | select(.login == `"$Username`") | .login"
    ) -AllowFailure
    if ($pending.ExitCode -eq 0 -and -not [string]::IsNullOrWhiteSpace($pending.Output)) { return "pending" }
    return "missing"
}

function Invite-MemberByUsername {
    param([string]$Organization, [string]$Username)
    $user = Invoke-Checked -Command "gh" -Arguments @(
        "api", "users/$Username", "-H", "X-GitHub-Api-Version: $ApiVersion", "--jq", ".id"
    ) -AllowFailure
    if ($user.ExitCode -ne 0 -or [string]::IsNullOrWhiteSpace($user.Output)) {
        Write-Warn "GitHub user '$Username' could not be resolved; invitation skipped."
        return
    }
    Invoke-Mutation -Description "Invite '$Username' to '$Organization'." -Command "gh" -Arguments @(
        "api", "-X", "POST", "orgs/$Organization/invitations",
        "-H", "X-GitHub-Api-Version: $ApiVersion", "-F", "invitee_id=$($user.Output.Trim())", "-f", "role=direct_member"
    )
}

function Ensure-TeamMembers {
    param([string]$Organization, [PSCustomObject]$Team, [object[]]$Rows)
    foreach ($row in $Rows) {
        $username = $row.github_username.Trim()
        if (-not (Test-GhResource "users/$username")) {
            Write-Warn "GitHub account '$username' does not exist or is not visible; skipped."
            continue
        }
        $state = Get-MembershipState -Organization $Organization -Username $username
        if ($state -eq "missing" -and $InviteMissingMembers) {
            Invite-MemberByUsername -Organization $Organization -Username $username
            Write-Warn "'$username' was missing. An invitation was requested; team membership will be applied after acceptance on a later run."
            continue
        }
        if ($state -ne "active") {
            Write-Warn "'$username' organization membership is '$state'; team membership and issue assignment will be skipped until acceptance."
            continue
        }
        Invoke-Mutation -Description "Add '$username' to '$($Team.name)'." -Command "gh" -Arguments @(
            "api", "-X", "PUT", "orgs/$Organization/teams/$($Team.name)/memberships/$username",
            "-H", "X-GitHub-Api-Version: $ApiVersion", "-f", "role=member"
        )
    }
}

function Ensure-LocalRepository {
    param([string]$Path, [string]$Branch)
    if (-not (Test-Path (Join-Path $Path ".git"))) {
        Invoke-Mutation -Description "Initialize local Git repository on '$Branch'." -Command "git" -Arguments @("-C", $Path, "init", "-b", $Branch)
    } else {
        Write-Info "Local Git repository already exists."
    }
    if ($Apply) {
        $name = (Invoke-Checked -Command "git" -Arguments @("config", "--global", "user.name") -AllowFailure).Output
        $email = (Invoke-Checked -Command "git" -Arguments @("config", "--global", "user.email") -AllowFailure).Output
        if ([string]::IsNullOrWhiteSpace($name) -or [string]::IsNullOrWhiteSpace($email)) {
            throw "Configure git user.name and user.email before using -Apply."
        }
        Invoke-Checked -Command "git" -Arguments @("-C", $Path, "add", ".") | Out-Null
        $status = (Invoke-Checked -Command "git" -Arguments @("-C", $Path, "status", "--porcelain")).Output
        if (-not [string]::IsNullOrWhiteSpace($status)) {
            Invoke-Checked -Command "git" -Arguments @("-C", $Path, "commit", "-m", "chore: bootstrap MovePal repository and complete backlog") | Out-Null
        }
    } else {
        Write-Host "[DRY-RUN] Stage and commit all generated repository, automation, and backlog files."
    }
}

function Ensure-Repository {
    param([string]$Organization, [PSCustomObject]$Repository, [string]$Path)
    $fullName = "$Organization/$($Repository.name)"
    $exists = (Invoke-Checked -Command "gh" -Arguments @("repo", "view", $fullName, "--json", "name") -AllowFailure).ExitCode -eq 0
    Ensure-LocalRepository -Path $Path -Branch $Repository.default_branch
    if (-not $exists) {
        Invoke-Mutation -Description "Create private repository '$fullName' and push '$($Repository.default_branch)'." -Command "gh" -Arguments @(
            "repo", "create", $fullName, "--private", "--description", $Repository.description,
            "--source", $Path, "--remote", "origin", "--push", "--disable-wiki"
        )
    } else {
        Write-Info "Repository '$fullName' already exists."
        if ($Apply) {
            $remote = Invoke-Checked -Command "git" -Arguments @("-C", $Path, "remote", "get-url", "origin") -AllowFailure
            if ($remote.ExitCode -ne 0) {
                $ssh = (Invoke-Checked -Command "gh" -Arguments @("repo", "view", $fullName, "--json", "sshUrl", "--jq", ".sshUrl")).Output
                Invoke-Checked -Command "git" -Arguments @("-C", $Path, "remote", "add", "origin", $ssh) | Out-Null
            }
            $remoteBranch = Invoke-Checked -Command "git" -Arguments @("-C", $Path, "ls-remote", "--heads", "origin", $Repository.default_branch) -AllowFailure
            if ([string]::IsNullOrWhiteSpace($remoteBranch.Output)) {
                Invoke-Checked -Command "git" -Arguments @("-C", $Path, "push", "-u", "origin", $Repository.default_branch) | Out-Null
            } else {
                Write-Info "Remote '$($Repository.default_branch)' already exists. No automatic overwrite was attempted."
            }
        } else {
            Write-Host "[DRY-RUN] Ensure origin exists and push only if remote master is absent."
        }
    }
    Invoke-Mutation -Description "Configure repository merge and branch defaults." -Command "gh" -Arguments @(
        "repo", "edit", $fullName, "--default-branch", $Repository.default_branch,
        "--enable-issues=true", "--enable-projects=true", "--enable-wiki=false",
        "--delete-branch-on-merge=true", "--enable-squash-merge=true",
        "--enable-merge-commit=false", "--enable-rebase-merge=false"
    )
}

function Ensure-TeamPermission {
    param([string]$Organization, [string]$Repository, [PSCustomObject]$Team)
    Invoke-Mutation -Description "Grant '$($Team.name)' permission '$($Team.repository_permission)' on '$Organization/$Repository'." -Command "gh" -Arguments @(
        "api", "-X", "PUT", "orgs/$Organization/teams/$($Team.name)/repos/$Organization/$Repository",
        "-H", "X-GitHub-Api-Version: $ApiVersion", "-f", "permission=$($Team.repository_permission)"
    )
}

Write-Host "MovePal owner bootstrap - $Mode" -ForegroundColor Green
Write-Host "Root: $RootPath"
Require-Command "gh"
Require-Command "git"
$Python = Get-PythonInvocation
$config = Get-Content -Raw $ConfigPath | ConvertFrom-Json

Write-Step "Validate GitHub authentication and organization ownership"
Invoke-Checked -Command "gh" -Arguments @("auth", "status") | Out-Null
$currentUser = (Invoke-Checked -Command "gh" -Arguments @("api", "user", "--jq", ".login")).Output.Trim()
$orgRole = (Invoke-Checked -Command "gh" -Arguments @(
    "api", "orgs/$($config.organization)/memberships/$currentUser",
    "-H", "X-GitHub-Api-Version: $ApiVersion", "--jq", ".role"
)).Output.Trim()
if ($orgRole -ne "admin") { throw "Authenticated account '$currentUser' is not an owner/admin of '$($config.organization)'." }
Write-Info "Authenticated owner/admin: $currentUser"

Write-Step "Validate team files and complete backlog"
Invoke-PythonScript -Python $Python -ScriptPath (Join-Path $RootPath "scripts/validate_teams.py") -Arguments @(
    "--team-a", (Join-Path $RootPath "config/team_a.csv"), "--team-b", (Join-Path $RootPath "config/team_b.csv")
)
Invoke-PythonScript -Python $Python -ScriptPath (Join-Path $RootPath "scripts/validate_backlog.py") -Arguments @(
    "--backlog", $BacklogPath
)
Write-Info "Team and backlog validation passed."

Write-Step "Create or validate organization teams and membership"
foreach ($team in $config.teams) {
    Ensure-Team -Organization $config.organization -Team $team
    $csvPath = Join-Path $RootPath $team.source_file
    $members = Import-Csv $csvPath
    Ensure-TeamMembers -Organization $config.organization -Team $team -Rows $members
}

Write-Step "Create or validate the private repository"
Ensure-Repository -Organization $config.organization -Repository $config.repository -Path $RootPath
foreach ($team in $config.teams) {
    Ensure-TeamPermission -Organization $config.organization -Repository $config.repository.name -Team $team
}

Write-Step "Prepare labels, milestones, organization Project, custom fields, and repository link"
$prepareArgs = @(
    "--organization", $config.organization,
    "--repository", $config.repository.name,
    "--project-title", $config.project.title,
    "--metadata", $MetadataPath
)
if ($Apply) { $prepareArgs += "--apply" }
Invoke-PythonScript -Python $Python -ScriptPath (Join-Path $RootPath "scripts/prepare_repository.py") -Arguments $prepareArgs

if (-not $SkipBacklogImport) {
    Write-Step "Import the complete backlog and assign Sprint 1"
    $importArgs = @(
        "--organization", $config.organization,
        "--repository", $config.repository.name,
        "--project-title", $config.project.title,
        "--backlog", $BacklogPath,
        "--source", "all",
        "--report", (Join-Path $RootPath "bootstrap_reports/backlog_import_summary.json")
    )
    if ($Apply) { $importArgs += "--apply" }
    if ($UpdateExistingIssues) { $importArgs += "--update-existing" }
    Invoke-PythonScript -Python $Python -ScriptPath (Join-Path $RootPath "scripts/import_backlog.py") -Arguments $importArgs
} else {
    Write-Warn "Backlog import was skipped by request."
}

Write-Step "Bootstrap summary"
Write-Host "Mode: $Mode"
Write-Host "Repository: https://github.com/$($config.organization)/$($config.repository.name)"
Write-Host "Default branch: $($config.repository.default_branch)"
Write-Host "Project: $($config.project.title)"
Write-Host "Product backlog: 63 issues (all imported unless skipped)"
Write-Host "Sprint 1: 27 Team B development issues plus 6 Team A manual QA issues"
Write-Host "Final external QA date: 2026-07-29"
Write-Host "Post-sprint/future/optional issues: imported but unassigned"
Write-Host "No token or student email address was printed or committed by this script."
if ($Apply) {
    Write-Host "Apply completed. Follow docs/verification_checklist.md and create Project views manually." -ForegroundColor Green
} else {
    Write-Host "Dry-run completed. Review warnings, then rerun with -Apply." -ForegroundColor Green
}
