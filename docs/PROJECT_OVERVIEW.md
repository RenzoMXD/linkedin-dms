# Project Overview — Social DMs Sync (X / Twitter)

## Summary
We’re building an **opt-in DM synchronization and sending service** for social platforms, starting with **X (Twitter)**.

This project is intended to be **open-source and community-built**:
- We will provide the skeleton: API, storage, job runner, abstractions
- Contributors can implement provider-specific logic (Playwright, HTTP scraping, official APIs where available)

## Problem
Teams running outreach/support communities often need:
- a searchable local archive of DMs
- message analytics and routing
- the ability to send DMs programmatically from authorized accounts

For X, this is difficult due to:
- session + anti-bot constraints
- rate limits
- frequent UI/API changes

## Core requirements

### A) Sync DM history
Given:
- authenticated session (cookies)
- optional per-account proxy

We need:
- conversation discovery
- message history retrieval
- incremental sync (only new messages)
- persistence in a database
- observability (logs, metrics)

### B) Send DMs
Given:
- authenticated session
- recipient identity

We need:
- message send
- retries with idempotency key
- record delivery status

## Principles
- **Consent & access control**: only accounts you own or have explicit permission to access
- **No bypassing challenges**: we don’t implement CAPTCHA/2FA circumvention
- **Secure by default**: redact secrets, encrypt cookies at rest

## MVP plan

### Phase 1 — Skeleton
- FastAPI service with basic endpoints
- SQLite storage schema
- provider abstraction + dummy provider
- CLI to run sync/send jobs

### Phase 2 — X provider implementation
- Decide approach (Playwright vs HTTP)
- Implement conversation/message fetch
- Implement sending
- Add rate limiting + proxy support

### Phase 3 — Hardening
- Postgres support
- background job queue (RQ/Celery/Arq)
- Docker + deploy docs

## Open questions
- Preferred provider approach?
- Target deployment environment?
- Required message types (text only vs media)?

See Issues for breakdown.
