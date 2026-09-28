# Working in this repo (rules for AI assistants)

This is a VTEX Professional Services client project repo, created from
[`vtex-client-project-template`](https://github.com/vtexprojects/vtex-client-project-template).
If you are an AI helping someone work in this repo, these rules apply automatically.

**This template ships pre-built.** `STRUCTURE.md`, `PROJECT.md`, `CHECKLIST.md`, and `JOURNAL.md`
already exist at the root with `{{DOUBLE_BRACE_PLACEHOLDERS}}` — they are not generated from
scratch by a skill at initialize time the way earlier versions of this template worked. Your job on
a freshly-cloned repo is to **fill in the placeholders and validate the setup** (see the checklist
below), not to invent a folder structure or scaffold new core files.

## Setup Validation Checklist (run this first, every session)

Before doing anything else in this repo, check whether it's actually finished being set up. Don't
assume a fresh clone is ready just because the four core files exist — they exist in every clone of
this template, filled in or not.

1. **Are the placeholders actually filled in?** Grep `PROJECT.md` for `{{` — if you find any, this
   repo hasn't been initialized yet. Stop and run initialize mode (below) before anything else.
2. **Does `PROJECT.md`'s header have a real Rocketlane Project ID?** Not a placeholder, an actual
   number.
3. **Does that Rocketlane project actually exist?** Call `get_projects` by that ID. If it 404s or
   the ID looks fabricated, treat this as unset — don't proceed as if it's linked.
4. **Does that Rocketlane project's "GitHub Repository" custom field match this repo's slug?**
   Pull the project with `includeAllFields: true` and check the custom field value against this
   repo's actual `owner/name`. Three outcomes:
   - Matches → good, nothing to do.
   - Set to something else → flag it to the SA before touching it; don't silently overwrite a
     value someone else may have set intentionally for a different reason.
   - Empty/unset → write this repo's slug into it, but **confirm with the SA first** — Rocketlane
     is a shared, live system, not a scratch space.
5. **Is the recurring Project Health Check automation set up?** Check for an existing Routine (list
   your available scheduled-trigger tooling) targeting this project. If none exists, set one up
   per "Recurring Health Check Automation" below — but ask the SA first about cadence and how they
   want to be notified, don't assume the default cadence there is right for every engagement.
6. **Has the Project Health Check itself ever been run?** Check `CHECKLIST.md`'s "Project Health
   Check" section for a real "Last run" date. If it still says "Never yet," run it now (see
   `STRUCTURE.md`'s Agent Instructions and `CHECKLIST.md`'s Project Health Check section for the
   method).
7. **Is the weekly Template Sync Check automation set up?** Check for an existing Routine (list
   your available scheduled-trigger tooling) targeting this project for that specific purpose. If
   none exists, set one up per "Template Sync Check" below — ask the SA first about cadence
   (weekly is the default) and how they want to be notified.
8. **Is the weekly Status Log Check set up, as its own Routine separate from the daily Health
   Check?** Check for an existing Routine (list your available scheduled-trigger tooling) targeting
   this project specifically for the Status Log cadence check — this is a different Routine from
   item 5, not another trigger on the same one. If none exists, set one up per "Weekly Status Log
   Check" below — ask the SA first about cadence (default: weekly, every Monday) and notification
   preference.
9. **Is the private, shared Claude Cowork project for this engagement set up?** Check
   `PROJECT.md`'s Quick Facts for the "Claude Cowork project" row. If it still says "Not yet
   created," surface "Claude Cowork Project Setup" below to the SA — there is no tool or connector
   in this session that can create a Cowork project directly, so this always needs a manual step
   from the SA, not a write you can make yourself. This is also re-surfaced daily by the Recurring
   Health Check Automation (below) while it stays unset, so it isn't only caught when a fresh
   session happens to run this checklist.
10. **Is `PROJECT.md`'s "Monitored Sources" table filled in and confirmed by the SA?** Every
    recurring automation reads its sources (Slack channel IDs, Granola folder, Read AI, recurring
    meetings, Gmail domains/labels, Drive folder, Zendesk, VTEX accounts) from that table. If a
    row is empty or still marked `⏳`, **ask the SA for those values in one grouped message** and
    write the answers into the table — don't leave them living only in a chat, a personal memory
    file, or an inference from past scans. Values you can pull from a connector (e.g. listing
    Granola folders or Slack channels) are fine to propose, but they stay `⏳` until the SA
    confirms them. A catch-up scan against an unconfirmed source list should say so in its output
    rather than present its coverage as complete.
11. **Is the dashboard published to private GitHub Pages?** Check `PROJECT.md`'s Quick Facts
    "Dashboard (GitHub Pages)" row. If it still says "Not yet published," set it up per
    "Dashboard Publishing" below, right away, without asking first (standing authorization, see
    that section).

Only after this checklist passes (or you've surfaced to the SA what's missing and why) should you
treat the repo as "a normal day in the life of an ongoing engagement" rather than "still being set
up."

## Initialize mode (day zero — repo just created from this template)

1. Ask for (or pull from whichever connectors are available — Rocketlane, Google Drive, Slack,
   Gmail, meeting-notes tools): client/project name, VTEX Principal Solution Architect name and
   email, the Rocketlane Project ID and URL, brands in scope, System Integrator name, countries in
   scope, language footprint (multilanguage true/false, which languages), and the client's key
   stakeholders (name + role, for `PROJECT.md`'s Client Stakeholders table). Also pull the
   Rocketlane project's phases (`get_phases`) for `PROJECT.md`'s header — write "Not yet defined"
   if the project doesn't use phases rather than leaving the placeholder unfilled. Pull first, ask
   only for what's still missing, grouped into one message.
   - **In the same message, ask the SA for the automation data that fills `PROJECT.md`'s
     "Monitored Sources" table** — the automations can't work reliably without it, and none of it
     can be safely guessed:
     - Slack channels and DMs to monitor (name + channel ID), and any long-running threads worth
       re-checking.
     - Granola folder (name + ID — list folders with `list_meeting_folders` and propose a match),
       and whether Read AI or another meeting-notes tool is also used.
     - Recurring meetings (weekly client sync, architecture check-ins, internal syncs).
     - Gmail: client and SI email domains, any labels used, other senders worth watching.
     - Google Drive project folder URL, and where documents received from the client/SI should be
       filed (Hard Rule 14).
     - VTEX accounts: production, QA/stage/dev, and which sandbox/partner accounts are *not* the
       client's.
     - Zendesk/support ticket tracking, if any.
     - Automation preferences: cadence for each Routine (Health Check, Status Log, Template Sync),
       how they want to be notified, and whether `JOURNAL.md`-only entries may commit directly to
       `main` or must always go through a PR.
   - Write every answer into the repo (`PROJECT.md`'s Quick Facts and Monitored Sources, marked
     `✅ Confirmed`) before creating any Routine — the Routines read from the repo, not from this
     conversation.
2. **Multi-contract check:** before filling anything in, check whether another repo already exists
   for this client. If this new engagement is actually a new contract/phase for an existing client
   repo, that should be a new row in *that* repo's `PROJECT.md` Rocketlane Projects table, not a
   second repo — flag this to the SA rather than initializing a duplicate.
3. Replace every `{{PLACEHOLDER}}` in `STRUCTURE.md`, `PROJECT.md`, `CHECKLIST.md`, and
   `JOURNAL.md` with real values. Leave anything genuinely unknown (architecture, integrations,
   requirements that depend on a SOW/Blueprint handoff) as "Pending — awaiting SOW/Blueprint
   handoff" rather than inventing plausible-sounding content — this is the single biggest thing
   that makes an initialize pass feel slow and untrustworthy when done wrong.
4. Write this repo's slug into Rocketlane's "GitHub Repository" custom field (confirm with the SA
   first — see the Setup Validation Checklist above).
5. Set up the recurring Project Health Check automation (below), after confirming cadence and
   notification preference with the SA.
6. Run the Project Health Check once, for real, and record the result in `CHECKLIST.md` and
   `PROJECT.md`'s header.
7. Publish the dashboard to private GitHub Pages per "Dashboard Publishing" below. Don't ask
   first; it runs in every initialize.
8. Report back: repo URL, dashboard URL, confirmation the four files are filled in, whether the
   Rocketlane custom-field write succeeded, health-check automation status, and a short list of
   what's still genuinely pending — so the SA has one clear follow-up list.

## Dashboard Publishing (GitHub Pages)

The docs preview / dashboard (`.preview/`) is published to **private** GitHub Pages by
`.github/workflows/dashboard-pages.yml` on every push to `main`. Anyone with read access to this
repo can then open it without cloning or running a local server. `.preview/build_site.py`
produces the site. The site mirrors `main` as of the last deploy, not open branches/PRs or
unpushed local changes; localhost stays the working view for those.

The workflow can't turn Pages on by itself, because the default `GITHUB_TOKEN` has no
repo-administration permission. So the first setup runs once, from the SA's own `gh` login. The
SA needs admin on the repo, which they normally have as its creator.

**Standing authorization (set 2026-09-24 so every project gets its dashboard): run this setup without asking the SA first**, in every initialize
and whenever Setup Validation Checklist item 11 finds it missing. This is a deliberate exception
to the "confirm before changing configuration" discipline. It covers only these Pages steps, and
only with visibility private. Say in the session output that it ran and give the URL. Every
other settings change still needs confirmation.

1. Check whether Pages already exists: `gh api repos/<owner>/<repo>/pages`. A 404 means it isn't
   set up yet.
2. Create it with workflow-based builds:
   `gh api -X POST repos/<owner>/<repo>/pages -f build_type=workflow`
3. **Make it private, immediately, before any deploy:**
   `gh api -X PUT repos/<owner>/<repo>/pages -F public=false`. Then confirm
   `gh api repos/<owner>/<repo>/pages --jq .public` returns `false`. The site contains contract
   and client data, so never skip or reorder this step. The workflow's "Refuse to publish a
   public site" step also blocks any deploy while visibility isn't confirmed private, as a second
   line of defense.
4. Trigger the first deploy with `gh workflow run dashboard-pages.yml`, and wait for it with
   `gh run watch`.
5. Record the URL (`gh api repos/<owner>/<repo>/pages --jq .html_url`) in `PROJECT.md`'s Quick
   Facts "Dashboard (GitHub Pages)" row, as a surgical edit through the normal branch + PR path.

If step 2 or 3 fails with a permissions error, the SA isn't an admin on the repo. Stop there and
tell the SA which org admin to ask. Don't retry with a different token. A private site's
`*.pages.github.io` subdomain is assigned by GitHub and can't be changed; a shorter URL needs a
custom domain, which requires a DNS record from VTEX IT/Infra.

## Recurring Health Check Automation

The Project Health Check (see `CHECKLIST.md`) and a catch-up scan across whatever connectors are
available this session (Granola, Read AI, Slack, Google Drive, Gmail, and any others connected —
new meetings, relevant channel/email activity, new documents) are both far more useful running on
a schedule than only when someone remembers to ask. **Default cadence: daily, every morning** —
confirm with the SA rather than assuming this fits every engagement; a quieter account may prefer
weekly instead.

**Before creating a new Routine, check whether one already exists** for this project (list your
available scheduled-trigger tooling, filtered to this repo/client) — never create a duplicate. If
none exists, set one up per the instructions below, after confirming cadence and notification
preference with the SA (see the Setup Validation Checklist above).

**What the routine should do, each time it fires:**

1. Run the Project Health Check — `CHECKLIST.md`'s "Project Health Check" section has the method:
   compare live Rocketlane data (phases, hours, dates) against what `PROJECT.md`/`CHECKLIST.md`
   currently say.
   - **As part of this step, also check whether the project's Rocketlane Status Log needs an
     off-cycle refresh — the *event-triggered* half of that check only.** The Status Log is
     weekly by default (owned by the independent "Weekly Status Log Check" routine below), so
     this daily run should **rarely** draft one. Draft one here **only** if this run turned up
     something that changes the project's story: a significant change in client mood, a
     significant delivery delay, or a major blocker/unblocker — see `CHECKLIST.md`'s Project
     Health Check section for the exact (deliberately narrow) trigger list. Routine movement — a
     risk updated, an ADR promoted, a small progress change — is **not** a trigger; it waits for
     the weekly draft. When in doubt, don't draft. When a refresh is due, draft it in the format
     specified by `Internal Documents/Project Management/Governance/STATUS-LOG-RULES.md` — same
     "suggest, never silently write" discipline as everything else Rocketlane-facing (see step 4
     below).
   - **Also check whether the private, shared Claude Cowork project for this engagement has been
     created yet** — `PROJECT.md`'s Quick Facts "Claude Cowork project" row. While it still reads
     "Not yet created," this is a standing pending SA action, not a one-time FYI — re-surface it
     every run per step 4 below, the same persistence rule as a pending Rocketlane suggestion,
     until the SA either creates it (and updates that row) or explicitly says to drop it. See
     "Claude Cowork Project Setup" below for what to surface (the manual steps and standard
     prompt).
2. Run a catch-up scan across every source listed in `PROJECT.md`'s "Monitored Sources" table
   whose connector is reachable this session (Granola, Read AI, Slack, Google Drive, Gmail,
   calendar, etc.) — read the listed channels/folders/filters directly rather than rediscovering
   them each run; if a row is still `⏳` or empty, say so in the run's output — for this project,
   since the last time the routine ran (or since the last real filing
   session, for its first run) — new meetings, relevant channel/email activity, new shared
   documents. Same discipline as any other filing pass applies: validate a document actually has
   usable content before filing it (Hard Rule 9), don't fabricate what wasn't found, and don't
   claim a source was checked if its connector wasn't actually reachable this run.
   - **Slack mention sweep, thread replies included — every run.** A channel read with `oldest` =
     last run returns only top-level messages, so a request made to a VTEX SA as a *reply* inside
     an older thread was confirmed in practice to go unseen by every run. On top of the
     per-channel reads, search every Slack channel in `PROJECT.md`'s Monitored Sources for
     messages since the last run that mention one of the VTEX SAs listed in `PROJECT.md` (by Slack
     user ID and name) or VTEX by role, **including replies inside older threads**. For each hit
     that asks a VTEX SA to do, check, or answer something: dedup against `ACTION-TRACKER.md`
     Sections A–C first; if not already tracked, write a Section C candidate (owner = the person
     named, else the default assignee per `ROCKETLANE-RECONCILIATION-RULES.md` §6), and add the
     thread to `PROJECT.md`'s "Slack long-running threads" Monitored Sources row so later replies
     are re-read. A Slack reply alone never creates the Rocketlane task — that still needs SA
     approval (`ROCKETLANE-RECONCILIATION-RULES.md` §13/§16). Report the result in the run output
     ("Slack mentions: N new, M already tracked", or "none").
   - **A meeting-notes tool's own summary is not the transcript, even when the tool markets itself
     as "full detail."** Confirmed in practice on a live engagement: two different by-ID/by-query
     meeting-summary calls to the same note-taking connector each independently omitted real,
     explicit decisions a person made in the meeting (a milestone to delete, risks to remove, a
     third risk discussed by name) — pulling the connector's actual transcript tool surfaced all of
     it. Default to the summary tools for routine "anything new?" browsing — they're cheaper and
     usually sufficient. But before a meeting's content drives an actual register/milestone/ADR edit
     (closing or removing a risk, changing a milestone, correcting a decision record) — or for any
     internal working-session-style meeting where people make quick calls a summarizer tends to
     compress away — pull the verbatim transcript instead of trusting the summary as complete.
   - **ADR / Behavior Note candidate check — every run, not only when a meeting is captured.**
     On a live engagement, a VTEX Support ticket reply confirmed a per-account feature flag and
     exactly what it changes. That confirmation landed only as a risk-row update and never became a
     Behavior Note, because no step here asked the question. Drafts had only come from
     `vtex-meeting-decision-capture` or an explicit request in chat. For everything this run's
     health check and catch-up scan turned up (meetings, Slack/email threads, VTEX Support tickets,
     Rocketlane comments, live-test notes), ask:
     - **Behavior Note candidate?** A VTEX platform behavior confirmed by an authoritative source,
       such as an API contract, default, or limit, a per-account feature flag and what it changes,
       a status transition, or a protocol constraint. Authoritative sources are a VTEX Support or
       product-team reply, VTEX docs, a reproduced live test, or the SA stating it directly.
     - **ADR candidate?** An architecture or design decision that was actually made, with a
       decider or forum, a date, and a chosen option. An open question with options on the table
       is not an ADR. It belongs in a Section C topic or a Section D risk instead (Hard Rule 13).
       Also check open risks and topics that note an ADR is still pending, in case their decision
       has now landed.
     - **Dedup first.** Check `ADRs/` and `Behavior Notes/` (`Drafts/`, `Accepted/`, `Retired/`)
       and `CHECKLIST.md` Section F. If an existing document already covers it, propose an edit to
       that document instead of a new draft, and follow Hard Rule 12 if it carries a `✅`.
     - **If it clears the bar**, pull the verbatim source first (full ticket, transcript, or
       thread, not a summary). Then write `DRAFT-BN-<slug>.md` / `DRAFT-ADR-<slug>.md` into the
       matching `Drafts/` folder as part of this run's PR. Use the `vtex-behavior-note` /
       `vtex-adr-writer` template if that skill is available; otherwise match an existing file in
       the same folder. Cite the exact source (ticket number, meeting + date, thread timestamp),
       and mark anything not yet verified as unverified. Never write into `Accepted/`, and never set
       `reviewed_by`, `Atlas candidate`, or `Atlas approved`. If the source is too thin to support
       a real draft (Hard Rule 9), list it as a "possible candidate" in the run output instead of
       filing it.
     - **Always report the result.** Every run's output gets an "ADR / BN candidates" section
       listing each new draft (title, source, one-line reason), each proposed edit, and each
       possible candidate, or "none found this run", so a miss is visible. Record the same line in
       `CHECKLIST.md`'s "Last run" findings. A new draft is a real repo change, so it goes through
       the branch + PR path in step 3, never the `JOURNAL.md`-only direct-commit exception.
   - **Register consolidation check — every register, every run.** The write-time half is Hard Rule 15: every record this run creates or updates goes through that check first. On a live engagement, a topic
     stayed open although the project's open-points tracker already covered everything it had
     left, and no run flagged it: the health check compared Rocketlane against the repo, but never
     compared the repo's own records against each other. This check does that, and also checks
     each record against what it points to. It covers every register: Topic Analysis docs and
     `CHECKLIST.md` Section C; ADRs and Behavior Notes (files in `Drafts/`/`Accepted/`/`Retired/`
     plus Section F); Section D risks; Section E milestones; Section H customer needs; Section I
     roadmap watch; and `ACTION-TRACKER.md` Sections A–C. For every record that isn't closed, done,
     or retired, ask the same questions:
     - **Duplicate or covered elsewhere?** Is the same point already tracked in another record or
       register, such as a topic or risk whose open questions all sit in another document, two
       risks describing one issue, a Section C candidate that already exists as a Section A row,
       or a Behavior Note draft that repeats an Accepted one? Propose merging or closing one, and
       point to the survivor.
     - **Resolved by a later record?** Did an Accepted ADR, a Behavior Note, a confirmed decision,
       a completed Rocketlane task, or a newer meeting/thread settle it? Examples are a risk whose
       mitigation landed, a topic whose decision became an ADR, a draft ADR that a later ADR
       superseded, or a task whose deliverable is filed. Propose closing it, or marking it
       partially resolved, with the source cited.
     - **Parked but not closed?** A status like "stored" or "historical", a "superseded" note
       inside the file, a draft untouched for weeks, or a "waiting on X" where X already happened.
       These read as done but aren't. Propose a real status: closed, retired, or active again with
       a next step.
     - **Out of sync with its own references?** The register row and the document disagree
       (status, severity, version, owner), a cross-reference points to a renamed or retired ID, or
       an `ACTION-TRACKER.md` row disagrees with its live Rocketlane task. Propose the correction.
     - **Missing from its register?** A file with no register row, a risk mentioned in the docs
       but absent from Section D, or a Rocketlane task with no ledger row. Flag it, since nothing
       else will ever surface it.
     - **Propose, don't close silently.** Put every proposed change in the run's PR. For
       documents, add a "Closed/Retired <date> — <why, and where the remaining points live>" note
       after the title (Hard Rules 12–13: never move or convert a Topic into an ADR, never touch
       `✅` fields). Update the matching register status too. Name each proposal in the run output,
       grouped by register, so the SA can approve or reject it. Rocketlane-side effects (closing a
       task, for example) are suggestions in chat, per "Keeping Rocketlane aligned". Report
       "Register consolidation: N proposals (Topics a, ADR/BN b, Risks c, Milestones d, Tasks e,
       Other f), M missing register rows", or "none", and record the same line in
       `CHECKLIST.md`'s "Last run" findings. Like a new draft, this goes through the branch + PR
       path in step 3, never the `JOURNAL.md`-only direct-commit exception.
3. **Never commit directly to `main` or write silently for `PROJECT.md`, `CHECKLIST.md`, new
   meeting-note files under `meetings/`, or anything Rocketlane-relevant.** For those, create a
   branch, make the proposed updates, and **open a pull request** for the SA to review — the same
   "suggest, don't silently write" discipline this file already applies to Rocketlane updates (see
   "Keeping Rocketlane aligned with what gets filed here" below) applies here too, just enforced
   structurally through a PR instead of a chat message, since no one is watching an unattended
   scheduled run in real time to approve something inline.
   - **Exception: a `JOURNAL.md`-only entry may commit directly to `main`**, skipping the
     branch/PR step — but only when the entry is purely additive (respects Hard Rule 2:
     append-only, newest entry first, never editing or deleting a past entry) and the run touches
     nothing else — no `PROJECT.md`, `CHECKLIST.md`, or `meetings/` file change, and no
     Rocketlane-worthy finding. The moment a run's findings also warrant a `PROJECT.md`/
     `CHECKLIST.md` change or a Rocketlane suggestion, the whole batch — including the
     `JOURNAL.md` entry — goes through the normal branch+PR path instead, so the suggestion has
     somewhere to surface for SA review; don't split one run's output across a direct commit and a
     PR. Confirm this carve-out's cadence/notification preference with the SA same as the rest of
     this automation — a quieter account may prefer every entry to go through a PR regardless.
   - **Before creating that branch (for changes that still require one), check whether an open PR
     from a previous automated run already exists** touching the same files (`PROJECT.md`/`CHECKLIST.md`/`JOURNAL.md`, or the
     `ACTION-TRACKER.md` ledger — see
     `Internal Documents/Project Management/Governance/ROCKETLANE-RECONCILIATION-RULES.md` §17 for
     the Rocketlane-reconciliation case). If one does, **check out and build on that branch**
     instead of starting fresh from `main` — commit this run's updates on top of it and push to the
     same PR rather than opening a new one. A run that only ever reads `main` is blind to whatever
     a still-open PR already proposed or already mirrored, which causes two real failure modes:
     re-flagging the same drift or proposal a pending PR already captured, and separate unmerged
     branches quietly diverging from each other. Only start a fresh branch from `main` when no open
     PR from a prior run exists, or once the SA has merged or closed the previous one.
   - If a PR from this automation has sat open and unmerged for several days, say so plainly in
     the run's output (e.g. "PR #N open N days, awaiting your review") — don't let reconciliation
     output silently pile up unreviewed.
4. If a real, Rocketlane-worthy change turns up (a milestone done, a risk opening/closing, a phase
   transition, or an off-cycle Status Log refresh per step 1 above), **surface it directly in the
   run's chat/notification output as an explicit suggestion asking the SA to validate it — never
   rely on the PR description alone, and never rely on a pointer into `CHECKLIST.md` in place of
   the actual content.** The SA shouldn't have to open the repo to see a pending Rocketlane
   suggestion; state it plainly where the routine reports back (e.g. "Suggested Rocketlane update:
   mark Task X complete — confirm?" or, for the Status Log, **the full proposed note text, pasted
   inline in the chat/notification output itself** — "see CHECKLIST.md for the draft" does not
   satisfy this), and also echo it in the PR description when a PR is already being opened for other changes in
   the same run, so the two stay in sync. Don't write to Rocketlane from an unattended run — wait
   for the SA's explicit go-ahead in chat, same as any other Rocketlane write (see "Keeping
   Rocketlane aligned with what gets filed here" below).
   - **A pending suggestion that the SA hasn't responded to is not "done" once mentioned once.**
     Every subsequent run must check the open-proposal list (Rocketlane tasks, milestones, or phase
     changes suggested but not yet approved, edited, or discarded by the SA) and `CHECKLIST.md`'s
     "Status Log last suggested" vs. "last actually updated" lines; anything still open
     gets re-surfaced again, in full, at the very top of that run's output, above the health-check,
     reconciliation, and catch-up-scan sections. Treat it as the lead item the SA has to clear
     before the rest of that day's findings, not a footnote — a suggestion that only ever appears
     once and then silently rides along inside a PR description until someone happens to open it
     has failed the entire point of surfacing it. Stop re-surfacing only once the SA has actually
     responded (approve/edit/discard), not once some number of days has passed.
   - **The Cowork project check works the same way, even though it isn't a Rocketlane write.**
     While `PROJECT.md`'s Quick Facts "Claude Cowork project" row still reads "Not yet created,"
     surface the manual-creation steps and the standard prompt from "Claude Cowork Project Setup"
     below at the top of every run's output too, until the SA either creates it (update that row)
     or explicitly says to stop flagging it.
5. If nothing new is found, it's fine to skip opening a PR that day — don't open an empty or
   no-op PR just to prove the routine ran; a quiet notification (or none) is enough.

**Known constraint, confirmed in practice:** some orgs do not support explicitly attaching
connector access (e.g. Rocketlane) to a scheduled trigger — the `connectors` parameter on trigger
creation may be rejected outright ("not available for this organization"). If that happens:
- Bind the Routine to the *current session* (self-bind / default mode) rather than a fresh session
  per firing — a self-bound Routine resumes a session that already has its connectors live, rather
  than depending on connector grants attached to the trigger itself.
- **Test it immediately after creating it** — don't wait for the first real scheduled fire to find
  out whether it actually has Rocketlane access. Use your fire-immediately/test-fire tooling to
  trigger it once right after creation and confirm real data comes back, not a fabricated guess.
  Build the test instruction into the Routine's own prompt: if the relevant connector tools aren't
  reachable when it fires, it should say so via notification and touch no files, never fabricate
  numbers to fill the gap.
- If self-bound, remember the Routine depends on that specific session still existing. If the
  session is ever archived or the environment is torn down, the Routine will need to be recreated
  against a live session.

## Template Sync Check

This repo was created from
[`vtex-client-project-template`](https://github.com/vtexprojects/vtex-client-project-template),
which keeps evolving after any one client repo forks from it — new Hard Rules, corrected wording,
new automation sections. Nothing pulls those updates in automatically, so without a deliberate,
recurring check this repo's `CLAUDE.md`/`STRUCTURE.md` quietly drift out of date — this already
happened for real (see the PR that reconciled this repo against the template).

**Before creating a new Routine, check whether one already exists** for this project for this
specific purpose (list your available scheduled-trigger tooling, filtered to this repo/client) —
never create a duplicate. If none exists, set one up (weekly is a reasonable default; confirm
cadence and notification preference with the SA).

**What the routine should do, each time it fires:**

1. Get the current `CLAUDE.md` and `STRUCTURE.md` from
   `vtexprojects/vtex-client-project-template`'s `main` branch — use a local sibling clone if
   one's available on this machine, otherwise fetch the raw files directly from GitHub.
2. Diff them against this repo's own `CLAUDE.md`/`STRUCTURE.md`, **ignoring differences that are
   just this project's own values** (client/SI name, brand subfolders, version/date headers) — the
   comparison is about generic process rules, not this project's own content.
3. For each genuinely new or changed rule on the template side, judge whether it's a real gap this
   repo is missing, or something this repo deliberately diverged from for a reason specific to
   this engagement — don't blindly overwrite a deliberate customization just because the template
   moved on.
4. **Never commit directly to `main` or silently overwrite this repo's rules.** If there's
   anything worth pulling in, open a branch + PR summarizing what changed on the template side and
   what's being proposed here — same discipline as the Recurring Health Check Automation above.
5. If nothing new turned up, skip opening a PR — a quiet notification (or none) is enough.

This check is one-directional (template → this repo). The reverse — a genuinely reusable
improvement made here that should go back into the template — is still something the SA has to
notice and act on manually; nothing automates that side yet.

## Weekly Status Log Check

The project's Rocketlane Status Log is the internal/SA status narrative (client mood, overall
status, key decisions, risks, next steps) that anyone reading only Rocketlane sees. It needs a
periodic refresh even in a quiet week — a note saying "still on track, nothing new" is itself
useful — but it should **not** become a daily note. **Weekly is the norm**; an off-cycle refresh is
the exception, reserved for a real change in the project's story (see the event-triggered half
below).

**Publishing mechanism:** the Status Log is published as a native Rocketlane status-update entry,
not written into a custom field. Use the dedicated Rocketlane Status Log connector
(https://claude.ai/directory/a688602a-1c33-430e-ac61-c400c3afbae4) for all Status Log reads and
writes:
- `rocketlane_list_status_updates(project_id)` — published entries, to check what's already live
  and when it was last published.
- `rocketlane_get_field(field_id)` — picklist metadata, e.g. field `1928042` ("Status Log Customer
  Mood": Very Satisfied / Satisfied / Neutral / Dissatisfied / Highly Dissatisfied).
- `rocketlane_publish_status_update(project_id, overall_status, notes, customer_mood, ...,
  confirm)` — writes and publishes. `overall_status` is 1 (on track) / 2 (ahead of time) / 3
  (running late) / 4 (at risk). Always requires the SA's go-ahead in chat first (see "Always
  suggest, never silently write" below); call once with `confirm` omitted/false to preview, then
  again with `confirm: true` only after the SA approves. See
  `Internal Documents/Project Management/Governance/STATUS-LOG-RULES.md` for the note content
  format and the label mapping.

Don't write Status Log entries into Rocketlane's "Status Log Notes" custom field via
`update_project` — that was an older practice and the field is not the destination for new
entries.

**Two independent halves, two independent routines:**
- **Cadence-based** — owned by this routine, on its own schedule (**default: weekly, every
  Monday**), independent of whatever cadence the Recurring Health Check Automation runs on, so a
  quieter Health Check can't let the Status Log go stale.
- **Event-triggered** — runs as part of the Recurring Health Check Automation (its step 1), and is
  deliberately narrow: **only** a significant change in client mood, a significant delivery delay,
  or a major blocker/unblocker. Routine movement (a risk updated, an ADR promoted, a small progress
  change) is not a trigger — it goes into the next weekly draft. This narrow bar exists because a
  broader trigger list ("any risk opens/escalates/closes, any ADR, any mood signal") was confirmed
  in practice to produce a new draft almost every day on an active engagement.

**Before creating a new Routine, check whether one already exists** for this project for this
specific purpose (list your available scheduled-trigger tooling, filtered to this repo/client) —
never create a duplicate, and never conflate it with the Recurring Health Check Automation's own
Routine. If none exists, set one up per the instructions below, after confirming cadence and
notification preference with the SA (see the Setup Validation Checklist above).

**What the routine should do, each time it fires:**

1. Pull the live Rocketlane Status Log (`rocketlane_list_status_updates(project_id)`, most recent
   `publishedAt`) and compare against `CHECKLIST.md`'s "Status Log last actually updated" line. A
   refresh is due if that line still reads "Never yet" (immediately due, don't wait for a 7-day
   clock with no start date) or if 7 or more days have passed since that date. On a weekly-Monday
   cadence this will normally just mean "yes, due" every time — keep the 7-day figure as an
   explicit floor anyway, in case a run gets skipped or the SA moves the cadence.
2. If a real entry has already been published since the last check (the SA, or the Health Check's
   event-triggered half, already handled it), just confirm that and don't open a duplicate
   suggestion.
3. When a refresh is due, draft it in the format specified by `STATUS-LOG-RULES.md` — same
   "suggest, never silently write" discipline as everywhere else Rocketlane-facing.
4. Surface and record it the same way the Recurring Health Check Automation does (its steps 3 and
   4): a branch + PR for the `CHECKLIST.md` update recording the suggestion, and the full proposed
   note text pasted inline in the run's own chat/notification output — never just a pointer into
   `CHECKLIST.md`. A pending suggestion the SA hasn't responded to gets re-surfaced in full at the
   top of every subsequent run of *either* this routine or the Recurring Health Check Automation —
   they share the same "last suggested"/"last actually updated" state in `CHECKLIST.md` — until the
   SA approves, edits, or discards it in chat.
5. If a PR from this routine has sat open and unmerged for several days, say so plainly in the
   run's output, same as the Recurring Health Check Automation does.

This inherits the same self-bind/test-immediately discipline as the Recurring Health Check
Automation's "Known constraint" note above if `connectors` isn't supported on scheduled triggers
for this org — that constraint applies to any Routine here, not only the daily one.

## Claude Cowork Project Setup

This engagement should have a private, shared Claude Cowork project — a claude.ai workspace scoped
to this VTEX account, carrying grounding rules so any Claude session working this account defaults
to verified, account-specific answers instead of general VTEX knowledge (pattern sourced from
another VTEX PS engagement's equivalent setup).

**There is no tool or connector, from this repo or any session working it, that can create this
project automatically** — it's a claude.ai account-level object, not something git/CLAUDE.md
driven. Check `PROJECT.md`'s Quick Facts "Claude Cowork project" row: if it still says "Not yet
created," surface this section to the SA and ask them to create it manually:

1. In claude.ai, create a new Cowork project, set to private.
2. Name it consistently with this engagement (e.g. `{{PROJECT_NAME}}`).
3. Paste the prompt below (filled in for this engagement) as its instructions/system prompt.
4. Share it with whoever on the VTEX side needs access.
5. Once created, update `PROJECT.md`'s Quick Facts row with a link/name and today's date — this
   is a surgical edit to that one row, not a rewrite of the file (Hard Rule 6).

**Standard prompt template for this engagement** — fill in every `{{PLACEHOLDER}}` with this
engagement's real values before pasting; don't paste it with placeholders still in it:

```
This is a PS engagement for VTEX client {{CLIENT_NAME}}. Their real accounts are
{{PRODUCTION_ACCOUNT}} (production) and {{OTHER_REAL_ACCOUNTS}} (QA/staging/dev, as applicable) —
never assume something found in a test/sandbox account (like {{SANDBOX_ACCOUNT}}) holds true for
these without checking. {{SI_SHORT_NAME}}'s own sandbox/demo accounts, if any, are also not this
client's accounts — findings there are context only, never treated as confirmed for this client's
environments.

Engagement rules:
- Never invent or assume VTEX platform behavior, API responses, account configuration, or client
  data. If a VTEX connector or tool can answer it (account config, catalog, promotions, endpoints,
  docs), use it before answering — don't rely on general knowledge for anything account-specific
  or version-specific.
- If no connector can verify a claim, say so explicitly instead of guessing. "I don't have a way to
  confirm this — you'd need to check X" beats a plausible-sounding answer.
- When citing platform behavior (API defaults, config fields, endpoint contracts), prefer VTEX
  developer docs/endpoint lookups over memory of how VTEX "usually" works — the platform changes,
  and account-specific config (feature flags enabled per account only) can override defaults.
- State which account any finding applies to. Don't generalize a result from one account —
  especially a sandbox or the SI's own accounts — to this client's own environments.
- Flag known VTEX pitfalls proactively when relevant to this engagement's architecture — list them
  here as this engagement identifies them (e.g. a promotion-eligibility default that affects an
  adopted ADR, an auth constraint relevant to an open risk, a platform limit relevant to a
  requirement) — cross-reference the ADR/Behavior Note/risk each one affects.
- If a setup needs to be tested, do it against a disposable sandbox, never directly against this
  client's real accounts.

I'm the PS Solution Architect on this account — assume that context and skip re-explaining basic
VTEX concepts unless asked.
```

## Keeping Rocketlane aligned with what gets filed here

This repo and Rocketlane describe the same engagement from two angles — this repo is the detailed
working record (documents, decisions, risk write-ups), Rocketlane is the commercial/PM system of
record (tasks, phases, budget, dates) that other VTEX teams and the client see. They drift apart
silently unless something actively keeps them in sync, and drift is exactly what caused the
Contract-vs-Rocketlane budget mismatch that motivated the `Contract/` split (see Hard Rule 7).

**Whenever a commit to this repo reflects a real change in project state — not a docs-only
cleanup — check whether Rocketlane needs a matching update, and surface it to the SA as a
suggestion, don't apply it silently:**

- **A milestone in `CHECKLIST.md` Section E moves to done** → suggest marking the matching
  Rocketlane task/milestone complete (`update_task`), or creating one if none exists yet
  (`create_task`) — a milestone hit here with nothing to show for it in Rocketlane is invisible to
  anyone not reading this repo.
- **A risk in Section D opens, escalates, or resolves** → suggest logging or updating it as a
  Rocketlane task or project comment, especially anything that could affect the go-live date or
  budget — that's exactly the kind of thing an exec reading only Rocketlane needs to see.
- **A `Contract/Amendments/` entry gets filed** (new signed scope, hours, or term) → suggest the
  Rocketlane updates that should follow: adjusted budgeted hours, a new/extended phase, a revised
  due date — whatever the amendment actually changed. Never edit Rocketlane's numbers to match the
  amendment without saying so; suggest it explicitly so the SA can confirm before it goes live in a
  shared system.
- **`PROJECT.md`'s header status changes** (health color, phase, go-live date) in a way that isn't
  yet reflected in Rocketlane → suggest the corresponding phase transition or field update
  (`update_project`, `create_phase`/`update_phase`) rather than letting the two systems disagree
  about what phase the project is actually in.
- **An ADR or decision changes delivery scope or timeline** in a way Rocketlane's tasks don't yet
  reflect → suggest updating or creating the affected task(s) so Rocketlane's task list still maps
  to what's actually being delivered.
- **The project's Rocketlane Status Log is due for a refresh** (published as a native status-update
  entry via `rocketlane_publish_status_update` — see "Weekly Status Log Check" above) → suggest a
  new note in the `STATUS-LOG-RULES.md` format. Two independent tracks, neither gated on "a commit
  happened":
  - **Cadence-based (the norm)** — the "Weekly Status Log Check" routine, default every Monday. Due
    immediately if "Status Log last actually updated" still reads "Never yet," otherwise once 7 or
    more days have passed since that date.
  - **Event-triggered (the exception)** — checked by every Recurring Health Check Automation run,
    but **only** for a significant client-mood change, a significant delivery delay, or a major
    blocker/unblocker. Everything else waits for the weekly draft. When in doubt, don't draft.

  Once suggested by either track, it stays a live, open item — re-surfaced in full at the top of
  every subsequent run of *either* routine — until the SA actually responds in chat (approve, edit,
  or discard). See `CHECKLIST.md`'s Project Health Check section for the tracked dates.

**Task-level tracking works the same way, through a dedicated ledger.** Every VTEX SA action item
and client/SI commitment worth tracking — not just the milestone/risk/amendment-level triggers
above — belongs in
`Internal Documents/Project Management/Governance/ACTION-TRACKER.md`, mirrored against Rocketlane
on a recurring cadence per
`Internal Documents/Project Management/Governance/ROCKETLANE-RECONCILIATION-RULES.md` (join key,
sync direction, default ownership — the Project Lead SA unless the source names someone else,
approval boundaries). Both files ship filled in by default, the same as
`CLIENT-COMMUNICATION-PLAYBOOK.md` — read the rules file before identifying a new action item as a
Rocketlane creation candidate or reconciling the ledger against live Rocketlane state. A
newly-identified creation candidate is written straight into `ACTION-TRACKER.md`'s Section C — no
chat approval needed for that ledger write, only for the eventual Rocketlane `create_task` call —
see `ROCKETLANE-RECONCILIATION-RULES.md` §16 for the exact mechanism.

**Never cite a bare `CHECKLIST.md` ID (e.g. "RISK-029") in anything Rocketlane-facing** — a task
description, comment, or status update — without a short, self-contained explanation of what it
actually is. The ID means nothing to someone reading only Rocketlane, which has no access to this
repo's `CHECKLIST.md`; even an "unchanged since last time" item needs its one-line substance
restated, not just its ID and a status delta. Applies to risks, tasks, and milestones alike.

**Always suggest, never silently write** — same caution as the "GitHub Repository" custom-field
write in the Setup Validation Checklist above: Rocketlane is a shared, live system other people
and automations depend on, not a mirror to keep updated unattended. State what changed here, what
Rocketlane action it implies, and wait for the SA to confirm before calling a Rocketlane write
tool (`create_task`, `update_task`, `create_phase`, `update_phase`, `update_project`, etc.).
**Surface the suggestion directly in the chat/session — not only inside a PR description, a file,
or another document — so the SA sees it and can respond without having to go check the
repository.** This applies whether the suggestion comes from a live interactive session or an
unattended automated run (see "Recurring Health Check Automation" above for the latter). If the
SA confirms, make the write, then note in the same `JOURNAL.md` entry that documents the repo-side
change that the matching Rocketlane update was made (or explicitly wasn't, and why).

## Hard rules

1. **Follow `STRUCTURE.md`'s naming conventions exactly** (`ADR-NNN-<slug>.md`,
   `DRAFT-ADR-<slug>.md`, `TOPIC-NNN-<slug>.md`, etc.) — don't improvise variants.
2. **`JOURNAL.md` is append-only, newest entry first.** Never edit or delete a past entry, even to
   fix a stale detail — add a new entry that corrects or supersedes it, and say plainly that it's a
   correction.
3. **Never write a real person's name, email, or other identifying detail into an example, sample,
   or illustrative section** — anonymize (`the SA`, `<client>`, `Acme Corp`) even in "here's what
   good looks like" material. Real names in this project's own operational docs (stakeholder
   lists, meeting notes, `PROJECT.md`) are the one exception — this is private project data, not a
   shared public artifact.
4. **More specialized skills (`vtex-meeting-decision-capture`, `doc-audit`, `vtex-adr-writer`,
   `vtex-behavior-note`, and others) live in
   [`vtexprojects/vtex-sa-toolkit`](https://github.com/vtexprojects/vtex-sa-toolkit)**, not here.
   If one of those needs fixing, that's a PR against that repo. The day-to-day operations this file
   describes (initialize, setup validation, health checks, checklist/journal maintenance) are
   self-contained in this template on purpose — don't fetch the toolkit repo just to do those.
5. **This repo's `PROJECT.md` header carries the Rocketlane Project ID, and this repo's slug is
   written into that Rocketlane project's "GitHub Repository" custom field** (not a native
   `externalReferenceId` field — there isn't one). Keep both in sync if this repo ever moves. See
   the Setup Validation Checklist above — verify this rather than assuming it's already correct.
6. **When updating `CHECKLIST.md` or `PROJECT.md`, make surgical edits** — don't rewrite a whole
   file when only one section or row changed.
7. **`Contract/` is binding; `Sales Phase/` never is.** `Contract/Signed Agreement/` (summarized in
   `PROJECT.md`'s Contract Terms block) defines the scope/budget/deliverables the engagement is
   legally bound to — it changes only via a new signed entry in `Contract/Amendments/`, never by
   editing `PROJECT.md`'s Contract Terms table to match Rocketlane or reality. `Sales Phase/` is
   the opposite: historical record of what was originally pitched, with zero authority once
   delivery starts — never answer a "what's contracted" or "what's the current architecture"
   question from it. If a real decision or risk would exceed what `Contract/` allows, surface it as
   a Contract Amendment candidate rather than silently absorbing it. See `STRUCTURE.md`'s top
   callout for the full three-way model (Sales Phase / Contract / project phase).
8. **A real change filed in this repo (milestone, risk, amendment, phase/status change) should
   prompt a suggested Rocketlane update** — task create/update or phase change — not a silent one.
   See "Keeping Rocketlane aligned with what gets filed here" above for the specific triggers and
   why this is a suggestion, not an automatic write.
9. **Before filing a transcribed, summarized, or otherwise AI-derived document, check it actually
   carries usable content — don't file it just because the transcription itself succeeded.** A
   real incident: a Q&A transcription had every metadata column (Date, Supplier, RFP chapter) come
   back empty (`—`), with only four thin rows of actual Q&A, and got filed and cross-referenced
   from `PROJECT.md`/`CHECKLIST.md` anyway — pure noise, later found and deleted by the SA.
   Concretely, before saving:
   - If a table's key columns are mostly blank/`—`/"not captured", ask whether the document is
     worth keeping at all — accurately transcribing an empty source doesn't make the result useful.
   - Prefer flagging a source as "found but too thin to be worth filing" over filing a near-empty
     transcription and noting the gap inside it.
   - If genuinely unsure whether something clears the bar, ask the SA rather than filing silently
     — cheaper to ask once than to leave junk for someone to find and clean up later.
   - This applies to any derived document, not just Q&A transcriptions — meeting-note summaries,
     revenue-data transcriptions, and similar all carry the same risk.
10. **Keep the architecture snapshot current — but only when asked.** `vtex-projects-manage` (and
    any AI session in this repo) may be asked to generate or refresh
    `Internal Documents/Architecture/architecture-snapshot.md`: a single Mermaid diagram of the
    architecture as currently understood, plus a bulleted "Open points" list pulled from
    `PROJECT.md`'s open risks/discrepancies and any ADR marked not-yet-decided. It's a **static
    snapshot, not a live view** — regenerate it only when the SA asks, never automatically on
    every session. The one exception: **if the file's own "Last generated" date is a week or more
    old, proactively ask the SA whether they want it refreshed** before relying on it for anything
    important (same staleness-check spirit as the Project Health Check) — don't just silently use
    a stale diagram as if it were current. If the snapshot already carries `✅ Reviewed by <name>`
    (Hard Rule 12) and you regenerate it with real content changes, follow that rule's "Changes
    since last review" convention rather than silently leaving the stale `✅` on the new content.
11. **Before drafting any client-facing communication (email, Slack/Teams message, status update,
    meeting follow-up), read
    `Internal Documents/Project Management/Governance/CLIENT-COMMUNICATION-PLAYBOOK.md` first and
    follow it** — it covers what internal-only language never goes external (risk IDs, raw health
    colors, unsigned amendments, `Sales Phase/` content) and the expected structure per
    communication type. It ships filled in by default; don't restate its content here — if it ever
    needs to change, edit that file, not this one. Drafting is fine to do unprompted; actually
    sending stays subject to the standing rule that sending any message needs the SA's explicit
    go-ahead.
12. **ADRs and Behavior Notes move through two physical folder stages — `Drafts/` → `Accepted/` —
    under their respective `Internal Documents/Architecture/ADRs/` and `.../Behavior Notes/`
    folders (see `STRUCTURE.md`'s "Document stages"). Neither type has a physical `Reviewed/`
    stage — the folder a document sits in is the SA's final-promotion signal only; an
    SA-formed-but-not-yet-committed view is instead recorded on that document's own
    `reviewed_by`/`reviewed_date` fields while it's still in `Drafts/`, a status, not a folder
    move:**
    - `Drafts/` — freshly captured (`DRAFT-ADR-<slug>.md` / `DRAFT-BN-<slug>.md`). Nothing has
      looked at it yet — `reviewed_by`/`reviewed_date` are blank. Once the SA has read it and
      formed a view, but it isn't yet the team's committed position, fill in those two fields;
      **only the SA sets them**. The document stays here, still named `DRAFT-...`, until promoted.
    - `Accepted/` — the SA has confirmed this is the real, current position. Promotion means
      renaming `DRAFT-ADR-<slug>.md` → `ADR-NNN-<slug>.md` (or the Behavior Note equivalent) and
      moving it here. **Only the SA promotes a document into `Accepted/`** — an AI session may
      draft one, set/reset its `reviewed_by`/`reviewed_date` fields, or move one back to pending
      with a note explaining why, but never promotes one forward itself, no matter how confident
      it is the content is solid.

    **Meeting notes (`meetings/`) sit outside this review model entirely.** They're reference
    material (a record of what was said, not a decision), so they carry no review field and never
    need SA review. The SA reviews only what a meeting *produces*: ADR and Behavior Note drafts (by
    folder stage), Topic Analysis docs, and `architecture-snapshot.md`. In `CHECKLIST.md`'s Meeting
    Decision Capture Log, a meeting that produced no draft gets `— n/a (notes only)` in its
    `Reviewed?` column, never `⚠️ Not reviewed`, so the log doesn't imply SA work that doesn't
    exist. Hard Rule 9's content check still applies before filing a note.

    Topic Analysis docs and `architecture-snapshot.md` skip these stages entirely — they're always
    written directly as final documents, never as drafts. Since they never sit in `Drafts/`, they
    instead carry their own explicit **`Reviewed by SA`** field, right after their title: defaults
    to `⏳ Pending SA review`; **only the SA sets it** to `✅ Reviewed by <name>,
    <date>`. Never set this yourself, even for a document that looks solid — it's a claim about who
    actually read it, not about how old or trusted it seems. This is the same field-not-folder
    pattern ADRs/Behavior Notes now use for their own in-`Drafts/` `reviewed_by`/`reviewed_date`
    fields.

    **Separately — a different, independent axis from the review stage/fields above** — every
    document in `Accepted/`, every Topic Analysis doc, and `architecture-snapshot.md` carries two
    more fields,
    right after its title, tracking whether its content belongs in VTEX's Atlas knowledge base (a
    shared platform database serving all of VTEX and partners) as opposed to just being this
    project's own documentation:
    - **`Atlas candidate`** — defaults to `— Not yet assessed`. An AI session (or the SA) may set
      this to `🚫 Not Atlas-worthy` after checking it against `STRUCTURE.md`'s Atlas-readiness
      filter and finding it doesn't clear the bar (not client-generalizable, or the Atlas KB
      already covers the same fact), or to `🤖 Suggested by AI, <date> — <one-line
      reason>` when it looks genuinely platform-general. Either way, this is only ever a
      suggestion/assessment, never an approval.
    - **`Atlas approved`** — defaults to `— Not yet`. **Only the SA sets this**, to `✅ Approved by
      <name>, <date>` — regardless of whether `Atlas candidate` was already suggested or the SA is
      approving on their own initiative. Never set this yourself, no matter how confident you are.

    Both `Atlas candidate` and `Atlas approved` are future integration points (an eventual sync
    into Atlas will read `Atlas approved`) — nothing consumes them yet, but keep them accurate
    regardless, the same as any other field in this repo.

    **A `✅` on any of these fields is a claim about content the SA has actually seen — it doesn't
    survive a later substantive edit.** If you edit a document that already carries `✅ Reviewed by
    <name>` or `✅ Approved by <name>` (not a typo/formatting fix — an actual content
    change), add a dated bullet describing exactly what changed under a `## Changes since last
    review` section (create it, right after the field block, if it doesn't exist yet), and reset
    the affected field back to its pending state (`⏳ Pending SA review` / `— Not yet`). This
    applies to an Accepted ADR/Behavior Note too, even though its review signal is folder location
    rather than a field — if you substantively edit one, add the same "Changes since last review"
    section and say so directly to the SA, since there's no field to flip back to pending for those.
    The point is that the SA can jump straight to what's new instead of re-reading the whole
    document — never leave a stale `✅` sitting next to content they haven't actually seen.
13. **A Topic Analysis doc never becomes an ADR — they're separate, permanent documents.** Topic
    Analysis (`TOPIC-NNN`) is the exploration itself (options, tradeoffs, open questions) and stays
    in place as the historical record even after the question it raises gets resolved. Once a real
    decision is reached, file a **new, separate** ADR (through the normal `Drafts/` → `Accepted/`
    pipeline) that cross-references the Topic Analysis it grew out of, and add a short note to the Topic Analysis doc itself — e.g.
    `**Resolved — see ADR-NNN**` right after its title — so a reader lands on the decision, not a
    dead end. **Never rename, move, or convert the Topic Analysis file into the ADR** — both stay in
    place side by side, each doing a different job (exploration vs. decision).
14. **This git repo is the source of truth for how project documents are organized — the Google
    Drive project folder (`PROJECT.md`'s Quick Facts — `Google Drive project folder`) is storage,
    not a second source of truth.** Don't assume it already mirrors this repo's structure for a
    document type nothing has been filed for yet — check, or ask the SA, before inventing a new
    path in Drive. **Do not assume the Drive folder itself is shared with the client or SI** —
    confirm this per engagement rather than defaulting either way; on at least one engagement it
    turned out nobody outside VTEX had browsing access to it, and what actually reached the
    client/SI was individual files sent through a separate channel (email, Slack, or the SI's own
    systems), not the client opening the Drive folder directly. If that's also true here, uploading
    to Drive is about keeping VTEX's own internal record consistent and discoverable for anyone
    else at VTEX working the account — treat it as the client-facing delivery step only if the SA
    confirms the folder is actually shared.

    Use it for two things: (a) a document ready to be shared with the client or SI, or an internal
    architecture artifact that just reached a stable/approved state — this repo's copy alone
    doesn't reach anyone outside it, so upload a copy to Drive too, as the actual deliverable
    format (`.docx`/`.pdf`/etc. — not necessarily a live-editable Doc/Sheet unless that's genuinely
    what's being delivered); and (b) a document received from the client or SI worth storing there
    for the team. File either case respecting whatever folder structure the Drive folder already
    has — reuse a matching existing folder, or create a new one that fits how it's currently
    organized, rather than assuming a `Shared/`-equivalent exists there. If that structure is
    genuinely unclear (an ambiguous mix of received and sent documents, no obvious place to file
    into), **ask the SA where it should go rather than guessing**, and note it as a standing gap in
    `PROJECT.md` so it isn't re-asked every time. Use the Drive connector if connected this
    session.

    Upload/file in each of these cases, once the Drive folder's own matching subfolder is
    confirmed to exist (create it, following the folder's existing structure, if it doesn't):
    - A document copied into `Shared/With {{CLIENT_SHORT_NAME}}/` or `Shared/With
      {{SI_SHORT_NAME}}/` → the Drive folder's own matching `Shared/...` subfolder.
    - An ADR or Behavior Note the moment it's promoted into `Accepted/` (see `STRUCTURE.md`'s
      "Document stages") → the Drive folder's mirrored
      `Internal Documents/Architecture/ADRs/Accepted/` / `Behavior Notes/Accepted/`.
    - An architecture diagram filed under `Internal Documents/Architecture/Diagrams/`
      (`DIAG-NNN-<slug>-v<version>.pdf`).
    - Any other finalized architecture/design document — a Topic Analysis doc, Solution Design
      output, or a freshly regenerated `architecture-snapshot.md` (Hard Rule 10).
    - A document received from the client or SI worth keeping for the team — file it to fit
      whatever structure the Drive folder already has for received documents; if that's unclear,
      ask the SA rather than guessing, and note it as a standing gap in `PROJECT.md` so it isn't
      re-asked every time.

    **Confirm with the SA before the actual upload, in every case above** — Drive is a shared
    system other people (and possibly automations) depend on, not a scratch space to write to
    unattended. If the folder does turn out to be client/SI-visible on this engagement, this is a
    client-visible action and the same standing rule Hard Rule 11 already applies to actually
    sending a message; if it's VTEX-internal only, it's still not a silent write — just a lighter
    bar than Hard Rule 11's.

15. **Consolidate before you write: check for duplicates and knock-on effects before creating
    or updating any record.** This is the write-time half of the Health Check's "Register
    consolidation check". That check is the periodic sweep, and this rule stops the drift from
    being created in the first place. Before adding a record to any register, or changing a
    record's status, severity, or owner, search every register for the same point. Registers
    include a risk, a topic, an ADR or Behavior Note draft, an `ACTION-TRACKER.md` row or Section C
    candidate, a milestone, a customer need, a decision-log entry, and a filed meeting note. This
    applies to interactive sessions and to every automation alike.
    - **Already tracked?** If an existing record covers the same point, update that record
      instead of creating a second one. A new fact about an open risk is a dated note on that risk,
      not a new risk. A candidate task that already exists in the PM tool or the ledger is a
      mirror-back, not a new candidate.
    - **Does it resolve or supersede something older?** If the new information answers, closes,
      supersedes, or contradicts another record, update that record in the same change. Close it,
      mark it partially resolved, or add a cross-reference, and cite the source. Examples: a
      decision that answers a topic's question, a confirmation that removes a risk's premise, or a
      completed task behind a still-open ledger row.
    - **Does it break a reference?** If the change renames, promotes, retires, or deletes
      something, such as a draft ADR promoted to a numbered ADR, a PM-tool task deleted, or a
      document versioned, fix the cross-references and register rows that point to it in the same
      change.
    - **Is it missing from its register?** Every new document gets its register row in the same
      change, and every new PM-tool task gets its ledger row.
    - **Say what the check found**, in the commit message, PR description, or run output, e.g.
      "Consolidation: added a note to the existing risk instead of a new row; closed the topic it
      resolves", or "Consolidation: no related records". Closing or merging a record someone else
      opened still follows the usual discipline: propose it in the PR, and treat PM-tool writes as
      suggestions to the SA.
