# Client Communication Playbook

> Ships with every client repo, filled in from day one — not an "if this engagement needs one"
> doc. Read this before drafting any client-facing communication (email, Slack/Teams message,
> status update, meeting follow-up). The **Engagement-Specific Notes** section at the bottom is
> the only part that should differ between clients — the rest is standing PS practice and should
> stay identical to the template unless the SA deliberately changes it here.

## Before you write anything

1. **Pull facts, don't reconstruct them from memory.** Read `PROJECT.md`'s header and the relevant
   `CHECKLIST.md` rows for whatever you're reporting on. Never state a date, a percentage, or a
   status color in a client communication unless you can point to where it came from in this repo
   or a connected system (Rocketlane, etc.).
2. **Know who's reading it.** Check `PROJECT.md`'s stakeholder list for the right names and the
   right level of technical detail — a message to an executive sponsor and a message to the SI's
   engineering lead earn different framing of the same fact.
3. **This produces a draft, never a send.** Drafting a communication is a Regular action; actually
   sending it (email, Slack message, calendar invite) requires the SA's explicit go-ahead — that's
   already a standing rule for any AI session, not something specific to this playbook.

## What never goes external

Internal tracking language is for this repo, not for the client. Translate before sending:

- **Internal risk IDs and `CHECKLIST.md` row codes** (e.g. `R13`, `A18`) are our shorthand — a
  client sees the issue described in plain language, not the ID.
- **Internal document IDs** (`ADR-NNN`, `BN-NNN`, `GAP-NNN`, `FR-NNN`, `TOPIC-NNN`, and the like)
  work the same way — the recipient may have no access to VTEX's internal architecture register,
  so "documented as ADR-005" is meaningless to them at best and an accidental disclosure of
  internal process at worst. Describe the decision and its substance in plain language instead.
- **A fact sourced exclusively from a VTEX-internal-only meeting** (no client or SI attendee)
  never goes into client-facing material, even if it seems purely technical. The rule is about
  where the fact came from, not how sensitive it sounds: the same fact is fine once it has been
  raised in a session the client/SI attended, or the SA states it directly for external use.
- **Raw health colors and budget/hours-consumed percentages** are internal signals, not
  automatically shareable facts — whether and how to surface them externally is the SA's call each
  time, not a default.
- **`Sales Phase/` content has no authority** (see `STRUCTURE.md`'s Agent Instructions) — never
  quote it to a client as current scope or architecture; that's `PROJECT.md` §5 and the ADRs.
- **An unreviewed item in `Internal Documents/Architecture/ADRs/Drafts/` or
  `Internal Documents/Architecture/Behavior Notes/Drafts/`** hasn't been promoted by the SA yet —
  don't reference it as decided.
- **`Contract/Amendments/` candidates that haven't been signed yet** — describe them as proposed,
  never as agreed, until a signed entry actually exists.

## Structure by communication type

**Status update (email or Slack).** One-line headline first (what changed since last update), then:
what shipped, what's next, any ask or blocker with a clear owner and date, next touchpoint. Skip
sections that have nothing new rather than padding them out.

**Escalation.** State the issue in one plain sentence before any context. Then: impact if
unresolved, the options considered, the specific decision or action being requested, and the
deadline that decision is needed by. Escalations are for things that need a decision or unblock —
not a place to restate general status.

**Meeting follow-up.** Decisions made (plain language, not ADR-speak), action items with an owner
and a date each, open questions still outstanding. Link back to the source meeting note in
`meetings/` for anyone who wants full detail, rather than reproducing the whole transcript.

**Ad-hoc Slack/Teams message.** Shorter than an email, one topic per message, lead with the
question or the ask rather than burying it in context.

## Tone

Direct and specific over broad and reassuring — a vague "things are progressing well" reads as
evasive once a client has seen a few real updates. State what's true, including setbacks, and pair
any setback with what's being done about it. Match the client's own register (formal vs.
conversational) rather than defaulting to one house style regardless of audience.

---

## Engagement-Specific Notes

_Populate this section as you learn this specific client's communication preferences — channel
preference (email vs. Slack vs. Teams), who must always be cc'd, tone expectations, cadence. Leave
it empty rather than guessing; an AI session drafting a communication should ask the SA if this
section is empty and the preference isn't obvious from `PROJECT.md`'s stakeholder list._

- Pending — no engagement-specific communication preferences recorded yet.
