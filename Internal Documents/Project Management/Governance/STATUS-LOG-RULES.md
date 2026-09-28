# Project Status Log Format (Rocketlane Status Log)

**Ships filled in by default**, same model as `CLIENT-COMMUNICATION-PLAYBOOK.md` and
`ROCKETLANE-RECONCILIATION-RULES.md`. `CHECKLIST.md`'s Project Health Check section tracks *when* to
suggest a Status Log refresh (weekly cadence + a narrow set of event triggers). This document is the
*content format* for the note itself once a refresh is due. See `CLAUDE.md`'s "Weekly Status Log
Check", "Recurring Health Check Automation", and "Keeping Rocketlane aligned with what gets filed
here" for the trigger logic and the "suggest, never silently write" approval discipline this format
is drafted under.

**Destination:** a native Rocketlane status-update entry on this engagement's Rocketlane project
(`PROJECT.md`'s header), published via `rocketlane_publish_status_update` on the dedicated
Rocketlane Status Log connector
(https://claude.ai/directory/a688602a-1c33-430e-ac61-c400c3afbae4). Don't write the note into the
"Status Log Notes" custom field via `update_project`. That was the older practice, and the field is
not the destination for new entries. Publishing always requires the SA's explicit go-ahead in chat.
The tool previews before writing: call it once without `confirm`, then again with `confirm: true`
only after the SA approves. This document only governs what the drafted note should contain.

**Audience:** internal/SA use, not client-facing. If this format is ever reused for a client-facing
summary, adjust the language and detail level, and run it through `CLIENT-COMMUNICATION-PLAYBOOK.md`
first.

## 1. Header

- As-of date (the date this note reflects).
- Prepared by (the SA's name).

## 2. Client Mood

- One label only, matching the connector's `customer_mood` picklist exactly: **Very Satisfied** /
  **Satisfied** / **Neutral** / **Dissatisfied** / **Highly Dissatisfied**. (This is Rocketlane's
  "Status Log Customer Mood" field, `1928042` on VTEX's Rocketlane instance. Call
  `rocketlane_get_field(1928042)` first if the labels ever seem to have changed.)
- Below the label, the detail that actually supports it: concrete signals from the most recent
  client-facing interaction (who said/did what, what was left open or deferred). Clearly separate
  what's new since the last note from standing historical context.
- If there was no new client interaction in the window, say so explicitly rather than asserting a
  mood without evidence.

## 3. Project Status

- One label only, matching the connector's `overall_status` values exactly: **On Track** (1) /
  **Ahead of Time** (2) / **Running Late** (3) / **At Risk** (4). Expect "Ahead of Time" to be used
  rarely.
- No embellishment — the raw call.
- **Caveat confirmed in practice:** Rocketlane doesn't always carry a reliable native field for
  this. `inferredProgress` can come back empty, and `progressPercentage` is only the percentage of
  *tasks* closed — not weighted by hours or effort — so it can't justify the label on its own.
  Cross-check against the Project Health Check signals in `CHECKLIST.md` (budget vs. progress
  ratio, overdue-task count, go-live date) before picking a label.
- **Lead with the actual project timeline, never with hours-consumed-vs-budget percentages.** Phase
  due dates, the go-live date, and confirmed session/milestone dates are the real near-term signal.
  Hours burn is fine to mention in passing but must **never** be the primary basis for the rating.
  A hours-intensive stretch (heavy workshop cadence, front-loaded discovery) is expected and is not
  on its own a reason to downgrade the label. Confirmed on a live engagement after a draft used
  "hours consumed 85% vs. 53% progress" as the reason to mark a project Running Late.

## 4. Key Points & Decisions (since the last note)

- Only decisions that are closed/confirmed — not discussions still in progress.
- Each line states *what* was decided, not the process that got there.
- Exclude internal housekeeping (Rocketlane cleanup, timesheet policy, already-resolved bugs)
  unless the client explicitly asked about it.

## 5. Risks

- Only what's new or reinforced since the last note. Don't restate the full risk register.
- **Never cite a bare ID** (e.g. "RISK-012 (Medium) — unchanged"). The ID means nothing to someone
  reading only Rocketlane, which has no access to this repo's `CHECKLIST.md`. Every risk line must
  carry a short, self-contained explanation of what the risk actually is (one clause is enough —
  pull it from Section D), not just its status delta. Even an "unchanged" risk needs its one-line
  substance restated.

## 6. Next Steps

- Action + owner; concrete tasks with a date where one exists.
- Don't list overdue VTEX-side administrative tasks unless the client asked about them.

## 7. Formatting: write `notes` as HTML, not plain text

**Confirmed in practice:** Rocketlane's renderer collapses plain-text `\n` line breaks into a single
flat paragraph, so a note drafted as plain text reads as one wall of text once published. Always
build the `notes` string as HTML:

- One `<p><strong>Section:</strong> ...</p>` block per section (Client Mood, Project Status, Key
  Points & Decisions, Risks, Next Steps).
- Within a section, separate bullet lines with `<br>` — not `<ul>/<li>`. Prefix each bullet line
  with an em dash ("—") or, for Risks, the relevant severity marker, consistent with prior entries.
- Escape HTML-significant characters in any content pulled from elsewhere (e.g. `&` → `&amp;`).

## General rules

- **The no-bare-ID rule applies everywhere in the note, not just Risks.** A risk ID, task name,
  milestone ID, or ADR number is meaningless to a Rocketlane-only reader. Whenever Key Points &
  Decisions or Next Steps references a tracked item, say what it actually is in the same line.
- **Verify any metric before citing it.** Never assume a Rocketlane percentage means what it
  appears to mean (see the Project Status caveat above).
- **Cut anything that can't be backed by a real source** (meeting notes, Slack, email, Rocketlane)
  rather than inferring it to fill a section.
- **Never post to Rocketlane without the SA's explicit confirmation.** This document produces a
  draft; the actual write stays the SA's call. Call `rocketlane_publish_status_update` without
  `confirm` first (it previews), share that preview and the full draft note with the SA in chat,
  and only call it again with `confirm: true` after they approve.
