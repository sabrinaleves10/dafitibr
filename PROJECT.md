# PROJECT: {{PROJECT_NAME}} — VTEX Commerce Platform Implementation

> **Version:** 1.0.0 | **Last updated:** {{DATE}}
> **Owner:** {{SA_NAME}} (VTEX Principal Solution Architect)
> **Status:** {{PROJECT_STATUS}}
> **Health:** {{HEALTH_STATUS}} — one-line summary of the latest Project Health Check (see
> `CHECKLIST.md`). Leave as "Not yet run" until the first check happens; update this line every
> time the check runs and finds something worth surfacing, not on every re-run.
> **Current Rocketlane Project:** {{ROCKETLANE_PROJECT_ID}} ([open in Rocketlane]({{ROCKETLANE_PROJECT_URL}}))

### Quick Facts

An AI session (or a human) should be able to read only this table and know who the client is,
where the engagement stands in Rocketlane, and its geographic/language footprint, without reading
the rest of this file. (How the "GitHub Repository" Rocketlane link works, and how to verify it, is
an operating rule — see `CLAUDE.md`'s Hard Rules and Setup Validation Checklist, not repeated here.)

| Field | Value |
|---|---|
| Client | {{CLIENT_NAME}} |
| System Integrator | {{SI_NAME}} |
| Google Drive project folder | {{GOOGLE_DRIVE_PROJECT_FOLDER_URL}} — client/SI-facing deliverables also get uploaded to its `Shared/` subfolder (see CLAUDE.md Hard Rule 14); confirm the link and its structure with the SA during initialize |
| Dashboard (GitHub Pages) | Not yet published — see `CLAUDE.md`'s "Dashboard Publishing (GitHub Pages)" |
| Claude Cowork project | Not yet created — no tool or connector can create it automatically; see `CLAUDE.md`'s "Claude Cowork Project Setup" for the SA's manual steps and the standard prompt |
| Countries | {{COUNTRIES_LIST}} |
| Multilanguage | {{MULTILANGUAGE_BOOL}} |
| Languages supported | {{LANGUAGES_LIST}} |
| Rocketlane Project Phases | {{ROCKETLANE_PHASES_LIST}} — pull from `get_phases`; write "Not yet defined" if the project doesn't use phases |

### Monitored Sources

Every recurring automation (`CLAUDE.md`'s Recurring Health Check Automation, Weekly Status Log
Check, and any catch-up scan) reads its sources from this table — not from memory, keyword
search, or a guess at what "probably" belongs to this project. **The SA provides these values at
initial setup** (see `CLAUDE.md`'s Initialize mode and Setup Validation Checklist); a row marked
`⏳` was inferred (from a connector listing or this repo's history) and still needs the SA's
confirmation. When a source changes (new channel, new recurring meeting, folder moved), update the
row here — surgically, per Hard Rule 6 — so the next automated run picks it up.

| Source | Identifier(s) | How automations use it | Status |
|---|---|---|---|
| GitHub repo | {{GITHUB_REPO_SLUG}} | Must match Rocketlane's "GitHub Repository" custom field (Hard Rule 5) | ⏳ Ask SA |
| Rocketlane project | {{ROCKETLANE_PROJECT_ID}} — see header above | Health Check pulls phases, hours, dates, tasks | ⏳ Ask SA |
| Rocketlane Status Log | {{ROCKETLANE_STATUS_LOG_CONNECTOR_AND_FIELDS}} | Weekly Status Log Check + event-triggered refresh | ⏳ Ask SA |
| Google Drive folder | {{GOOGLE_DRIVE_PROJECT_FOLDER_URL}} — see Quick Facts | Catch-up scan for new documents; upload destination (Hard Rule 14) | ⏳ Ask SA |
| Slack channels / DMs | {{SLACK_CHANNELS_WITH_IDS}} | Read each channel directly by ID (`slack_read_channel`, `oldest` = last run) — never keyword search as the primary method; re-check known open threads separately, since a channel read misses new replies to older threads | ⏳ Ask SA |
| Slack long-running threads | {{SLACK_LONG_RUNNING_THREADS}} — channel ID + thread `ts`, with a one-line topic each | Re-read each thread with `slack_read_thread` every run, `oldest` = last run, until it closes; the Slack mention sweep (`CLAUDE.md` Recurring Health Check step 2) adds threads here; drop a row only once the thread is resolved and any resulting task is tracked | ⏳ Ask SA |
| Granola folder | {{GRANOLA_FOLDER_NAME_AND_ID}} | `list_meetings` with this `folder_id`; pull the verbatim transcript before any register/milestone/ADR edit | ⏳ Ask SA |
| Read AI | {{READ_AI_USAGE}} | Catch-up scan for meetings not recorded in Granola | ⏳ Ask SA |
| Recurring meetings | {{RECURRING_MEETINGS}} | Expected meeting cadence — a missing weekly note is itself worth flagging | ⏳ Ask SA |
| Gmail | {{CLIENT_AND_SI_EMAIL_DOMAINS_AND_LABELS}} | Catch-up scan filter — threads to/from these domains, plus Rocketlane overdue/assignment alerts | ⏳ Ask SA |
| Zendesk (VTEX Support) | {{ZENDESK_TICKET_TRACKING}} | Check status of known tickets each run | ⏳ Ask SA |
| VTEX accounts | {{VTEX_ACCOUNTS_CLIENT_AND_NON_CLIENT}} — list the client's production/QA/stage/dev accounts and, separately, any sandbox/partner accounts that are *not* the client's | Account-inspection tools; never generalize a sandbox finding to the client's accounts | ⏳ Ask SA |

### Rocketlane Projects

One repo can outlive a single contract — a renewal, a phase 2, or a separate concurrent contract
for the same client all point back here rather than getting a new repo. This table is the full
history; "Current" marks which project's tasks and status drive this file and `JOURNAL.md` right
now.

| Project ID | Label | Status | Linked since |
|------------|-------|--------|--------------|
| {{ROCKETLANE_PROJECT_ID}} | {{ROCKETLANE_PROJECT_LABEL}} | Current | {{DATE}} |

### Contract Terms (binding — see `Contract/Signed Agreement/`)

> These are the legally contracted terms, not a live sync of Rocketlane or a restatement of
> `Sales Phase/`. They change only when a new signed entry lands in `Contract/Amendments/` — never
> by editing this table to match what Rocketlane shows or what delivery actually needs. If a
> decision made during delivery (an ADR, a risk in `CHECKLIST.md`, a scope discussion) would
> require going beyond what's listed here, that's a signal to raise a Contract Amendment with the
> SA, not to quietly proceed or to "fix" this table.

| Term | Value | Source |
|------|-------|--------|
| Contracted hours/budget | {{CONTRACTED_HOURS}} | `Contract/Signed Agreement/` |
| Contract term | {{CONTRACT_START_DATE}} – {{CONTRACT_END_DATE}} | `Contract/Signed Agreement/` |
| Contracted scope | See "Brands in scope" below | `Contract/Signed Agreement/` |
{{CONTRACT_TERMS_ADDITIONAL_ROWS}}

---

## 1. Project Overview

{{PROJECT_OVERVIEW}}

---

## 2. Client

| Field | Detail |
|-------|--------|
| **Company** | {{CLIENT_COMPANY_FULL}} |
| **HQ** | {{CLIENT_HQ_COUNTRY}} |
| **Website** | {{CLIENT_WEBSITE}} |
| **Sectors** | {{CLIENT_SECTORS}} |
| **Key contact** | {{CLIENT_KEY_CONTACTS}} — see Client Stakeholders below |

### Client Stakeholders ({{CLIENT_NAME}})

Who's who on the client side — read before drafting any client-facing communication (see
`CLIENT-COMMUNICATION-PLAYBOOK.md`). One row per person; add rows as new stakeholders appear.

| Name | Role |
|---|---|
| {{CLIENT_STAKEHOLDER_NAME}} | {{CLIENT_STAKEHOLDER_ROLE}} |

### Brands in scope

> Reflects `Contract/Signed Agreement/` — the binding scope. `Sales Phase/` may show an earlier,
> different proposed footprint (normal — scope often narrows or shifts before signature); a
> mismatch between this table and Rocketlane phase names or revenue data is worth investigating,
> not assuming away.

| Brand | Countries | Business Model | Notes |
|-------|-----------|----------------|-------|
{{BRANDS_TABLE_ROWS}}

> **Brands/countries explicitly excluded from this contract:** {{OUT_OF_SCOPE}}

---

## 3. VTEX Team

| Role | Name |
|------|------|
| Principal Solution Architect | {{SA_NAME}} ({{SA_EMAIL}}) |
{{VTEX_TEAM_ROWS}}

---

## 4. System Integrator — {{SI_NAME}}

{{SI_DESCRIPTION}}

**{{SI_NAME}} team composition:**
{{SI_TEAM_COMPOSITION}}

**Key {{SI_NAME}} deliverables:**
{{SI_DELIVERABLES}}

---

## 5. Architecture Summary

> This section (plus `Internal Documents/Architecture/ADRs/`) is the **current, living**
> architecture — kept up to date as decisions get made during delivery. `Sales Phase/VTEX
> Proposal/` and `Sales Phase/Agency Proposal/` are a frozen snapshot of what was originally
> proposed, not what's currently true. If they disagree, this section wins — update it (and add an
> ADR) whenever a real decision changes something from what was sold; don't edit the Sales Phase
> originals to match. That freedom has one limit: a decision here still has to fit inside the
> **Contract Terms** above. An architecture decision that would require more hours, a brand/country
> outside contracted scope, or a deliverable never promised isn't just an ADR — flag it as a
> Contract Amendment candidate.

### Platform
- **Commerce:** VTEX
- **Frontend:** {{FRONTEND_TECH}}
- **CMS:** {{CMS_TECH}}
- **Search:** {{SEARCH_TECH}}
- **Personalization:** {{PERSONALIZATION_TECH}}
- **Identity / SSO:** {{SSO_TECH}}
- **ERP integrations:** {{ERP_SYSTEMS}}
- **Integration Layer:** {{MIDDLEWARE_TECH}}
{{ADDITIONAL_PLATFORM_ITEMS}}

### Account Structure
{{ACCOUNT_STRUCTURE_DESCRIPTION}}

### Key Architecture Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
{{ARCH_DECISIONS_ROWS}}

### Notable Capabilities (outside base license — confirm with VTEX)
{{OUT_OF_LICENSE_ITEMS}}

---

## 6. Key Integrations

| System | Direction | Owner | Notes |
|--------|-----------|-------|-------|
{{INTEGRATIONS_TABLE_ROWS}}

---

## 7. Project Phases & Rollout

{{PHASES_DESCRIPTION}}

### Overall Timeline (indicative)

| Period | Milestone |
|--------|-----------|
{{TIMELINE_ROWS}}

---

## 8. Project Approach

{{PROJECT_APPROACH_DESCRIPTION}}

---

## 9. Delivery Model

| Component | Responsible |
|-----------|-------------|
| VTEX platform configuration | {{SI_NAME}} |
| Headless frontend | {{SI_NAME}} |
| CMS setup | {{SI_NAME}} |
| Integration Layer / Middleware | {{SI_NAME}} |
| Backend system integrations (ERP, etc.) | {{CLIENT_SHORT_NAME}} IT |
| Platform license & infrastructure | VTEX |
| Architecture oversight | VTEX SA ({{SA_NAME}}) |
{{DELIVERY_MODEL_ADDITIONAL_ROWS}}

---

## 10. Key Requirements (from RFP / Discovery)

{{KEY_REQUIREMENTS_LIST}}

---

## 11. Open Topics & Risks

{{OPEN_TOPICS_LIST}}

> See `CHECKLIST.md` for full tracking of open items, risks, and document status.

---

## 12. Reference Documents

| Document | Location |
|----------|----------|
{{REFERENCE_DOCS_ROWS}}
