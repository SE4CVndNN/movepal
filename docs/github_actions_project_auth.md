# Optional authentication for Project workflows

## Initial bootstrap

No Actions secret is required. Run `scripts/bootstrap_org.ps1` locally under the authenticated organization-owner account. This creates the Project and imports all backlog issues.

## Later workflow reruns

The built-in repository `GITHUB_TOKEN` cannot access an organization Project. Therefore `prepare-project.yml` and `import-backlog.yml` expect a credential named `MOVEPAL_PROJECT_TOKEN`.

The preferred long-term design is a GitHub App installed on `SE4CVndNN` with the minimum required access:

- organization Projects: read and write
- repository Issues: read and write, because the importer creates/updates issues
- repository Metadata: read
- repository Contents: read if required to link/read the repository
- installation restricted to the MovePal repository where possible

A more secure GitHub App workflow would generate a short-lived installation token using an app client ID and private key. The included workflows accept one token secret to keep the student project simpler; do not place the broad owner OAuth token used by `gh auth` into this secret.

If you deliberately use a narrowly scoped token instead:

1. Create it specifically for this automation and minimize repository/organization access.
2. Open `SE4CVndNN/movepal -> Settings -> Secrets and variables -> Actions`.
3. Create repository secret `MOVEPAL_PROJECT_TOKEN`.
4. Paste the token once; never place it in a file or workflow.
5. Run both workflows first with `dry_run=true`.
6. Rotate/revoke the token after the course if it is no longer needed.

The local bootstrap remains the recommended route for the initial import.
