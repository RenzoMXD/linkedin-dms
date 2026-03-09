# Desearch — Social DMs Sync (X / Twitter first)

This repository is for building a **community-driven DM sync service**, starting with **X (Twitter) Direct Messages**.

The goal: given a user’s X account session (cookies) and a proxy, the service should be able to:

1. **Sync DM history** (fetch and store conversation history)
2. **Send DMs** to specific users

We’re intentionally keeping the first version minimal, so contributors can plug in better scraping, official APIs (if available), storage backends, and deployment options.

## What we want to build (overview)

### Core capabilities

#### 1) Sync DM history
- Accept an authenticated X session (typically **browser cookies**; optionally username/password if someone implements it safely)
- Use a **per-account proxy** (residential/mobile proxies are often required)
- Discover DM conversations
- Fetch message history per conversation
- Persist messages in a normalized format (DB)
- Incremental sync (only fetch new messages after last checkpoint)

#### 2) Send DMs
- Send a DM to a specific recipient
- Support idempotency / retries
- Record outbound message status

### Constraints / reality
- X is heavily protected by anti-bot systems.
- Cookie-based sessions can expire and may trigger security challenges.
- Proxies, rate limiting, and careful request patterns are mandatory.

This repo is **NOT** about bypassing security challenges or breaking laws/terms. It’s about building a robust, opt-in syncing tool for accounts you own or have explicit permission to access.

## Non-goals
- Account takeover or credential harvesting
- Circumventing CAPTCHAs / 2FA / device challenges
- Mass spam / unsolicited messaging

## Proposed architecture

### Components
- **Worker**: does the actual sync/send actions for one account
- **API service**: manages accounts, schedules syncs, exposes endpoints
- **Storage**: database for accounts, conversations, messages, sync cursors

### Data model (suggested)
- `Account`: handle, cookies blob reference, proxy config, last sync time
- `Conversation`: conversation id, participants
- `Message`: message id, conversation id, sender id, text, media refs, timestamp
- `SyncCursor`: per conversation cursor/watermark for incremental sync

### Interfaces
- **Provider abstraction** (recommended):
  - `providers/x/` implements X-specific logic
  - Later we can add `providers/linkedin/`, `providers/telegram/`, etc.

## MVP scope (what we want first)

1. A minimal Python service skeleton
2. A provider interface with placeholder X implementation
3. A simple storage layer (SQLite first)
4. CLI commands:
   - `sync` (fetch conversations + messages)
   - `send` (send DM)

Contributors can then replace the provider implementation with:
- browser automation (Playwright)
- network scraping (session cookies + HTTP)
- official APIs (if and when possible)

## Repo layout (planned)

```
.
├─ apps/
│  └─ api/                 # FastAPI service
├─ libs/
│  ├─ core/                # shared models, storage, config
│  └─ providers/
│     └─ x/                # X/Twitter provider (placeholder)
├─ scripts/
├─ tests/
└─ docs/
```

## Getting started (for contributors)

This repo will use Python 3.11+.

### Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run (planned)
```bash
python -m apps.api
```

## How to contribute

- Pick an issue and comment that you’re working on it.
- Keep PRs small and focused.
- Add tests where possible.

## Security & privacy

Cookies and session tokens are extremely sensitive.

**Do not** commit real cookies or credentials.

When implementing account auth handling:
- Encrypt cookies at rest
- Support secret managers via env vars
- Add redaction in logs

## Roadmap

- [ ] MVP skeleton: FastAPI + SQLite + provider interface
- [ ] X provider: conversation discovery + incremental sync (TBD)
- [ ] X provider: send DM (TBD)
- [ ] Proxy + per-account rate limiting
- [ ] Dockerfile + deployment guide

---

If you want to help, start with the issues in this repo.
