# vtex-client-project-template

Template repo for a new VTEX Professional Services client engagement. One repo per client — the
SA creates it manually by clicking **"Use this template"** above, naming it after the client
alone (no Rocketlane Project ID in the name; a client can have more than one contract over time).

## What's in this repo, right now

The full folder tree, naming conventions, and core project files are **already here** — filled
with `{{DOUBLE_BRACE_PLACEHOLDERS}}`, ready to be replaced with a real client's values rather than
generated later by a separate skill. Nothing needs to be scaffolded; a freshly-created repo from
this template already has everything an AI session needs to start working in it.

- **`CLAUDE.md`** — the operating rules for any AI working in a client repo: the Setup Validation
  Checklist (run first, every session, not just on day zero), the Initialize workflow for a
  brand-new repo, the recurring Project Health Check automation, and the hard rules (naming
  conventions, `JOURNAL.md` append-only, anonymization, keeping the Rocketlane link in sync).
  Identical across every client repo — this is the one file that should never diverge.
- **`STRUCTURE.md`** — the canonical folder tree and, above it, the authority model that actually
  matters more than the folders themselves: **`Sales Phase/`** (the original RFP/pitch — frozen,
  zero authority once signed), **`Contract/`** (the signed agreement — binding, constrains
  everything else, changes only via a dated entry in `Contract/Amendments/`), and **everything
  else** (the living project-phase work — ADRs, specs, integration detail — where real decisions
  get made, as long as they fit inside what `Contract/` allows). `meetings/` sits at the root,
  outside all three, because the Read AI → AWS Lambda pipeline that files meeting notes always
  writes there regardless of phase or topic — that path must never be renamed.
- **`PROJECT.md`** — the living project definition: stakeholders, brands in scope, the Rocketlane
  Project ID(s), and a **Contract Terms** block that summarizes what `Contract/Signed Agreement/`
  actually says (hours, term, scope) so it doesn't have to be re-read for every question.
- **`CHECKLIST.md`** — the master tracking sheet: project inputs/outputs (Section A/B), open risks
  (D), milestones (E), meeting decisions (F), what's filed under `meetings/` and `Customer Needs/`
  (G/H, the latter cross-checked against VTEX's own roadmap), a roadmap watch-list not yet tied to
  a filed need (I), and the Project Health Check itself.
- **`JOURNAL.md`** — append-only, newest entry first, narrative memory: "catch me up on this
  project in 30 seconds." Never edited or backdated — a stale or wrong entry gets corrected by a
  new entry on top of it, not by rewriting the old one.
- **`.preview/`** — a local, read-only viewer for the five files above (plus `README.md`), with a
  sidebar and rendered Markdown/tables, so a quick look doesn't mean reading raw `.md` in a plain
  text editor. Flags any file that still has unfilled `{{PLACEHOLDERS}}`. Also has a tabbed
  Dashboard (Overview / Risks & Milestones / Documents / Tasks) pulled live from `PROJECT.md`,
  `CHECKLIST.md` §D/E, and `ACTION-TRACKER.md` — a quick status view without opening any one file
  directly. Run it from Claude Code with "preview this repo" (it reads `.claude/launch.json`), or
  manually: `python3 -m http.server 4321` from the repo root, then open
  `http://localhost:4321/.preview/index.html`.

**First thing to do in a freshly-created repo from this template:** clone it, then ask Claude Code
to set it up. `CLAUDE.md`'s Initialize workflow fills in the `{{PLACEHOLDERS}}` across the four
core files, confirms and links the Rocketlane project, and sets up the recurring Project Health
Check. The Setup Validation Checklist at the top of `CLAUDE.md` is what any AI session should run
first from then on — not just on day zero — to confirm the Rocketlane link is actually correct
rather than assumed.

## Why the structure looks like this

The folder tree isn't arbitrary — two pieces of it come directly from running this exact structure
on live engagements, not from guessing up front:

- **`Sales Phase/`, `Contract/`, and project-phase content are kept strictly apart** because
  mixing them caused a real problem: a table meant to reflect the signed contract had drifted to
  match Rocketlane instead, silently absorbing scope changes no one had actually signed off on.
  The fix isn't just "use separate folders" — it's the authority model in `STRUCTURE.md` (above)
  that says which of the three a question should even be answered from.
- **`meetings/` lives at the repo root**, not nested under a phase folder, because the automated
  pipeline that files meeting notes (Read AI → AWS Lambda) always writes to that exact path — a
  deeper folder structure would silently break ingestion, not just look worse.

More specialized skills (`vtex-meeting-decision-capture`, `doc-audit`, `vtex-adr-writer`,
`vtex-behavior-note`) live in
[`vtexprojects/vtex-sa-toolkit`](https://github.com/vtexprojects/vtex-sa-toolkit) — genuinely
shared logic worth centralizing there instead of per-client. The day-to-day loop this template
covers on its own — fill in placeholders, validate setup, run health checks, maintain the
checklist/journal — doesn't need that repo fetched at all.

## Not yet built (documented as follow-up, not faked as working)

- Converting an approved internal ADR into a client-facing version
- An AI pass over decision docs suggesting what the SA should cover in discovery
- Flagging internal guides that could become public VTEX Help Center articles
