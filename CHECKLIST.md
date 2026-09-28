# {{PROJECT_NAME}} — Project Checklist & Status

> **Version:** 1.0.0 | **Last updated:** {{DATE}}
> **Owner:** {{SA_NAME}} (VTEX Principal Solution Architect)

Legend: ✅ Done · 🔄 In Progress · ⏳ Pending · ❌ Blocked · 🗂️ Stored

---

## How to use this file

- **Inputs** = documents received from the client or partners that need to be stored/processed.
- **Outputs** = documents we need to create or deliver.
- **Architecture Cases** = specific topics/scenarios requiring analysis, an ADR, or a behavior note.
- Update status and add the file path when a document is stored or created.
- AI agents: always update this file after filing or creating any project document.

---

## A. Project Inputs

These are documents that have been provided by the client, agency, or VTEX — they need to be stored and, where noted, processed to extract key information.

| # | Item | Action | Status | File Path | Notes |
|---|------|--------|--------|-----------|-------|
| A01 | Proposed Architecture by SA — Diagram | Store + extract to PROJECT.md | ⏳ Pending | — | VAMS version: TBD |
| A02 | Proposed Architecture by SA — VAMS | Store | ⏳ Pending | — | Not yet received |
| A03 | Solution Design document | Store + extract risks & open topics | ⏳ Pending | — | |
| A04 | RFC document | Store | ⏳ Pending | — | Not yet received |
| A05 | Agency Proposal — Solution Execution Approach | Store | ⏳ Pending | — | |
| A06 | Agency Proposal — Project approach, rollout, RACI | Store | ⏳ Pending | — | |
| A07 | Proposed Timeline | Store | ⏳ Pending | — | |
| A08 | RACI Matrix | Store | ⏳ Pending | — | |
| A09 | Team Roster | Store | ⏳ Pending | — | |
| A10 | Rollout Strategy | Store | ⏳ Pending | — | |
| A11 | RFP (original) | Store | ⏳ Pending | — | |
| A12 | Technical & Functional Requirements | Store | ⏳ Pending | — | |
| A13 | List of Deliverables | Store | ⏳ Pending | — | |
| A14 | Financial Offer(s) | Store | ⏳ Pending | `Sales Phase/Financial Offers/` | Pre-signature original — never `Internal Documents/Commercial/` |
| A15 | Contractual Documents (Order Form, DPA, etc.) | Store | ⏳ Pending | `Contract/Signed Agreement/` | Separate from `Sales Phase/` — a contract has its own lifecycle and can be amended later (see A16) |
| A16 | Contract Amendment(s) / Extension(s) | Store | ⏳ Pending | `Contract/Amendments/` | Only if/when a scope change, extension, or new SOW gets negotiated — add one row per amendment when it happens, re-priced offer and signed version together |
{{ADDITIONAL_INPUT_ROWS}}

> **Filing note:** Sales-phase documents (RFP, both vendors' proposal responses, RFP Q&A/revenue
> data) go under `Sales Phase/`, not `Documents Shared by Customer/` — see `STRUCTURE.md`. Reference
> the actual stored path here once each is filed, and mark 🗂️ Stored, not just ⏳ Pending, once done.

---

## B. Project Outputs (Documents to Create)

These are documents that need to be produced by the VTEX team.

| # | Item | Action | Status | File Path | Notes |
|---|------|--------|--------|-----------|-------|
| B01 | Project Definition (`PROJECT.md`) | Create | ✅ Done | `PROJECT.md` | v1.0.0 — {{DATE}} |
| B02 | Folder Structure (`STRUCTURE.md`) | Create | ✅ Done | `STRUCTURE.md` | v1.0.0 — {{DATE}} |
| B03 | Project Checklist (`CHECKLIST.md`) | Create | ✅ Done | `CHECKLIST.md` | This file |
| B04 | Architecture Cases Index | Create | ⏳ Pending | `Internal Documents/Architecture/Topic Analysis/INDEX.md` | See Section C below |
| B05 | ADR Index | Create | ⏳ Pending | `Internal Documents/Architecture/ADRs/INDEX.md` | To be started once topics are confirmed |
| B06 | Integration Specifications (per system) | Create | ⏳ Pending | `Internal Documents/Solution Design/Integration Specs/` | Discovery phase |
| B07 | Functional Specifications (per brand/capability) | Create | ⏳ Pending | `Functional Specifications/` | Analysis & Design phase |
| B08 | Rollout Plan (detailed, post-kick-off) | Create | ⏳ Pending | `Internal Documents/Project Management/Timeline/` | Post kick-off |
| B09 | Consolidated Team Roster | Create | ⏳ Pending | `Internal Documents/Project Management/Team Roster/` | VTEX + SI + Client contacts |
| B10 | Meeting Log (`meetings/` populated) | Create | ⏳ Pending | `meetings/` | First entry at kick-off. Indexed in Section G below as files land — that section is the actual log, this row just tracks "has it started." |
| B11 | Client Communication Playbook | Create | ✅ Done | `Internal Documents/Project Management/Governance/CLIENT-COMMUNICATION-PLAYBOOK.md` | Ships filled in by default. Fill its "Engagement-Specific Notes" section as this client's comms preferences become known |
| B12 | Other governance docs (if any) | Create | ⏳ Pending | `Internal Documents/Project Management/Governance/` | Only if this engagement produces one (e.g. an escalation policy) — leave Pending if none exists |
{{ADDITIONAL_OUTPUT_ROWS}}

---

## C. Architecture Cases / Topic Analysis

Each row is a specific technical topic requiring analysis, an ADR, and/or a behavior note.
Create one `TOPIC-NNN-<slug>.md` file per item in `Internal Documents/Architecture/Topic Analysis/`.

| # | Topic | Priority | Status | ADR? | File | Notes |
|---|-------|----------|--------|------|------|-------|
{{ARCHITECTURE_TOPICS_ROWS}}

---

## D. Open Risks & Issues

| # | Risk / Issue | Severity | Owner | Status | Resolution / How it's handled | Notes |
|---|-------------|----------|-------|--------|-------------------------------|-------|
| R01 | Integration delivery by client IT is on critical path | 🔴 High | {{CLIENT_SHORT_NAME}} IT | ⏳ Open | — | Joint integration release planning required at kick-off |
{{ADDITIONAL_RISK_ROWS}}

> **Status values:** `⏳ Open` (needs a decision/owner), `✅ Accepted` (an inherent platform
> constraint, not a pending decision), or `✅ Closed` (once resolved — add a resolution note, don't
> delete the row). Every Accepted/Closed row fills the **Resolution / How it's handled** column: one
> or two plain sentences on how the risk was resolved, or how it will be handled so it doesn't
> materialize. Open rows leave it as `—`. The dashboard's Closed Risks tab reads this column.

> **Removed rows:** a row dismissed as never having been a real risk is removed from this table
> entirely rather than kept as "Closed" — the gap in the `R`-number sequence is expected and not a
> data-loss signal; see `JOURNAL.md` for what was removed and why.

> **Numbering:** keep risk IDs sequential and never reuse a resolved one's number. Risks surfaced
> by the Project Health Check below typically start around R17+ in projects that also track
> architecture-specific risks R01-R16-ish — there's no fixed range, just don't collide.

---

## E. Milestones

| # | Milestone | Target | Status |
|---|-----------|--------|--------|
| M01 | Contract signed / project awarded | {{CONTRACT_DATE}} | {{CONTRACT_STATUS}} |
| M02 | Commercial and contractual docs finalized | TBD | ⏳ Pending |
| M03 | Project kick-off | TBD | ⏳ Pending |
{{MILESTONE_ROWS}}

---

## F. Meeting Decision Capture Log

Populated by `vtex-meeting-decision-capture` (in the `solution-architecture` plugin) after
processing a meeting transcript. The `Reviewed?` column applies only to rows that produced an ADR or
Behavior Note draft: the SA promotes or discards each draft, then updates its row. Meeting notes
themselves are reference material and never need SA review (`CLAUDE.md` Hard Rule 12), so a
notes-only row gets `— n/a (notes only)`. Nothing in `Internal Documents/Architecture/Drafts/` is final
until this log says so.

| # | Meeting Date | Source | ADR Drafts | Behavior Note Drafts | Action Items Routed | Reviewed? |
|---|-------------|--------|------------|----------------------|----------------------|-----------|
{{MEETING_CAPTURE_ROWS}}

---

## G. Meeting Notes, Decks & Recordings Filed

Index of everything actually filed under root-level `meetings/` — separate from Section F, which
tracks the AI-drafted decision-capture log, not the raw files themselves. Add a row whenever a
meeting note, deck, or recording is filed; skip routine internal syncs that produced nothing
worth indexing.

| # | Date | Topic | File | Notes |
|---|------|-------|------|-------|
{{MEETING_FILES_ROWS}}

---

## H. Customer Needs / Feature Requests Filed

Index of everything filed under `Customer Needs/` (gap analysis, feature requests) — see
`STRUCTURE.md` for what belongs here. When filing a new item, check whether it's already covered
by VTEX's product roadmap (e.g. via the `product-ai-hub-mcp` connector, if available this session)
before treating it as a net-new ask — a need that's already planned changes the conversation with
the client from "we'll request this" to "this is coming." Never fabricate a roadmap date if the
tool isn't accessible; record it as not-yet-checked instead.

| # | Item | File | Status | Roadmap Status | Notes |
|---|------|------|--------|-----------------|-------|
{{CUSTOMER_NEEDS_ROWS}}

---

## I. Roadmap Watch

Upcoming VTEX platform capabilities relevant to this account — not tied to a specific filed
Customer Need, but worth tracking for current-phase decisions (e.g. "don't build a workaround for
X, it ships next quarter") or future-phase planning (e.g. renewal/expansion conversations). Add a
row when the SA or VTEX Product flags something relevant; check via `product-ai-hub-mcp` (if
available) rather than guessing at timelines. Prune rows once a capability ships and either gets
adopted or is confirmed not relevant — this is a watch list, not a permanent record.

| # | Capability / Theme | Relevance to {{CLIENT_SHORT_NAME}} | Expected Timing | Status | Notes |
|---|---------------------|--------------------------------------|------------------|--------|-------|
{{ROADMAP_WATCH_ROWS}}

---

## Project Health Check

**Any AI agent working on this project should run this proactively — at the start of a session, or
whenever asked for a status update — not only when explicitly asked to "check risks."** The whole
point is catching schedule/budget drift automatically instead of waiting for it to surface as a
missed date. Pull `get_projects` (Rocketlane) for the project(s) linked in `PROJECT.md`'s header
with `includeAllFields: true`, and compare:

| Signal | How to compute | What it catches |
|--------|-----------------|-------------------|
| Go-live date consistency | Compare the "Project Expected Go Live" custom field against Rocketlane's native `dueDate` on the same project | Two systems of record disagreeing about when the project actually finishes |
| Budget vs. progress ratio | `percentageBudgetedHoursConsumed` vs. `progressPercentage` — **and** Rocketlane's budgeted-hours figure vs. `PROJECT.md`'s Contract Terms block (the actual contracted hours) | Hours burning faster than deliverables complete; separately, Rocketlane's own budget figure silently drifting from what was actually signed — this has already happened in practice on a live engagement |
| Profit margin trend | `financials.metrics.actualProfitMargin` vs. `estimatedProfitMargin` | Commercial health of the engagement, not just delivery health |
| Task-level overdue count | `get_tasks` filtered by `taskStatus.ne` (not Completed) and `dueDate.lt` (today) | **Check reliability before trusting this per project** — some Rocketlane project templates don't populate individual task due dates, in which case the filter can't distinguish "overdue" from "no date set." Sample a few tasks with `includeAllFields` first; don't report an overdue count as fact if the underlying tasks don't actually carry due dates. |
| Status Log staleness | Compare today's date against **Status Log last actually updated** below (and `rocketlane_list_status_updates`' most recent `publishedAt`) | The internal/SA status narrative (the project's Rocketlane Status Log — see `CLAUDE.md`'s "Weekly Status Log Check") going stale even though the signals above keep moving — see "Status Log update triggers" below |

Task-by-task reconciliation (mirroring individual Rocketlane tasks against a ledger, proposing
creations for new action items) is a separate, complementary process — see
`Internal Documents/Project Management/Governance/ACTION-TRACKER.md` and
`ROCKETLANE-RECONCILIATION-RULES.md` in that same folder. This table is about the project's overall
health signals, not individual task drift.

When something is newly found (a date mismatch, a budget/progress gap, a margin drop, genuine
overdue tasks), record it in this section's own "Last run" findings below and update
`PROJECT.md`'s header Health line. **Don't file margin or task-punctuality findings as new
Section D risk rows** — this section is already the tracker for those signals, and a duplicate
"risk" drifts out of sync with the live numbers here and inflates the risk count. Section D is
for delivery risks (architecture, scope, external dependencies); a genuinely new *delivery* risk
a health check surfaces (e.g. a go-live date mismatch that threatens the timeline) still belongs
there. If nothing material changed since the last run, don't touch any file — just note it
internally and move on. Don't pad `JOURNAL.md` with "still fine" re-runs.

**ADR / Behavior Note candidates:** every run also checks what it found for new ADR or Behavior
Note candidates. It dedups them against Section F and the `ADRs/`/`Behavior Notes/` folders,
writes any real candidate as a `DRAFT-*` file in `Drafts/` within the run's PR, and records an
"ADR / BN candidates" line in the "Last run" findings below, even when the answer is "none found."
See `CLAUDE.md`'s "Recurring Health Check Automation", step 2, for the bar each type has to clear.

**Register consolidation:** every run also compares the repo's registers against each other and
against what they point to. That covers Topics (Section C), ADRs and Behavior Notes (Section F and
their folders), Section D risks, Section E milestones, Section H/I rows, and `ACTION-TRACKER.md`
Sections A–C. For each record still open, the run asks whether it's a duplicate, whether a later
record resolved it, whether it's parked without being closed, whether its row disagrees with its
document or its Rocketlane task, and whether it's missing from its register. It proposes each fix
in its PR and records a "Register consolidation" line in the "Last run" findings below, even when
the answer is "none". See `CLAUDE.md`'s "Recurring Health Check Automation", step 2.

**Status Log update triggers (Rocketlane Status Log, native status-update entry via the dedicated
Status Log connector — see `CLAUDE.md`'s "Weekly Status Log Check"):** two independent tracks, each
with its own routine. Never publish the note without the SA's go-ahead either way.

- **Cadence-based, weekly (the norm)** — the "Weekly Status Log Check" routine (default: every
  Monday). Due when **either**:
  - **"Status Log last actually updated" below still reads "Never yet."** A Status Log that's never
    been written is immediately due on the first run that reaches this check.
  - Otherwise, it's been **7 or more days** since that date.
- **Event-triggered (the exception)** — checked by every Health Check run, but **only** for:
  - A **significant change in client mood** — a real shift up or down (an escalation, open
    frustration, or clear praise from the client), not a single neutral message.
  - A **significant delivery delay** — a go-live or key-milestone slip, or a blocker that clearly
    puts a delivery date at risk.
  - A **major blocker or unblocker** — something that stops or restarts a critical workstream.

  Not a trigger by itself: a risk updated, escalated, or closed without changing the delivery
  outlook; an ADR promoted; a small `progressPercentage` change; a routine Slack/email exchange.
  Those go into the next weekly draft. When in doubt, don't draft — wait for the weekly run.

Draft the suggested note **in full**, in the format specified by
`Internal Documents/Project Management/Governance/STATUS-LOG-RULES.md` (header, Client Mood,
Project Status, Key Points & Decisions, Risks, Next Steps) — don't just say "an update is due" — so
the SA can approve or edit it in place. Record whichever of the two lines below changed after each
run. A suggestion the SA hasn't acted on yet still counts as "suggested," not "updated."

- **Status Log last suggested:** Never yet.
- **Status Log last actually updated:** Never yet.

**Last run:** Never yet — run this at kickoff, and set up the recurring version described in
`CLAUDE.md`'s "Recurring Health Check Automation" section as part of initializing this project.
