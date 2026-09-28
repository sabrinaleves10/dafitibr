# Rocketlane Reconciliation Rules

> Ships with every client repo, filled in from day one — same standing-practice model as
> `CLIENT-COMMUNICATION-PLAYBOOK.md` in this folder. Only **Section 1 (Project Reference Data)**
> below should differ between clients — fill it in during Initialize mode, alongside the
> `{{PLACEHOLDER}}` pass on `PROJECT.md`/`CHECKLIST.md`. The rest is standing PS practice and
> should stay identical to the template unless the SA deliberately changes it here.

This document describes **logic and rules, not a specific implementation**. It governs how
`ACTION-TRACKER.md` (in this same folder) — the single running ledger of VTEX SA action items and
client/SI commitments — stays in sync with Rocketlane, and how new action items become Rocketlane
task proposals. It assumes read/write access to Rocketlane (via API or MCP) and a way to surface
proposals for human (SA) approval before writing to Rocketlane.

Not covered by this document: the daily Granola/Slack/Gmail capture rules (dedup, date-window/OOO
logic, filing destinations) or the ADR/Behavior Note/Customer Need document lifecycle — those are
covered by `CLAUDE.md`'s "Recurring Health Check Automation" section and the specialized skills in
[`vtexprojects/vtex-sa-toolkit`](https://github.com/vtexprojects/vtex-sa-toolkit).

---

## 1. Project reference data

Fill this in once, during Initialize mode, from `PROJECT.md`'s header and a `get_phases` /
`get_users` pull against the linked Rocketlane project. Keep it current if phases or the VTEX team
roster change.

- Rocketlane project: {{ROCKETLANE_PROJECT_LABEL}}, `projectId = {{ROCKETLANE_PROJECT_ID}}` (see
  `PROJECT.md`'s header — this should always match, never be re-typed independently).
- Phases: {{ROCKETLANE_PHASES_LIST}} (same list as `PROJECT.md`'s Quick Facts — pull from
  `get_phases`, keep both in sync if phases change).
- VTEX users eligible as task assignees: {{VTEX_TEAM_ROCKETLANE_USER_IDS}} (pull from `get_users`
  for anyone on the `PROJECT.md` §3 VTEX Team table who should ever hold a Rocketlane task).
- Task statuses: `1` To do · `2` In progress · `3` Completed · `4` Blocked · `5` On hold (Rocketlane
  platform defaults — confirm against `get_tasks` output if this project's instance differs).
- "Customer" placeholder assignee id, if one exists for this project: {{CUSTOMER_PLACEHOLDER_ASSIGNEE_ID}}.
  On at least one prior engagement this could not be set via the Rocketlane API/MCP (rejected
  whether passed as `placeholderId`, `userId`, or the customer-company system-bot id) — if the same
  holds here, note it and flag any task meant for that placeholder for the SA to add manually in
  the Rocketlane UI. Re-verify this per project rather than assuming the limitation carries over.
- {{CLIENT_SHORT_NAME}} and {{SI_SHORT_NAME}} people are not Rocketlane users on most engagements
  and generally can't be set as `assignees` — confirm for this project rather than assuming.

## 2. Join key

Every `ACTION-TRACKER.md` item has an `externalReferenceId` of the form:

```
{{PROJECT_CODE}}-<section>-<number>
```

Where `{{PROJECT_CODE}}` is a short, stable code for this engagement (e.g. client initials) picked
once during Initialize and never changed.

- Section `A` = VTEX SA's own actions.
- Section `B` = client/SI commitments.
- Examples: `{{PROJECT_CODE}}-A-14`, `{{PROJECT_CODE}}-B-11`.

This id is the join key between the ledger (`ACTION-TRACKER.md`) and the Rocketlane task. **Always
search Rocketlane by exact match on this field before doing anything else with an item.**

## 3. Sync direction — Rocketlane is authoritative once a task exists

- For any field Rocketlane actually tracks on an existing task — status, name, assignee (and,
  conceptually, priority, see §8) — **Rocketlane is the live source of truth.** The VTEX team edits
  tasks directly in Rocketlane day to day; it's not realistic to expect every change to land in the
  ledger first.
- So: if a task already exists in Rocketlane for a given `externalReferenceId`, the job's role is
  to **detect drift between Rocketlane and the ledger and update the ledger to mirror Rocketlane**
  — never to propose changing Rocketlane to match the ledger.
- The ledger stays authoritative only for items that have no Rocketlane task yet (candidates for
  creation, §6) and for narrative/history around each item.
- This mirror-back write (ledger ← Rocketlane) does **not** need human approval — it's an edit to
  this repo's own internal ledger, not a write to Rocketlane. Every other write below (create,
  update, close, reassign, date change) does.

## 4. Grouping / parent-child check — before proposing anything new

Before proposing a new standalone task:

1. Check whether the item should instead be a subtask of an existing Rocketlane task, or whether it
   and other pending items from the same run share a topic and should be grouped under one new
   parent task with subtasks — rather than one flat task per item.
2. Search existing Rocketlane tasks by topic/keyword for a plausible parent before proposing a
   standalone task. Also cross-check the other items about to be proposed in the same run for
   topical overlap with each other.
3. If a suitable existing parent is found, propose the new item as a subtask (`parent: {taskId}` at
   creation time).
4. If several related pending items share no existing parent, propose **one new parent task** with
   the individual items as subtasks, instead of several flat top-level tasks.

Why this matters: Rocketlane's `parent` field can only be set **at creation time** — it can't be
added or changed afterward — and there's no delete capability available via the API/MCP on most
accounts, so a flat task created by mistake can't later be converted into a subtask without the SA
deleting it manually in the UI. Re-verify delete availability for this project rather than assuming
it carries over from other engagements.

Also: a task whose only content is confirming attendance at a meeting is **not** a task — don't
propose creating one. Mention it in the summary only if it's worth noting at all.

**Naming rule:** whether standalone or a parent, never name a task with a single bare topic word
(e.g. "Pricing") — unusable for accurate timesheet logging. Use a scoped, specific name instead
(e.g. "Pricing rules — B2B price tables").

## 5. Ownership boundary — when to propose a `[{{SI_SHORT_NAME}}]`/`[{{CLIENT_SHORT_NAME}}]` task

Only propose a task tagged `[{{SI_SHORT_NAME}}]` or `[{{CLIENT_SHORT_NAME}}]` — i.e. tracking
something another team owns — when it is a genuine blocker: VTEX's own work cannot proceed without
their input, action, or configuration.

- Do not propose tracking a client/SI item purely for visibility into work VTEX doesn't own.
- The goal is a record that the team flagged a blocker and followed up on it — not accountability
  for another team's delivery.
- If it's unclear whether a client/SI item is a real blocker, say so explicitly in the proposal and
  let the SA decide, rather than defaulting to "create it."

## 6. Creating a new task (item has no Rocketlane task yet)

Propose, do not create directly. Shape:

- `taskName`: `[VTEX] <action>` / `[{{SI_SHORT_NAME}}] <action>` / `[{{CLIENT_SHORT_NAME}}] <action>`
  depending on the real owner.
  - `[{{SI_SHORT_NAME}}]`/`[{{CLIENT_SHORT_NAME}}]` tasks additionally get a `Check - ` prefix right
    after the tag — e.g. `[{{CLIENT_SHORT_NAME}}] Check - <action>` — the convention marking a task
    VTEX only monitors rather than executes. Apply to every new one of those tasks; skip for
    `[VTEX]` tasks and for tasks that are already Completed.
- `assignees`: the VTEX person chasing the item.
  - **Default assignee: the Project Lead SA** ({{SA_NAME}}, from `PROJECT.md`'s header) — unless
    the source item explicitly names someone else on the VTEX team as the one chasing it.
  - Never default to more than one assignee — use a single named owner. Other VTEX team members
    pick up specific items case-by-case (typically decided in a regular sync with the SA), not by
    default.
  - For `[{{SI_SHORT_NAME}}]`/`[{{CLIENT_SHORT_NAME}}]` tasks, `assignees` is still the VTEX person
    following up — there are usually no external Rocketlane users to assign (see §1).
  - If the real owner is the client or SI, note in `taskDescription` that the "Customer" placeholder
    (§1), if this project has one, should also be added manually in the Rocketlane UI — do not
    retry the API for this if it's already known to fail.
- `taskDescription` (HTML): an accountability block — "Accountable party" / "Owner" naming the real
  responsible person and company — plus the item text, the date it was raised, the source
  (file/thread/ticket), and a note that the ledger is authoritative for history and shouldn't be
  hand-edited to override Rocketlane.
- `phase`: whichever phase fits by date — check `PROJECT.md`'s header/`CHECKLIST.md` §E for the
  current phase; update §1 above once the project moves phases.
- `status`: `1` (To do), or `2` (In progress) if the source says work has started.
- `dueDate`: only if the source explicitly states a date. If not, leave empty and list the item
  separately as "no deadline" in the proposal — never invent one.

## 7. Existing task drifted from the ledger

If a task already exists but its live Rocketlane state (status/name/assignee) differs from the
ledger: update the ledger to match Rocketlane, stating which field changed and why (per the mirror
direction in §3). This is a ledger edit — no approval needed. Never propose changing Rocketlane to
match the ledger in this case.

## 8. Priority — known API limitation

On at least one prior engagement, Rocketlane's native `priority` field could not be written through
`update_task` (no such parameter in the schema). Verify this for the current project rather than
assuming it — if it holds, never attempt it and never propose it as a Rocketlane write.

If a priority recommendation is warranted (e.g. the item blocks other work): log it in the ledger's
own `Priority` column and/or as a `taskPrivateNote` on the Rocketlane task, and flag in the summary
that it still needs to be set manually in the Rocketlane UI if the write limitation applies.

Assigning `Priority` values in the ledger itself: default to a neutral placeholder (e.g.
`TBD`/`—`) unless there is real, explicit, sourced signal — an explicit Rocketlane priority already
set, blocking language in the source text, or a tie to a High-severity risk in `CHECKLIST.md`
Section D. Never infer High from generic urgency-sounding language without flagging that inference
as a judgment call in the summary.

## 9. Dependencies — check for known API quirks

Before relying on Rocketlane's `dependencies` field via `update_task`, do a small test — some
projects have seen this fail intermittently ("Not found" errors for tasks that clearly exist). If
it's unreliable on this project, don't keep retrying — record the intended dependency as a
`taskPrivateNote` on both tasks instead, and mention it in the summary.

## 10. Completing / closing a task

Only propose moving a task to Completed (status `3`) when both:

1. The ledger/source says the item was fulfilled, **and**
2. There is a valid completion/approval signal (see §11).

## 11. What counts as an approval or completion signal

Only these three count as approving an artifact or confirming a task is done:

1. **A reply by email** in the thread where the item/artifact was originally raised or sent.
2. **An explicit mention in a meeting note** that something was approved or completed.
3. **A manual action by the SA** — they closed/moved it themselves, or explicitly confirmed a prior
   proposal.

**Slack does NOT count.** It's read for capture, but a Slack message never approves anything and
never closes a Rocketlane task on its own. If something in Slack looks like an approval, note it as
evidence but still ask for confirmation.

Watch for false positives: "sounds good", "thanks", "noted", a 👍 — none of these are approvals.
Look for unambiguous approval language, or the person with actual authority over the decision
saying to go ahead. When in doubt, flag as "ambiguous signal" and let the SA decide.

## 12. Orphan Rocketlane tasks

If a Rocketlane task carrying a `[VTEX]`/`[{{SI_SHORT_NAME}}]`/`[{{CLIENT_SHORT_NAME}}]` prefix
exists with no counterpart in the ledger: report it as a desync for the SA to resolve. Do not touch
it automatically.

The reverse case — a ledger row citing a Rocketlane task ID that no longer exists live — is **not**
a desync to just report; it's ordinary drift, handled the same as any other §7 case (mirror the
deletion into the row, no approval needed). See §19 for the mandatory sweep that finds these.

## 13. Approval boundary — what may be written automatically vs. proposed

- **May write without asking:** the ledger mirror-back in §3/§7 (Rocketlane → ledger), and anything
  purely internal (drafts, an internal run log/checklist).
- **Must be proposed and require explicit SA approval before writing:** any Rocketlane `create`,
  `update` (status/name/assignee/dates), or close/reassign; anything that would count as an
  external send (email, Slack message, a client-facing submission).
- Approval happens in chat/PR/wherever the SA reviews the run's output — never assume a prior
  general design decision ("drafts can be auto") extends to live-system writes. When the boundary
  is unclear, propose rather than execute.

## 14. Anti-duplicate guard at execution time

When the SA approves a Rocketlane creation, **re-query that `externalReferenceId` immediately
before creating** — not just at proposal time. This matters especially if more than one
person/process can approve the same item. If the re-query returns a task, do not create a second
one — report that it already exists and move on. Never create two tasks for the same
`externalReferenceId`. If pre-existing duplicates are found, report them; do not delete them (no
delete capability on most accounts, and it's an SA call either way).

## 15. Suggested proposal format for the run's output

End every run with, at minimum:

- Window/scope reviewed and why.
- Done automatically (ledger mirror updates, drafts) — list what changed.
- Proposals needing approval, numbered so the SA can reply "go ahead with 1, 3":
  - New Rocketlane task creations
  - Rocketlane status changes / closures
  - Any other external-system write
- For attention: items with no deadline, ambiguous signals, desyncs (§12), possible duplicates,
  anything the API/connector couldn't do (§8, §9, §1 placeholder).

## 16. Daily operational flow

Clarifies how a daily/recurring run should actually behave, on top of the rules above — this is the
Rocketlane-reconciliation piece of `CLAUDE.md`'s "Recurring Health Check Automation":

1. Pull all live tasks in the Rocketlane project linked in `PROJECT.md`'s header. **This pull's
   task-ID set is also the input to §19's mandatory sweep below — run it every time, not only when
   something seems off.**
2. **Apply the ledger mirror-back (§3/§7) directly to `ACTION-TRACKER.md` — don't just report the
   drift in chat.** This write is already pre-approved (§13, no SA sign-off needed). Make it as a
   normal surgical edit (see `CLAUDE.md`'s "make surgical edits" rule). For an unattended scheduled
   firing, land it on a branch via PR per `CLAUDE.md`'s "Recurring Health Check Automation" section
   — never commit straight to `main` with nobody watching. In an interactive session with the SA
   present, applying it directly (with a PR still available on request) is fine.
3. Run the daily catch-up scan of new notes (Granola/Gmail/Slack/etc.) per the existing capture
   rules in `CLAUDE.md` — unchanged and out of scope of this file.
4. **Every run, do a full scan of `ACTION-TRACKER.md` Sections A and B for creation candidates —
   not only items surfaced by that run's own catch-up scan.** A row counts as a candidate when it
   has no live Rocketlane task cited or findable, its `Raised` date isn't from this run, and its
   Status doesn't already say "Discarded"/"deleted"/"not tracked as a Rocketlane task" (skip rows
   already marked that way — don't re-propose them). Without this, a routine that only proposes
   same-run findings will silently let real backlog items sit untriaged indefinitely — confirmed
   in practice on a live engagement, where ~25 rows raised over several weeks had never been
   proposed because no single run's catch-up scan happened to touch them. For each candidate found
   this way, apply the same grouping/parent-child check (§4), ownership boundary (§5), and naming
   rule (§4) as any other candidate before proposing it — and separately flag, without proposing
   automatically:
   - Rows that turn out to already be covered by an existing Rocketlane task under a different
     row/topic (cross-reference it, don't create a duplicate).
   - Rows that read as clearly moot now (the underlying question was resolved through another
     channel — an ADR, a decision log entry, a different risk closing).
   Any newly identified action item — from the catch-up scan or from this full-ledger pass — is
   written **directly into `ACTION-TRACKER.md`'s Section C ("New Task Candidates (pending SA
   review)") immediately — no chat approval needed for this write.** Section C is the review
   surface instead of a pre-write chat question: it's rendered as its own table on the site
   dashboard's Tasks tab (`.preview/index.html#dashboard:tasks`), and also surfaced in this run's
   own chat/notification output per step 4 of `CLAUDE.md`'s "Recurring Health Check Automation"
   (don't rely on a bare pointer into the file — paste what's new). The SA reviews pending rows
   there and replies to approve or discard each one. This does **not** relax §13/§16 step 2's
   requirement that the actual Rocketlane `create_task` call still needs explicit SA approval —
   only the *ledger write* proposing the candidate is pre-approved, the same way §3/§7's
   mirror-back already is. When the SA discards a batch of stale/never-actioned candidates in
   bulk, mark each Section C row discarded per step 5 below (a mirror-back-style edit that needs
   no approval) rather than leaving them to resurface unchanged on the next full scan.
5. Ledger bookkeeping once the SA acts on a previously-proposed candidate:
   - **New candidate found** → write it straight into Section C immediately (see step 4 above) —
     this is the row the SA reviews; no approval needed for this write.
   - **Approved and created in Rocketlane** → move the row from Section C into Section A or B as a
     normal tracked row, with its task ID/link — the same mechanic already used whenever a new
     Rocketlane task is linked — and mark the Section C row `✅ Approved — see §A.N`/`§B.N` rather
     than deleting it.
   - **Discarded** → keep the row in Section C, add a status note saying it was discarded. **Never
     delete a ledger row for a discarded candidate** — the history of "this was considered and
     rejected" stays visible even though the practical outcome (no live Rocketlane task) is the
     same either way.
6. The SA edits Rocketlane directly day to day (status changes, task deletions, new tasks) and
   expects all of that to be reflected in `ACTION-TRACKER.md` the next run via step 2 — this is the
   entire point of §3's mirror direction. There is no scenario in this flow where Rocketlane should
   be changed to match the ledger.

## 17. Continuity across unmerged reconciliation PRs

An unattended run lands its ledger mirror-edits and creation proposals on a branch + PR (§16 step
2, per `CLAUDE.md`'s "Recurring Health Check Automation"). If the SA hasn't merged that PR yet by
the time the *next* run fires, and that next run only reads `ACTION-TRACKER.md` off `main`, it is
reading a stale copy — it has no way to know what the pending PR already did. Concretely, this
causes two failure modes:

- **§12 false orphans:** a Rocketlane task the pending PR already linked via `externalReferenceId`
  still looks unlinked from `main`'s point of view, so the new run reports it as an orphan needing
  resolution when it's already been handled.
- **§6 duplicate proposals:** a creation candidate the pending PR already proposed (or, once
  approved, already created in Rocketlane and linked) gets proposed again from scratch, since the
  run reading `main` has no memory of the earlier proposal.

So, before pulling Rocketlane and starting the reconciliation logic (i.e. before §16 step 1):

1. Check whether an open PR from a previous reconciliation run already exists against
   `ACTION-TRACKER.md`.
2. If one does, **check out that PR's branch** (not `main`) and run the full reconciliation
   against that branch's version of the ledger — it reflects the latest known state, merged or not.
3. Commit this run's own mirror-edits and creation proposals on top of that same branch, updating
   the existing PR, rather than opening a second PR that touches the same rows.
4. Only target `main` directly (or branch fresh off it) when no such PR is open.
5. If the same PR has been open unmerged for several days, say so explicitly in the run's §15
   report (e.g. "PR #N open since <date>, awaiting merge") — don't let it go unmentioned while more
   runs keep stacking commits onto it.
6. This is purely about which copy of the ledger a run reads/writes — it doesn't change anything
   about Rocketlane writes themselves. Creation/update proposals still need explicit SA approval
   before any Rocketlane call, regardless of which branch they were drafted against.

## 18. Section A/B scope — live Rocketlane task required

`ACTION-TRACKER.md`'s Sections A and B feed the site dashboard's Tasks tab as if every row were a
live Rocketlane task the SA needs to act on there. Left unchecked, the ledger can accumulate rows
that never had, and were never meant to have, a Rocketlane counterpart — meeting-attendance
confirmations, pure logistics/scheduling asks, "discarded as stale" items, tasks the SA deleted
directly in Rocketlane — which then show up on the Tasks tab implying they're open Rocketlane
tasks when they aren't.

**A new Section A/B row may only be added once it has (or is being created with) a live Rocketlane
task carrying the same name** — the row and the Rocketlane task are two views of the same thing,
kept in sync (`create_task` → new row; a Rocketlane edit/completion → mirror into the row per
§3/§7; a Rocketlane deletion → mirror the deletion into the row's Status, per the existing
never-delete-a-row convention — the row stays, marked deleted, it just also stops qualifying as
live per this rule).

- An item that doesn't warrant a Rocketlane task at all — §4's "attendance-only is not a task"
  rule, a one-off logistics/scheduling ask, something resolved same-day through email/Slack — is
  **not** added to Section A/B as a row. If it's worth a mention, note it in that run's
  narrative/chat output or a `JOURNAL.md` entry instead; don't create a ledger row with no
  Rocketlane counterpart just to have a record of it.
- An item that *does* warrant a task but doesn't have one yet still goes through the existing
  Section C → A/B flow (§16 steps 4–5): land it in Section C first, only move it into Section A/B
  once the SA approves and it's actually created in Rocketlane.
- **This is not retroactive on an existing repo that adopts this rule mid-engagement.** Pre-existing
  Section A/B rows without a live Rocketlane link (meeting-logistics items, discarded-as-stale
  rows, tasks confirmed deleted in Rocketlane) stay as historical record — never delete, per the
  standing convention — they're simply no longer the pattern to follow for anything new.
- The dashboard enforces the surfacing half of this: `.preview/index.html`'s Tasks tab only renders
  a Section A/B row when its Source column carries a Rocketlane task link that isn't itself marked
  removed/deleted/not-found — see `hasLiveRocketlaneTask()`. A row can legitimately exist in the
  ledger (history) without ever showing up there (not a live task) — that's the point, not a bug.

## 19. Full task-ID sweep — every citation, every run (added 2026-09-22, pulled forward from bestbuy-b2b-ca)

§18 depends entirely on the ledger's Status/Source text staying accurate — the dashboard only knows
a row is "not live" because the text says so. §7/§16 step 2 already require mirroring drift when
it's *found*, but nothing before this rule made finding it mandatory and exhaustive. A "full re-pull
of live tasks" run that only compares the **total task count** between successive pulls ("same count
as last time") and treats an unchanged count as "no drift" is blind by construction: N deletions and
N unrelated new/completed tasks cancel out in the total, so a cited task can vanish or complete
without the count ever moving. On one live engagement this let an 11-row cluster of ledger rows sit
stale for at least 6 daily runs, showing on the dashboard as live open tasks the SA needed to act on
when none of them were. The same failure mode applies to any task cited only by a raw Rocketlane
task-ID link with no `externalReferenceId` to match on — which is most of Sections A and B on a
typical engagement — so this can't be treated as a one-off edge case.

**Required every run, not only when something looks off:**

1. Extract every literal Rocketlane task ID cited anywhere in Sections A and B (the `tasks/(\d+)`
   pattern in each row's Source column, plus any bare `Rocketlane task <ID>` mentions) into one set.
2. Diff that set against the current live pull's task-ID set (§16 step 1). **Never substitute a
   count comparison for this diff** — matching totals proves nothing about which specific tasks
   changed.
3. For every cited ID **not** present in the live pull, do an individual lookup (`get_tasks` by
   `taskId`) to tell deletion (403/not-found) apart from a pagination artifact of the bulk pull.
   Mirror the result into that row per §3/§7 — no approval needed, this is Rocketlane → ledger, same
   as any other drift.
4. For every cited ID that **is** present but whose live `status`/`taskName`/assignee no longer
   matches the row, mirror that too (already required by §7 — this sweep is what makes sure it
   actually gets checked, instead of relying on drift being noticed incidentally).
5. Report the sweep's scope in the run's output (e.g. "swept N cited task IDs, found M drifted") so
   a future run — or the SA — can tell a real "nothing changed" from a sweep that silently didn't
   run.

This sweep is what §16 step 1 refers back to. It applies to every row with a live-looking Rocketlane
citation, regardless of how old the row is or whether it's ever been touched by a prior mirror-back —
staleness compounds silently otherwise, since nothing else re-visits a row once it's first linked.
