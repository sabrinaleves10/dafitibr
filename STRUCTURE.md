# {{PROJECT_NAME}} — Project Folder Structure

> **Version:** 1.12.0 | **Last updated:** {{DATE}}
>
> **Version 1.12.0** dropped the physical `Reviewed/` stage folder for both `ADRs/` and
> `Behavior Notes/` — an SA-formed-but-not-yet-committed view is now recorded on the document
> itself via `reviewed_by`/`reviewed_date` fields while it stays in `Drafts/`, a status rather than
> a folder move. `Drafts/` and `Accepted/` are now the only two physical stages for both types.
> This reopens a call PR #11 made deliberately (excluding the equivalent Behavior-Notes-only change
> as "not universal across engagements") — the SA who requested this pull-forward considers a
> status field the universal default going forward, not an engagement-specific preference, so both
> document types now follow it consistently rather than leaving one on folders and one on a field.
> Proven out on a live client engagement (`bestbuy-b2b-ca`) before being pulled back into the
> template — see the PR that introduced this version for the source engagement's own STRUCTURE.md
> if useful context.
>
> **Version 1.11.0** added a `Retired/` terminal stage under `ADRs/` and `Behavior Notes/` (a
> document that's superseded, deprecated, or merged into another one moves here instead of just
> staying in `Accepted/` looking current), and a Health color rubric for `PROJECT.md`'s
> `**Health:**` line (previously undocumented judgment call). Both patterns were proven out on a
> live client engagement before being pulled back into the template — see the PR that introduced
> this version for the source engagement's own STRUCTURE.md if useful context.
>
> **Purpose:** This file defines the canonical folder structure for the {{PROJECT_NAME}} VTEX
> implementation project. It is machine-readable (used by AI agents to locate and file documents)
> and human-readable (used by the team to stay organized). All new files and deliverables must be
> placed according to this structure.
>
> This structure ships pre-built with the `vtex-client-project-template` repo — it is not
> generated at initialize time. Replace `{{PLACEHOLDERS}}` below with this client's actual values;
> the folder tree itself should stay as-is unless this specific engagement genuinely needs a
> different shape (e.g. no brands, a different SI arrangement). If it does diverge, bump the
> Version line above and say what changed and why — so a later session (or another SA) can tell
> deliberate divergence from silent drift.
>
> **Sales phase, contract, and project phase are three separate things with three different kinds
> of authority — not just three separate folders.** Confusing what kind of authority a document
> carries is the actual risk here, not just filing it in the wrong place:
>
> - **`Sales Phase/`** — the original RFP/pitch process: initial scope, first architecture design,
>   both vendors' proposals. **No authority once signed.** It's context for how the engagement
>   started, not a source anyone should quote for what's true now. Frozen and read-only from
>   signature onward — nothing is ever added to it again, including for a later extension (that's
>   `Contract/Amendments/`) or a superseded design (that's a new ADR).
> - **`Contract/`** — the signed legal agreement: scope, budget/hours, deliverables, term. **This
>   is binding and constrains everything else.** It changes only through a new dated, signed entry
>   under `Contract/Amendments/` — never by editing a table elsewhere to match reality. If a
>   decision made during delivery would require going beyond what's in `Contract/` (more hours,
>   a brand/country not in scope, a deliverable not promised), that is a signal to raise a Contract
>   Amendment with the SA — not something to quietly absorb into `PROJECT.md` or an ADR.
> - **Everything else (project phase)** — the living work: ADRs, specs, integration detail. This is
>   where real engineering decisions get made and *can* diverge from what `Sales Phase/` originally
>   proposed (see `PROJECT.md` §5) — but those decisions still have to fit inside what `Contract/`
>   allows. Sales Phase content has no veto here; Contract terms do.
>
> Never file the original RFP, either vendor's proposal, or a financial offer anywhere outside
> `Sales Phase/`; never file a signed contract or amendment anywhere outside `Contract/` — even
> though `Internal Documents/Commercial/` sounds like it could fit either, that folder is strictly
> post-contract internal working versions, never an original offer or a signed document.

---

## Root: `{{ROOT_FOLDER_NAME}}/`

```
{{ROOT_FOLDER_NAME}}/
│
├── STRUCTURE.md                    ← This file. Folder structure rules.
├── PROJECT.md                      ← Project definition, context, and key decisions.
├── CHECKLIST.md                    ← Master checklist tracking all project inputs/outputs and status.
├── JOURNAL.md                      ← Narrative memory-in-progress.
│
├── meetings/                       ← ALL meeting notes and transcripts, any phase (sales or PS),
│   │                                  any source (Read AI, Google Meet/Gemini auto-notes, manual
│   │                                  notes). Kept together at the root so nothing gets buried
│   │                                  inside phase-specific folders. Name format:
│   │                                  YYYY-MM-DD-<topic>.md (add a suffix like -am/-pm if more
│   │                                  than one meeting shares a date/topic).
│   │
├── Sales Phase/                    ← The original RFP/pitch process only — nothing else. Frozen
│   │                                  and read-only once signature happens; never add a file here
│   │                                  after that point, including for a later extension or scope
│   │                                  change (that's Contract/Amendments/ below instead).
│   │                                  **The architecture/solution content in here is a frozen
│   │                                  snapshot of what was proposed — never what's currently true.**
│   │                                  Once delivery starts, PROJECT.md §5 (kept current, backed by
│   │                                  ADRs) is the living architecture source of truth. If they
│   │                                  disagree, PROJECT.md/the ADR wins — that's expected, not an
│   │                                  error, and is exactly why the two are kept apart.
│   ├── RFP/                        ← The client's original RFP, plus supporting Q&A and
│   │   │                              commercial/revenue data gathered during the RFP process
│   │   └── Q&A/
│   ├── VTEX Proposal/              ← VTEX-authored: architecture diagram, solution design deck
│   ├── Agency Proposal/            ← SI ({{SI_SHORT_NAME}})-authored: execution approach, rollout/RACI plan
│   └── Financial Offers/           ← The original pricing/financial offer(s) from the RFP process.
│                                      A later re-priced offer for an extension/amendment goes in
│                                      Contract/Amendments/ instead — see below.
│
├── Contract/                       ← The legal agreement itself, across its whole lifecycle — kept
│   │                                  separate from Sales Phase because a contract isn't a sales
│   │                                  artifact: it persists and can be amended throughout the
│   │                                  engagement, long after the sales round that produced it is
│   │                                  closed. Internal Documents/Commercial/ below is for
│   │                                  post-contract internal working versions only, never the
│   │                                  original signed document.
│   ├── Signed Agreement/           ← Order Form, MSA, DPA — the original executed contract
│   └── Amendments/                 ← Each later amendment, extension, or change order as its own
│                                      dated entry (re-priced offer + the signed amendment together)
│
├── Customer Needs/                 ← Internal process gaps — requirements not covered natively by VTEX.
│   │                                  Use for gap analysis, feature requests, workaround proposals.
│   ├── Gap Analysis/               ← Documented gaps per functional area
│   └── Feature Requests/           ← Platform feature requests raised during the project
│
├── Documents Shared by Customer/   ← Documents the client shares DURING the live PS engagement
│   │                                  (post-kickoff) — not sales-phase material; see Sales Phase/
│   │                                  above for anything from before contract signature.
│   │                                  Do not modify originals; add notes as separate files.
│   ├── Architecture/               ← Client-provided architecture inputs (live engagement)
│   └── Legal & Compliance/         ← Other legal/compliance docs the client shares during delivery
│                                      (e.g. a security policy, a compliance certificate) — not the
│                                      contract itself or an amendment; those go in Contract/.
│
├── Documents Shared by SI/         ← Documents the System Integrator ({{SI_SHORT_NAME}}) shares DURING
│   │                                  the live PS engagement — the SI-authored counterpart to
│   │                                  Documents Shared by Customer/. Not sales-phase material (see
│   │                                  Sales Phase/Agency Proposal/ for that).
│   │                                  Do not modify originals; add notes as separate files.
│   └── Architecture/               ← SI-provided architecture inputs (live engagement)
│
├── Functional Specifications/      ← Functional specs produced during analysis & design.
│   │                                  One subfolder per brand or cross-brand capability.
│   ├── Cross-Brand/                ← Specs applying to all brands (checkout, OMS, search, etc.)
{{BRAND_SUBFOLDERS}}│
├── Internal Documents/             ← Project-internal working documents (not for client sharing).
│   ├── Architecture/               ← ADRs, diagrams, topic analysis, behavior notes
│   │   ├── architecture-snapshot.md ← One AI-generated file: a Mermaid diagram of the architecture
│   │   │                              as currently understood, plus an "Open points" list. Static
│   │   │                              snapshot, regenerated only on request — see CLAUDE.md Hard
│   │   │                              Rule 10. Distinct from Diagrams/ below (uploaded, versioned
│   │   │                              deliverables) — this is a lightweight, always-out-of-date-
│   │   │                              until-refreshed companion to PROJECT.md, not the official
│   │   │                              architecture diagram.
│   │   ├── ADRs/                   ← Architecture Decision Records. Stage subfolders below — see
│   │   │                              "Document stages" further down; no loose files directly in
│   │   │                              this folder any more. **No `Reviewed/` subfolder** — the
│   │   │                              "SA has read it and formed a view, not yet committed" signal
│   │   │                              is a status on the document itself, not a folder.
│   │   │   ├── Drafts/             ← Stage 1. Freshly captured (DRAFT-ADR-<slug>.md), unreviewed.
│   │   │   │                          Carries `reviewed_by`/`reviewed_date` fields (blank until
│   │   │   │                          the SA has read it and formed a view — still not the team's
│   │   │   │                          committed position; that's what promotion means).
│   │   │   ├── Accepted/           ← Stage 2. SA confirmed as the team's real, current position.
│   │   │   │                          This is where promotion happens: renamed from
│   │   │   │                          DRAFT-ADR-<slug>.md to ADR-NNN-<slug>.md. Carries the
│   │   │   │                          Atlas candidate/approved fields (CLAUDE.md Hard Rule 12).
│   │   │   └── Retired/            ← Terminal stage, not part of the forward progression. A
│   │   │                              document superseded, deprecated, or merged into another one
│   │   │                              moves here from whichever stage it was last in — see
│   │   │                              "Document stages" further down.
│   │   ├── Diagrams/               ← Architecture diagrams (DIAG-NNN-<slug>-v<version>.pdf)
│   │   ├── Topic Analysis/         ← Deep-dives per architecture topic (TOPIC-NNN-<slug>.md) —
│   │   │                              no stage subfolders; always written as final documents.
│   │   └── Behavior Notes/         ← VTEX platform behavior notes. Same two-stage-subfolder model
│   │       │                          as ADRs/ above — no loose files directly in this folder.
│   │       ├── Drafts/             ← Stage 1. Freshly captured (DRAFT-BN-<slug>.md), unreviewed.
│   │       │                          Same `reviewed_by`/`reviewed_date` field pair as ADRs above.
│   │       ├── Accepted/           ← Stage 2. Promoted: renamed DRAFT-BN-<slug>.md →
│   │       │                          BN-NNN-<slug>.md. Carries the Atlas candidate/approved
│   │       │                          fields (CLAUDE.md Hard Rule 12).
│   │       └── Retired/            ← Terminal stage — see the same subfolder under ADRs/ above and
│   │                                  "Document stages" further down.
│   ├── Project Management/         ← RACI, timeline, team roster for the live PS engagement
│   │   │                              (meeting notes live in meetings/ at the root, not here)
│   │   ├── RACI/
│   │   ├── Timeline/
│   │   ├── Team Roster/
│   │   └── Governance/             ← Non-meeting governance/process docs.
│   │       ├── CLIENT-COMMUNICATION-PLAYBOOK.md ← Ships filled in by default (not create-if-
│   │       │                                       needed) — see the file itself for content,
│   │       │                                       not restated here.
│   │       ├── ACTION-TRACKER.md               ← Ships filled in by default. Single running
│   │       │                                       ledger of VTEX SA action items and client/SI
│   │       │                                       commitments, mirrored against Rocketlane on a
│   │       │                                       recurring cadence — see
│   │       │                                       ROCKETLANE-RECONCILIATION-RULES.md.
│   │       ├── ROCKETLANE-RECONCILIATION-RULES.md ← Ships filled in by default, same model as the
│   │       │                                       playbook above. Standing rules for how
│   │       │                                       ACTION-TRACKER.md stays in sync with
│   │       │                                       Rocketlane: join key, sync direction, default
│   │       │                                       task ownership, approval boundaries.
│   │       ├── STATUS-LOG-RULES.md             ← Ships filled in by default. Content format for
│   │       │                                       the Rocketlane Status Log note (weekly by
│   │       │                                       default) — see CLAUDE.md's "Weekly Status
│   │       │                                       Log Check".
│   │       └── (escalation policy, etc.)       ← Other governance docs, created only if this
│   │                                              engagement produces one. Meeting notes go in
│   │                                              meetings/ regardless of topic either way.
│   ├── Commercial/                 ← Financial models, offer working docs — post-contract, internal
│   │                                  versions only. The original offer lives in
│   │                                  Sales Phase/Financial Offers/; the signed agreement itself
│   │                                  (and any amendment) lives in Contract/ — never here.
│   └── Solution Design/            ← Live Discovery/Analysis & Design output: rollout strategy,
│       │                              cutover plans. This is NOT the sales-phase VTEX proposal
│       │                              deck — that lives in Sales Phase/VTEX Proposal/.
│       └── Integration Specs/      ← Per-system integration specifications (see CHECKLIST.md B06)
│
├── Recordings/                     ← Meeting/workshop AUDIO/VIDEO files. (Transcripts and written
│   │                                  notes go in meetings/ at the root instead — this folder is
│   │                                  for the raw recording media itself.)
│   │                                  Name format: YYYY-MM-DD-<topic>.<ext>
│   ├── Workshops/
│   ├── Steering Committee/
│   └── Technical Sessions/
│
└── Shared/                         ← Documents ready to be or already shared with the agency or client.
    │                                  Only polished, approved documents go here.
    ├── With {{CLIENT_SHORT_NAME}}/  ← Shared with the client
    │   ├── Architecture/
    │   ├── Proposals/
    │   └── Reports/
    └── With {{SI_SHORT_NAME}}/      ← Shared with the SI
        ├── Architecture/
        ├── Integration Specs/
        └── Decisions/
```

---

## Naming Conventions

| Type | Convention | Example |
|------|-----------|---------|
| ADRs | `ADR-NNN-<slug>.md` | `ADR-001-search-provider.md` |
| Behavior Notes | `BN-NNN-<slug>.md` | `BN-001-oauth2-client-credentials.md` |
| Architecture diagrams | `DIAG-NNN-<slug>-v<version>.pdf` | `DIAG-001-architecture-v0.0.1.pdf` |
| Topic analysis docs | `TOPIC-NNN-<slug>.md` | `TOPIC-001-ocos-franchise-accounts.md` |
| Meeting notes (in `meetings/`) | `YYYY-MM-DD-<topic>.md` | `2026-01-15-kickoff-notes.md` |
| Recordings (in `Recordings/`) | `YYYY-MM-DD-<topic>.<ext>` | `2026-01-15-kickoff.mp4` |
| VTEX deliverables | Keep `VTEX -- <description>` prefix | As-is from VTEX convention |
| Draft ADR candidate | `DRAFT-ADR-<slug>.md` | `DRAFT-ADR-search-provider.md` |
| Draft Behavior Note candidate | `DRAFT-BN-<slug>.md` | `DRAFT-BN-checkout-retry-limit.md` |
| Supplementary evidence for an ADR/BN | `SUPPLEMENT-<ADR-or-BN-id>-<slug>.md`, filed alongside the file it supports | `SUPPLEMENT-BN-005-walkthrough.md` |

---

## Document stages (ADRs / Behavior Notes)

ADRs and Behavior Notes each progress through real, physical subfolders — `Drafts/` → `Accepted/`,
plus a terminal `Retired/` — rather than sitting loose in a single flat folder: the stage a document
is in should be visible in the folder tree itself for the moves that matter (draft vs. the team's
committed position), not tracked only in a status field. Neither type has a physical `Reviewed/`
stage — an SA-formed-but-not-yet-committed view is instead recorded on the document's own
`reviewed_by`/`reviewed_date` fields while it's still in `Drafts/`: a status, not a folder move.
A `Drafts/` → `Accepted/` move is a real `git mv`, not a metadata update. Topic Analysis docs and
`architecture-snapshot.md` don't use these stages — they're always written directly as final
documents. Since they never sit in `Drafts/`, they carry their own `Reviewed by SA` field instead
(`⏳ Pending SA review` / `✅ Reviewed by <name>, <date>` — SA-only, same rule as everywhere else in
this file, and the same field-not-folder pattern ADRs/Behavior Notes now use for their own
in-`Drafts/` `reviewed_by`/`reviewed_date` fields).

1. **`Drafts/`** — freshly captured (typically by `vtex-meeting-decision-capture`), named
   `DRAFT-ADR-<slug>.md` / `DRAFT-BN-<slug>.md`. Not reviewed. Anyone, including an AI session, may
   still discard it outright if it turns out to be noise. Once the SA has read it and formed a view
   — but hasn't yet committed to it as the team's real, current position — set that document's own
   `reviewed_by`/`reviewed_date` fields (blank/`— Pending SA review` until then). This stays a
   metadata update, not a folder move: the document is still in `Drafts/`, still isn't final.
2. **`Accepted/`** — the SA confirms this is the team's real, current position. This is what
   triggers **promotion**: move the file into `Accepted/` and rename it, dropping the `DRAFT-`
   prefix (`DRAFT-ADR-<slug>.md` → `ADR-NNN-<slug>.md`, `DRAFT-BN-<slug>.md` → `BN-NNN-<slug>.md`).
   **Keep the existing number** if the document already carries one from an earlier migration or
   register entry — don't renumber against what's already in `Accepted/`, since that number is
   already the identifier used throughout `CHECKLIST.md`, `JOURNAL.md`, and cross-references
   elsewhere; only assign a genuinely new next-sequential number for a document that never had one.
   A companion evidence file (e.g. a migrated walkthrough) promotes alongside its ADR/BN into the
   same `Accepted/` folder, named `SUPPLEMENT-<id>-<slug>.md`. Promotion is always an explicit SA
   action — never automatic; an AI session may reset a document's `reviewed_by`/`reviewed_date`
   fields back to pending, or delete it, with a note on why, but never move it into `Accepted/`
   itself.
3. **`Retired/`** — a **terminal** stage, not part of the forward progression above: a document
   moves here from whichever stage it was last in, once it's been superseded by another document,
   formally deprecated, rejected on review, or merged into another document's content. Keep the
   filename it already had (don't rename or drop/add the `DRAFT-` prefix on this move — a document
   that was still in `Drafts/` when retired keeps looking like a draft, since it never reached
   promotion). Retiring is always an explicit SA action, same as promotion — never automatic. The
   retirement notice inside the file itself remains the authoritative explanation of *why*; the
   folder just makes that status visible without opening the file. Don't confuse this with a
   document that's merely *inactive while a related open question gets resolved elsewhere* (e.g. a
   Topic Analysis doc is never retired even after its question is answered by a later ADR, per
   Hard Rule 13) — only move a document here when its own content is superseded or no longer the
   live position, not when an adjacent, related question is still being worked.

Only once a document is in `Accepted/` (or is a Topic Analysis doc / `architecture-snapshot.md`)
does it carry the two Atlas fields from `CLAUDE.md` Hard Rule 12 — `Atlas candidate` and `Atlas
approved`. These track something separate and independent from the review stage above: whether the
document's content belongs in VTEX's Atlas knowledge base (a shared platform database serving all
of VTEX and partners), not whether it's a good record of this project. A document can be a fully
Accepted, reviewed record of a real project decision and still never be Atlas-relevant — most
won't be, since most ADRs/Behavior Notes describe this client's specific setup, not general VTEX
platform behavior.

**Atlas-readiness filter** — before setting `Atlas candidate` to suggested, check all of:

- **Already in `Accepted/`, not `Drafts/`** (regardless of that document's own `reviewed_by`
  field). A document that hasn't cleared review yet is never Atlas-ready by definition, no matter
  how solid it looks.
- **Generalizable, not client-specific.** States a VTEX platform behavior, limitation, or reusable
  pattern — not a decision specific to this client's business or setup (e.g. "we chose this
  shipping model for our catalog" is this client's own choice; "VTEX's Tax Hub applies tax to the
  shipping fee this way" is a platform fact anyone integrating could reuse).
- **Actually new.** Query `vtex-atlas-knowledge-search` (or `vtex-architect-mcp`'s
  `retrieve_context`, if connected) for the same fact first — if the Atlas KB already covers it,
  set `Atlas candidate` to `🚫 Not Atlas-worthy` instead of suggesting it, so the next pass doesn't
  re-check the same non-candidate.
- **Anonymizable.** No participant name or client-identifying detail is load-bearing to the
  content itself — a document that only makes sense with a specific person's name attached isn't
  ready as written.

Nothing currently consumes `Atlas candidate`/`Atlas approved` automatically (per CLAUDE.md Hard
Rule 12, these are a future integration point) — the filter above is guidance for whoever (human or
AI) reviews a newly-promoted document, not an automated gate.

A `✅ Reviewed by <name>` or an `Atlas approved` value of `✅ Approved by <name>` doesn't survive a later substantive edit to the same
document — see CLAUDE.md Hard Rule 12's "Changes since last review" convention: reset the field to
pending and add a dated bullet saying exactly what changed, so the SA can review just the delta
instead of the whole document again.

**A Topic Analysis doc never becomes an ADR** — see CLAUDE.md Hard Rule 13. It stays in place
permanently as the exploration/analysis record; once a decision is reached, a new ADR is filed
separately, cross-referencing it, with a `**Resolved — see ADR-NNN**` note added to the Topic
Analysis doc itself. Never rename or convert one into the other.

---

## Health color rubric (`PROJECT.md`'s `**Health:**` line)

Until this rubric existed, the 🟢/🟡/🟠/🔴 choice on `PROJECT.md`'s `**Health:**` line was a pure
judgment call with no documented rule, which let it drift out of sync with what `CHECKLIST.md`
Section D's risk register actually said. If this project's local preview Dashboard renders that
emoji, check whether it distinguishes all four colors or collapses some of them visually — the
emoji you pick in `PROJECT.md` may be the only place a finer distinction actually lives.

Base the color primarily on `CHECKLIST.md` §D's currently-**open** (`⏳ Open`) risks — not
`✅ Accepted`/`✅ Closed` ones — secondarily on the Project Health Check's schedule/budget signals
(go-live date consistency, budget-vs-progress ratio, profit margin trend, overdue tasks):

- **🟢 Green** — No open 🔴 High risk, and the last Project Health Check found no schedule/budget
  signal worth flagging.
- **🟡 Yellow** — At least one open 🔴 High risk, but every one of them has a documented mitigation
  path (an owner assigned and a concrete "Next:" action, or an ADR/decision already in motion) and
  none is noted as escalating.
- **🟠 Orange** — At least one open 🔴 High risk that is explicitly trending worse, has gone
  unresolved across multiple review cycles, or has no clear path to resolution yet — **or** a
  Health Check signal (date mismatch, budget outpacing progress, negative margin trend) that hasn't
  escalated to a hard blocker.
- **🔴 Red** — Any open risk that directly threatens the go-live date or blocks delivery with no
  fallback, or a Health Check signal severe enough to threaten the contract/timeline outright.

Re-evaluate this rubric — and update the emoji together with the risk-count text — every time
`CHECKLIST.md` §D's open-risk set changes (a High risk opens, closes, escalates, or de-escalates)
or a Project Health Check run finds a new schedule/budget signal. Don't let the color go stale
independently of the count.

---

## Folder Purpose Quick Reference

| Folder | Who puts things here | What goes here |
|--------|---------------------|----------------|
| `meetings/` | Anyone / any note-taking tool | Every meeting's notes or transcript, any phase, any source |
| `Sales Phase/` | (historical — the original RFP round only) | The client's RFP, both vendors' proposal responses, and the original financial offer. Frozen from signature onward; architecture/scope content here can be superseded by `PROJECT.md` §5 and ADRs. |
| `Contract/` | VTEX SA | The signed agreement (Order Form, MSA, DPA) and every later amendment/extension — spans the whole engagement, unlike `Sales Phase/` |
| `Customer Needs/` | VTEX SA, {{SI_SHORT_NAME}} | Gap analysis, unmet requirements, feature requests |
| `Documents Shared by Customer/` | VTEX SA | Anything received from the client during the live engagement (originals, unmodified) |
| `Documents Shared by SI/` | VTEX SA | Anything received from the System Integrator during the live engagement (originals, unmodified) |
| `Functional Specifications/` | {{SI_SHORT_NAME}}, VTEX SA | Signed-off functional specs per brand/capability |
| `Internal Documents/` | VTEX SA, {{SI_SHORT_NAME}} | ADRs, diagrams, PM docs, commercial working files, live solution design |
| `Internal Documents/Architecture/ADRs/Drafts/` | `vtex-meeting-decision-capture` or the Recurring Health Check (AI-drafted) | Unreviewed ADR candidates — see "Document stages" |
| `Internal Documents/Architecture/Behavior Notes/Drafts/` | `vtex-meeting-decision-capture` or the Recurring Health Check (AI-drafted) | Unreviewed Behavior Note candidates — see "Document stages" |
| `Recordings/` | Anyone | Meeting/workshop audio/video files (not transcripts) |
| `Shared/` | VTEX SA | Final, approved docs sent to client or SI |

---

## Agent Instructions

- **Meeting notes or transcripts, from any source (Read AI, Google Meet/Gemini, manual notes) and
  any phase** → always `meetings/` at the repo root, never nested under `Internal Documents/` or
  elsewhere. Name them `YYYY-MM-DD-<topic>.md`; add a suffix if more than one shares a date.
- `Sales Phase/` is a closed historical record from the moment of signature onward — never add a
  file there after that point, for any reason, including a later extension or scope change (that's
  `Contract/Amendments/` instead). New architecture/solution-design work for the live engagement
  goes under `Internal Documents/`.
- **A contract extension, scope change, or new SOW is a `Contract/Amendments/` entry, not a new
  `Sales Phase/` round.** File the re-priced offer and the signed amendment together under one
  dated entry there — it's a change to the legal agreement, which has its own ongoing lifecycle,
  not a repeat of the original sales/RFP process.
- **Never answer "what's the current architecture / account strategy / scope" from a document
  under `Sales Phase/`.** That folder only tells you what was originally proposed or sold. The
  current, living answer is `PROJECT.md` §5 (Architecture Summary) plus
  `Internal Documents/Architecture/ADRs/Accepted/` (the promoted ADRs — not `Drafts/`, whatever
  a draft's own `reviewed_by` field says) — check there first, and if a Sales Phase document
  disagrees with them, the ADR/PROJECT.md wins; don't flag that as an inconsistency to resolve, it
  reflects a real decision made during delivery.
- **Never answer "what's contracted / what are we bound to" from `Sales Phase/` or from Rocketlane
  either.** `Contract/Signed Agreement/` (summarized in `PROJECT.md`'s Contract Terms block) is the
  only binding answer — Rocketlane fields can drift from the actual signed terms (this has already
  happened in practice: a tracked-hours figure and a go-live date have both been caught disagreeing
  with the real contract). If a real decision or a risk in `CHECKLIST.md` would require exceeding
  what `Contract/` allows, say so explicitly and suggest a Contract Amendment — don't silently
  proceed as if it's already covered, and don't edit `PROJECT.md`'s Contract Terms block to match
  reality without an actual signed entry in `Contract/Amendments/` behind it.
- **Sales phase, contract, and project phase never mix.** The original RFP or either vendor's
  proposal always goes under `Sales Phase/`; the signed agreement or any amendment always goes
  under `Contract/` — even though `Internal Documents/Commercial/` sounds like it could also fit
  either, that folder is strictly post-contract internal working files, never an original offer or
  a signed document.
- Non-meeting governance/process docs → `Internal Documents/Project Management/Governance/`.
  `CLIENT-COMMUNICATION-PLAYBOOK.md` ships there by default in every repo — read it before drafting
  any client-facing communication (see CLAUDE.md). Meeting notes always stay in `meetings/`
  regardless of topic, including governance-related meetings.
- **Task-level action tracking also ships by default in that same folder** —
  `ACTION-TRACKER.md` (the ledger) and `ROCKETLANE-RECONCILIATION-RULES.md` (the sync rules that
  keep it aligned with Rocketlane: join key, sync direction, default ownership, approval
  boundaries). See CLAUDE.md's "Keeping Rocketlane aligned with what gets filed here" section.
- **The Rocketlane Status Log format also ships by default in that same folder** —
  `STATUS-LOG-RULES.md` (what the note contains). When it's due (weekly by default, off-cycle only
  for a major event) lives in CLAUDE.md's "Weekly Status Log Check" and `CHECKLIST.md`'s Project
  Health Check section.
- **ADRs/Behavior Notes carry a `reviewed_by`/`reviewed_date` field pair while in `Drafts/`, for the
  SA-formed-a-view-but-not-committed signal — the `Drafts/`/`Accepted/` folder they're in is only
  the final promotion signal.** Topic Analysis docs and `architecture-snapshot.md` skip staging
  entirely, so they carry an explicit `Reviewed by SA` field instead (`⏳ Pending SA review` /
  `✅ Reviewed by <name>, <date>` — SA-only, same field-not-folder pattern). Once in `Accepted/` (or
  for Topic Analysis/the snapshot), a document also carries `Atlas candidate` and `Atlas approved`
  fields — see CLAUDE.md
  Hard Rule 12 and "Document stages" below. New docs default to `— Not yet assessed` / `— Not yet`;
  only the SA can set `Atlas approved`.
- **When filing a Customer Need (`Customer Needs/`) or discussing a platform gap, check whether
  it's already on VTEX's roadmap** (`product-ai-hub-mcp`, if connected this session) before
  treating it as net-new — record the result in `CHECKLIST.md` Section H's Roadmap Status column.
  Separately, if something roadmap-relevant to this account comes up unprompted (a future capability
  that could simplify a current workaround, or matters for a later phase), log it in Section I
  (Roadmap Watch) rather than letting it evaporate at the end of the conversation.
  **Status on two related tool limitations (check whether this note itself is stale before
  trusting it — both move fast):**
  - **Fixed 2026-08-25**: `search_cards` used to require the whole query as one literal substring
    (a scattered query like "locale category" returned nothing for a card whose title had both
    words, just not adjacent). That's shipped now — it tokenizes, matches each word anywhere on
    the card, and ranks an exact-phrase match first. Verified directly: "pricing external engines
    context" (words fully out of order) now finds the right card on the first result. Multi-word
    natural-language queries are reliable again; still use `get_card` directly whenever you
    already have a shareKey/URL, since that's always the fastest path regardless of search.
  - **Still in review**: a `list_my_interest_signals` MCP tool
    ([`vtex/product-ai-hub#360`](https://github.com/vtex/product-ai-hub/pull/360)) that will let an
    AI session read back the account's own logged interest signals directly, instead of needing
    the SA to paste a portal screenshot. Until that PR merges, `search_companies`/
    `list_customer_requests` still won't surface a signal (different, unrelated dataset) — a
    portal screenshot or the SA's direct knowledge is the only reliable source for "has this
    account already signaled interest in X." Also worth checking proactively: the account's own
    company-signals view in the portal may list items never filed as a Customer Need in this repo
    at all.
- When the user asks to **store** a document the client shared during the live engagement → place
  it under `Documents Shared by Customer/`, **and**, if it's worth keeping for the team beyond this
  repo, consider uploading a copy to the Drive folder too (per CLAUDE.md Hard Rule 14(b)) — filed
  to fit whatever structure Drive already has for received documents, confirming with the SA first.
- When the user asks to **store** a document the System Integrator shared during the live
  engagement → place it under `Documents Shared by SI/`, with the same optional Drive copy (Hard
  Rule 14(b), SA confirmation first).
- When the user asks to **create** an internal document → place it under `Internal Documents/` in
  the relevant subfolder.
- When a document is ready to share → copy (do not move) it to `Shared/With {{CLIENT_SHORT_NAME}}/` or `Shared/With {{SI_SHORT_NAME}}/`, **and** upload a copy to this project's Google Drive project folder, filed to fit whatever structure it already has (create a new folder there if none fits — don't assume it mirrors this repo) — see CLAUDE.md Hard Rule 14. This repo's copy alone isn't enough; the client can't see this git repo.
- **The same Drive-mirroring requirement applies beyond `Shared/` documents**, per CLAUDE.md Hard
  Rule 14: an ADR/Behavior Note the moment it's promoted into `Accepted/`, an architecture diagram
  filed under `Internal Documents/Architecture/Diagrams/`, and any other finalized
  architecture/design document (Topic Analysis, Solution Design output, a refreshed
  `architecture-snapshot.md`) all get a copy uploaded to the matching path in the Drive folder —
  confirm with the SA first, same as any other Drive upload.
- Functional specs belong in `Functional Specifications/` once approved; drafts stay in `Internal Documents/Solution Design/`.
- ADRs → `Internal Documents/Architecture/ADRs/Drafts/` while drafting; `ADRs/Accepted/` only
  once the SA promotes them (see "Document stages"). Never loose in `ADRs/` itself.
- Architecture topic analysis → `Internal Documents/Architecture/Topic Analysis/`
- Always update `CHECKLIST.md` after adding or creating any file.
- **A milestone, risk change, contract amendment, or phase/status change filed here should also
  prompt a suggested Rocketlane update** (task create/update, phase change) — see `CLAUDE.md`'s
  "Keeping Rocketlane aligned with what gets filed here" for the specific triggers. Suggest it to
  the SA; never write to Rocketlane unconfirmed.
- The primary working areas are `Internal Documents/Architecture/` and `Functional Specifications/`. Keep these current.
- **Meeting-captured drafts land in `ADRs/Drafts/` or `Behavior Notes/Drafts/`, never directly in
  `ADRs/Accepted/` or `Behavior Notes/Accepted/`.** See "Document stages" below for the full
  `Drafts/` → `Accepted/` pipeline — never promote a draft into `Accepted/`
  automatically, that's always an explicit SA action. See `vtex-meeting-decision-capture` in the
  `solution-architecture` plugin for how drafts get created. **If a skill you invoke (e.g.
  `vtex-meeting-decision-capture`) has its own hardcoded instructions naming a different path
  (such as an old flat `Drafts/` folder or a bare `ADRs/`/`Behavior Notes/` destination), this
  file's current structure wins — file the output where this file says, and flag the mismatch
  rather than silently following the skill's stale path.**
- **Run the "Project Health Check" (see `CHECKLIST.md`) proactively, not just when asked.** Any AI
  session picking up this project — at the start of a session, or when asked for a status update —
  should pull the Rocketlane project(s) linked in `PROJECT.md`'s header and compare against what's
  already recorded: does the go-live date still match across fields, is hours-consumed running
  ahead of delivery progress, has profit margin moved, are there new overdue tasks. This is how
  drift and schedule/budget risk get caught automatically instead of waiting for someone to notice.
  Only touch `CHECKLIST.md`/`JOURNAL.md` if something actually changed — don't pad the journal with
  "still fine" re-runs, and never fabricate a number if the underlying Rocketlane/connector access
  isn't actually available in that session. See `CHECKLIST.md`'s "Project Health Check" section for
  the full method, and `CLAUDE.md` for how to set up the recurring automated version of this check.
