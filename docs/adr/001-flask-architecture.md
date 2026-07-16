# ADR 001: Flask Application Structure

## Status

Accepted

## Context

MovePal requires a backend structure that is easy for beginner developers
to understand, test, and extend during MVP development.

The project needs a structure that separates web request handling from
application logic while avoiding unnecessary architectural complexity at
an early stage.

The selected approach should support:

- simple local development;
- deterministic automated testing;
- future MVP features;
- clear ownership of responsibilities;
- easy onboarding for new contributors.

## Decision

MovePal will use:

- Flask application factory pattern;
- Blueprint-based route organization;
- Service modules for application logic;
- Flask test client for automated verification.

The current implementation follows a small modular monolith approach.

The application is created through `create_app()` instead of creating
a global Flask instance. Routes are grouped using blueprints, while
reusable business logic is placed inside service modules.

## Architecture Overview

Browser / Client
        |
        v
Flask Blueprint Routes
        |
        v
Service Modules
        |
        v
Response (HTML / JSON)

Routes are responsible for communication with clients, while services
handle reusable application behavior.

## Module Responsibilities

| Module | Responsibility |
|---|---|
| `app/__init__.py` | Creates the Flask application using the factory pattern and registers routes |
| `app/config.py` | Provides application configuration and portable project paths |
| `app/routes/pages.py` | Handles HTML page rendering and browser-facing routes |
| `app/routes/api.py` | Handles JSON endpoints, request validation, and HTTP responses |
| `app/services/` | Contains reusable application logic separated from HTTP concerns |
| `app/templates/` | Provides HTML presentation templates |
| `app/static/` | Provides browser assets such as CSS and JavaScript |
| `tests/` | Verifies application behavior using Flask test client and unit tests |

## Rationale

This structure keeps HTTP handling separate from application logic.

Routes should remain thin and focus on:

- receiving requests;
- validating input;
- calling services;
- returning responses.

Services should contain reusable logic that can be tested independently
and reused by future features.

The application factory pattern improves testability by allowing the
application to be created with different configurations.

Blueprints provide enough organization for the current MVP while
remaining simple for contributors who are learning Flask.

## Blueprint Structure Decision

The current blueprint structure uses:

- `pages` blueprint for HTML browser views;
- `api` blueprint for JSON endpoints.

This separation is intentionally small because the current MVP has
limited feature boundaries.

Additional blueprints will be introduced only when clear ownership
boundaries appear, such as:

- authentication;
- movement sessions;
- scoring;
- administration features.

Keeping fewer blueprints at this stage reduces navigation overhead
and avoids splitting related functionality prematurely.

## Extension Points

The selected structure allows future MVP tasks to extend the system
without changing the existing foundation.

Future extensions can include:

- adding new API endpoints inside dedicated blueprints;
- adding new service modules for pose processing, movement evaluation,
  feedback, and scoring;
- introducing additional configuration classes;
- expanding integration tests while keeping the same test-client approach;
- replacing service implementations with adapters when external providers
  are introduced.

## Testing Decision

Flask test client is used to verify application behavior without requiring
a running development server.

Current integration tests verify:

- HTML page response from `/`;
- JSON response from `/api/health`.

This allows CI environments to validate application behavior without camera
hardware or external dependencies.

## Rejected Alternatives

### Full enterprise layered architecture

A larger architecture containing additional layers such as:

- controllers;
- repositories;
- interfaces;
- dependency injection containers;
- additional abstractions;

was rejected.

This approach would increase:

- implementation time;
- onboarding difficulty;
- maintenance overhead;
- amount of code required for simple features.

The current MVP scope does not require this level of abstraction.

### Extensive blueprint separation

Creating a separate blueprint for every possible feature was rejected.

Example:

routes/
    auth.py
    health.py
    movement.py
    scoring.py
    sessions.py

Introducing this structure too early would make the project harder to
navigate without providing significant benefits.

Blueprint boundaries will be introduced when features become large enough
to justify independent ownership.

## Consequences

Positive consequences:

- easier onboarding for beginner contributors;
- clear separation between HTTP and business logic;
- simpler automated testing;
- easier future extension of MVP features;
- portable project structure.

Negative consequences:

- some modules may grow larger before a new boundary is introduced;
- future scaling may require additional architectural decisions;
- the project may need refactoring if production requirements exceed the
  MVP scope.

These trade-offs are acceptable because the current priority is a working,
understandable, and testable MVP.