# ADR 001: Flask Application Structure

## Status
Accepted

## Context

MovePal requires a backend structure that is easy
for beginners to understand and extend.

## Decision

Use:

- Flask application factory
- Blueprint based routes
- Service modules for business logic
- Flask test client for verification

## Rationale

This structure keeps HTTP handling separate
from application logic while avoiding unnecessary
complexity.

It supports future MVP features and is easy
for new contributors to follow.

## Rejected Alternatives

A larger layered architecture and extensive
blueprint separation were rejected because
the MVP scope does not require this complexity yet.