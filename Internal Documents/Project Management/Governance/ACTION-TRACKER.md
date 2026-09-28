# ACTION-TRACKER — {{PROJECT_NAME}}

> Single running tracker: VTEX SA action items, plus client/SI requests and commitments worth
> tracking. Add new items or update status on existing ones — **never create a duplicate/alternate
> tracker file.** Mirrored against Rocketlane on a recurring cadence — see
> `ROCKETLANE-RECONCILIATION-RULES.md` in this same folder for the full sync rules (join key,
> sync direction, default ownership, approval boundaries). Also surfaced on the local preview
> Dashboard's Tasks tab (`.preview/`) — see `README.md`.
>
> **Never delete a row, including a discarded creation candidate.** Add a status note instead — the
> history of "this was considered and rejected" is worth keeping even once the practical outcome
> (no live Rocketlane task) is settled.

---

## A. VTEX SA Action Items

| # | Action | Owner | Raised | Priority | Due Date | Status | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | {{EXAMPLE_ACTION_TEXT}} | {{SA_NAME}} | {{DATE}} | — | — | Open | {{SOURCE_MEETING_OR_THREAD}} |
{{ADDITIONAL_ACTION_A_ROWS}}

---

## B. Client / SI Requests & Commitments (tracked for follow-up, not owned by VTEX SA)

| # | Action | Owner | Raised | Priority | Due Date | Status | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
{{ADDITIONAL_ACTION_B_ROWS}}

> Only track a client/SI item here when it's a genuine blocker for VTEX's own work — see
> `ROCKETLANE-RECONCILIATION-RULES.md` §5. Don't track client/SI work purely for visibility into
> something VTEX doesn't own.

---

## C. New Task Candidates (pending SA review)

Whenever a newly-identified Rocketlane task-creation candidate turns up (catch-up scan or
full-ledger pass, per `ROCKETLANE-RECONCILIATION-RULES.md` §16 step 4), **write it directly into
this table immediately — no chat authorization needed for this write.** This table is the review
surface instead: it renders as its own "New Task Candidates" table on the site dashboard's Tasks
tab (`.preview/index.html#dashboard:tasks`), where the SA reviews pending rows and replies (in
chat, on the dashboard's linked PR, or whenever convenient) to approve or discard each one.

This does **not** relax `ROCKETLANE-RECONCILIATION-RULES.md` §13/§16 — creating the actual task in
Rocketlane still requires explicit SA approval before the API call. Only the *ledger write*
(proposing the candidate here) is pre-approved, the same way the §3/§7 mirror-back already is.

Once the SA acts on a row:
- **Approved and created in Rocketlane** → move it to Section A or B as a normal tracked row (with
  its new task ID/link), and mark this row's Status `✅ Approved — see §A.N` / `§B.N`.
- **Discarded** → keep the row, mark Status `❌ Discarded (<date>) — <reason>`. Never delete a row,
  same convention as Sections A/B.

| # | Candidate | Suggested taskName | Owner | Raised | Source | Status |
| --- | --- | --- | --- | --- | --- | --- |
{{ADDITIONAL_ACTION_C_ROWS}}
