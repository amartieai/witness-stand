# MARTY FOR MODERATORS
## A pre-action gate for every removal, ban and refusal
**Version 1.0 · 2026-10-31 · MIT License — copy it, fork it, publish it, no permission needed.**
Canonical text: this document. Adopt by copying §3–§7 into your subreddit's wiki and pinning §8.

---

## 1. The problem, stated without euphemism

A moderator removes a post. The poster gets a sentence. The sentence is often a label — *low effort*,
*spam*, *off topic* — rather than a rule. There is no requirement anywhere on Reddit that the moderator
read the post, quoted the rule, or told the truth about what the post said. There is no guaranteed appeal: no rule entitles a poster to one, sets a deadline for one, or prevents the only route — modmail — from being ignored or refused.

Three failure shapes recur, and each one is cheap to prevent:

| Failure | What it looks like | Who it hurts |
|---|---|---|
| **The unread removal** | Removed within seconds of posting, reason is a category, the specific content was never opened | Good posters, especially new ones |
| **The misquoted rule** | "Rule 6" with no text. The reader cannot tell whether Rule 6 is about labeling, title case, or something the mod invented last week | Everyone — the rule stops teaching |
| **The claim dressed as a fact** | "This is spam", "this is witch-hunting", "this is AI-generated" — an assertion about the content that nobody checked | The poster, who now has to prove a negative to a channel that may refuse to open |

And a fourth that no moderator controls but every moderator should disclose:

| **The invisible override** | A sitewide filter or admin action removes content a moderator already approved, with no reason and no appeal | The moderator's credibility, and the poster's |

Marty does not fix the fourth. Marty makes it visible — which is the most a subreddit can do about
authority it does not hold.

---

## 2. What Marty is

**Marty is a gate, not a bot.** It is four checks that must pass, in order, before an enforcement action
takes effect. Three are policy; one is a line of text that goes into the record.

The whole design rests on one sentence:

> **A machine may hold. A human may remove. Nobody may remove silently.**

Where it lives, concretely: one wiki page (the policy), two AutoModerator rules (the parts a machine can
enforce), one saved response per subreddit rule (the text the poster receives), and one mod-note format
(the stamp). That is the entire install.

**Platform caveat (current Reddit restriction).** AutoMod's enforcement actions — Report, Filter, Remove, Mark as spam, Approve — are no longer available to newly created communities or communities where AutoMod has not been used. Those adopters use Reddit's Rules and Automation mod tools instead, or run Marty manually per §9 ("It does not require a bot"). Check which path your community is on before installing §4's blocks.

---

## 3. The gate

### GATE 1 — GUARD: authority and legibility

**Question:** *Am I allowed to do this, and can I actually see what I am acting on?*

Pass requires all four:
1. **Permission.** The acting account holds the permission bit for this action type (posts, users, wiki…).
2. **Rule exists.** The cited rule is on the subreddit's public rules page, by number and text, *today*.
   A rule remembered from last year, or enforced from a private note, fails.
3. **Rule reaches this content type.** A rule scoped to comments cannot remove a post. A rule about
   titles cannot remove a body.
4. **Legibility.** The material is readable by the acting moderator right now — not a filter banner, not
   a deleted parent, not a crosspost whose original is gone, not an image the moderator has not opened.

**Fails closed.** If you cannot read it, you cannot remove it. You may report it, hold it, or ask. A
removal of something you have not seen is not moderation; it is a guess with a timestamp.

> *the gate that stops a moderator from "confirming" a removal someone else already made.*

### GATE 2 — CHECK: the three attestations

**Question:** *What did I read, what rule applies, and is anything I am about to say about this content
true?*

**(a) Read attestation.** Record the object you read and one identifying feature of it: the post ID, the
body length, the specific lines relied on, or the frame you viewed. "Read the post" is not an attestation;
"read body, 1,842 chars, relied on ¶2–¶3" is.

**(b) Rule, quoted.** The removal reason must contain **the rule's number and its verbatim text**. Not a
paraphrase, not a category. If the rule text is longer than a screen, quote the operative clause and link
the rule.

**(c) Claims verified or struck.** Every factual assertion in the reason must be one of:
- **VERIFIED** — it is checkable against the material (a word is present, a link resolves, the length is
  under the minimum) and you checked it; or
- **STRUCK** — you cannot check it, so it does not appear in the reason.

"You are a spammer", "this is AI-generated", "this is ban evasion", "this account is a bot" are claims.
They are not rule citations. If the rule is *"no spam"*, quote the rule and describe the observable
behaviour; do not assert the intent.

> A removal reason that survives CHECK reads like this:
> *"Removed under Rule 4 — 'Link posts may not contain body text; put commentary in a comment.' Your post
> was a link post with 612 characters of body text. Repost as a bare link."*
> It names the rule, quotes it, states one checkable fact, and tells the poster the cure. Nothing in it
> can be argued with except the rule itself — which is exactly where the argument belongs.

### GATE 3 — JUDGE: the human step

**Question:** *Does this action turn on a judgement about a person or their intent?*

- **Objective/shape rules** (title format, link-only, minimum length, flair required, duplicate URL) may
  be enforced by machine. The rule is a shape and the shape is checkable. AutoMod may `remove`.
- **Judgement/claim rules** ("low effort", "bad faith", "spam", "witch-hunting", "off topic", "AI content")
  may be enforced **only** by a named human, **only** after GATE 1 and 2. AutoMod may `filter` these to a
  queue. It may never `remove` them.

The default for every bot is **hold, not delete**. A queue item is reversible and visible; a removal is
neither.

### GATE 4 — STAMP: the record

No stamp, no action. A stamp is one line, in the mod note and/or the removal message, in this format:

```
MARTY|v1|<RULE-ID>|<rule quoted, ≤40 chars>|read:<object+feature>|claims:<n verified / n struck>|stamp:@<mod>|<ISO-8601 UTC>|appeal:<route>
```

Example:

```
MARTY|v1|R4|"Link posts may not contain body text"|read:post 1abc23 body 612ch ¶1|claims:1v/0s|stamp:@u/example|2026-10-31T22:17:03Z|appeal:reply to this message
```

Rules of the stamp:
- **Named human** for any judgement removal. The stamp is a signature, not a formality.
- **UTC, to the second.** Local time makes a sequence unresolvable.
- **Appeal route named in the message the poster receives** — every time, including machine removals.
- **The stamp outlives the log.** Reddit's moderation log retains 90 days; mod notes are the durable
  copy. Stamp both.

---

## 4. Enforcement on Reddit — the actual configuration

Four blocks. Replace `R4` and the quoted text with your own.

### 4.1 Objective rule, machine removal (allowed) — link submission with body text

```yaml
---
type: link submission
body (regex): ['\S']
priority: 10
action: remove
action_reason: "MARTY R4 link-with-body | read:url+body | stamp:auto"
comment: |
  **Removed: Rule 4 — "Link posts may not contain body text; put commentary in a comment."**

  This post was submitted as a link with body text attached.

  **Cure:** repost as a bare link and add your commentary as the first comment.
  **Appeal:** reply to this message. A human moderator reads replies within 48 hours.
comment_stickied: true
modmail: |
  MARTY stamp — {{permalink}}
  Rule: R4 "Link posts may not contain body text"
  Read: url + body (body text present; exact length stamped by hand in the mod note)
  This removal is a shape check, not a judgement. Reversible on reply.
  #marty
---
```

> **Manual step (GATE 4 durable copy):** AutoMod cannot write a mod note. The moderator must stamp the mod note by hand per §4.4 for every machine removal under this block, so the stamp outlives the 90-day mod log. Stamp both.

### 4.2 Judgement rule, machine hold only (required)

```yaml
---
type: submission
title+body (includes-word): []  # adopting sub fills with its own trigger terms
priority: 20
action: filter
action_reason: "MARTY R7 judgement hold — human stamp required"
modmail: |
  MARTY HOLD — {{permalink}} — Rule 7 "No low-effort posts" needs a human.
  Do not approve or remove without GATE 2: quote the rule, verify or strike any claim.
  #marty
---
```

### 4.3 Ban message template (saved response, required)

```
You have been banned from r/<sub> for <duration>.

Rule: <N> — "<verbatim rule text>"
Content: <permalink to the specific item>
Read: <what the moderator read — e.g. "comment body, ¶2">
Appeal: reply to this message within 30 days. A human moderator will read it. If you believe the ban
itself was made in bad faith, you may also write to r/ModSupport with the subject "Subreddit Ban Appeal".
```

A ban without a quoted rule and a permalink is not a ban; it is a mood.

### 4.4 The mod note format (the durable stamp)

```
MARTY|v1|R7|"No low-effort posts"|read:post 1abc23 body 210ch|claims:0v/1s|stamp:@u/example|2026-10-31T22:20:11Z|appeal:modmail
```

Prefix every Marty note with `MARTY|v1|` so the weekly audit is one search, not an archaeology project.

---

## 5. The appeal, in writing

Publish this and mean it. Four commitments:

1. **Every removal names a rule and quotes it.** No exceptions, no categories standing in for rules.
2. **Every removal names an appeal route** — the reply thread on the removal message. It is never closed,
   and it is never pre-declared ignored.
3. **A human answers within 48 hours** with one of three words: **upheld** (and why), **reversed** (and
   the post restored), or **escalated** (and to whom, and by when).
4. **A reversal is logged, not hidden.** The mod note records the reversal and the reason. Reversals are
   published in the monthly count. A team that reverses nothing is not careful; it is not looking.

---

## 6. The weekly audit (ten minutes, and it is the whole enforcement)

Once a week, a moderator runs three numbers and posts them in mod chat:

1. **Removals in the last 7 days** (mod log, filter: action = remove) — count.
2. **Removals carrying a `MARTY|` stamp** (stamp mirrored into the AutoMod action_reason and counted from the mod log, or the stamp count taken over the weekly ten-removal sample's mod notes) — count.
3. **Appeals answered inside 48h / appeals received** — two counts.

Then sample **ten** removals, including at least two AutoMod ones, and check: rule quoted? claim verified
or struck? named human where judgement was involved? Any failure is corrected in the mod note with a
`CORRECTED:` line — not deleted.

Publish numbers 1–3 monthly. A gate nobody measures is a slogan.

---

## 7. Conformance — the ten fixtures

A subreddit claims adoption only if it passes all ten. Each is a decision, not a discussion; the pass
condition is what the policy *does*, not what the policy says.

| # | Fixture | Pass condition |
|---|---|---|
| 1 | Post removed for "low effort" with no quoted rule | **Refused.** Converted to a hold, or the rule quoted verbatim |
| 2 | AutoMod rule with `action: remove` on a judgement keyword ("spam", "AI") | **Fails conformance.** Must be `filter` |
| 3 | Removal of a post currently showing a sitewide filter banner | **Refused** at GATE 1 (illegible). Reported, not removed |
| 4 | Ban issued with a category, no rule number, no permalink | **Refused.** Ban message template is mandatory |
| 5 | Removal reason asserts "ban evasion" with no check | **Claim struck.** Observable behaviour described instead, or no removal |
| 6 | Modmail reply to an appeal | **Answered ≤48h** with upheld / reversed / escalated |
| 7 | Removal reason quoting the wrong rule number | **Caught by audit**; corrected note filed |
| 8 | Crosspost whose parent was removed; mod acts on the dead copy | **Refused** at GATE 1 (legibility) |
| 9 | Moderator-approved post later removed by a sitewide filter | **Disclosed** in the mod note: "upstream override, not a mod action" |
| 10 | A user asks "which rule?" on a silent removal | **Answered with the rule, or the removal reversed** |

Publish the pass/fail table. Version it. A conformance claim without a table is marketing.

---

## 8. The pinned post (copy verbatim)

> **How we moderate — the Marty gate**
>
> Every removal, ban and refusal in this community passes four checks before it takes effect:
>
> **1. Guard.** The moderator must be able to read what they are acting on, and the rule must exist and
> apply. We do not remove what we have not seen.
> **2. Check.** Every removal reason quotes the rule, word for word. Every factual claim in it is either
> verified against your post or struck. We do not call your post "spam" or "low effort" as a substitute
> for a rule.
> **3. Judge.** Anything that turns on a judgement about you is decided by a named human, never by a bot.
> Bots hold; humans remove.
> **4. Stamp.** Every action is signed with the rule, what was read, who stamped it, and how to appeal.
>
> **Your appeal:** reply to the removal message. A human answers within 48 hours with *upheld*,
> *reversed*, or *escalated*. We publish a monthly count of appeals, reversals, and stamps.
>
> We do not control Reddit's sitewide filters or admin actions. When one of those overrides us, we say so
> in the record rather than letting you guess who removed your post.

---

## 9. What Marty does not do — stated plainly, because overclaiming kills adoption

- **It does not bind Reddit.** A sitewide spam filter, an admin action, or a subreddit-setting change can
  override any moderator decision, including an approval. Marty governs the moderator's own hand only.
- **It does not create a legal right.** It is a voluntary standard, enforceable by nothing but the team
  that adopts it and the users who can read the numbers.
- **It does not stop bad actors.** A determined spammer gets removed under it, with a rule quoted. That is
  the point: the removal should be right, not merely effective.
- **It does not require a bot.** A team of two can run the whole thing with saved responses and mod notes.
  The AutoMod blocks in §4 are conveniences.
- **It costs time.** Roughly 20–40 seconds per judgement removal, plus ten minutes a week. If a team
  cannot pay that, it should say so publicly rather than adopt the words and skip the checks.

---

## 10. Install — thirty minutes

1. Create wiki page `moderation/marty` and paste §3–§6. (5 min)
2. Create one saved response per subreddit rule, each containing: rule number, verbatim rule, the cure,
   the appeal line. (15 min)
3. Add the two AutoMod blocks from §4.1 and §4.2 — objective rules to `remove`, judgement rules to
   `filter`. (5 min) Name which path you are on: if your community is new or AutoMod has not been used there, enforcement actions are unavailable and you use the Rules/Automation tools (or run Marty manually per §9) instead. Manual step: AutoMod cannot write a mod note — stamp each machine removal by hand per §4.4 so the stamp outlives the 90-day mod log.
4. Replace the ban message with §4.3. (2 min)
5. Pin §8. Record the adoption date and version in the wiki page header. (3 min)
6. Run the ten fixtures in §7 as a team, this week, and publish the table. (ongoing)

**Adoption record format:**
`Adopted: <subreddit> · Marty v1.0 · <YYYY-MM-DD> · fixtures passed <n>/10 · published <url>`

---

## 11. Versioning

- **v1.0** — 2026-10-31. First publication. Four gates, stamp format, ten fixtures.
- Changes bump the minor version and are listed here with a date and a one-line reason. Silent edits to a
  published standard are how standards die.
- Forks are encouraged. If you change a gate, change the version, and say why.

---

*Marty is named for the gate, not the gatekeeper. The gate does not care who you are; it asks the same
four questions of everyone, including the person who wrote it.*
