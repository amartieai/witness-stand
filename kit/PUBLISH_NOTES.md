# PUBLISH NOTES — Witness Kit v1.0 (published 2026-11-01)

**Provenance.** This kit was packaged on the founder's machine as `kit_v1` under order
ORD-0227 and reported in REP-0227; the packaged files' sha256 table is in that report. The
kit was then audited from a verbatim, hash-verified pull (audit: REP-0227 kit audit,
2026-11-01) before publication. The box copy is unchanged. Four corrections were applied
at publish, from the overseer's seat, and are listed here so the published kit's difference
from the packaged kit is on the record — amend, never silently edit.

1. **AutoMod body check (audit correction C1).** The packaged YAML block and §4.1 of the
   pack carried `body (regex): ['\\S']` (two backslashes), which a YAML reader passes to
   the regex engine as a literal backslash-plus-S — a check that would never fire on
   ordinary post text. REP-0227's text states the single-backslash form was inserted; the
   bytes disagreed, and this note corrects the report's claim on the record. Published
   form, as the audit prescribed: `body (regex): ['\S']`.
2. **License.** The packaged kit asserted CC BY 4.0 (its order's spec). The founder ruled
   on 2026-10-31 that the whole kit, code and papers, is MIT. The license statements in
   README.md and the pack header were swapped to MIT at publish, and the MIT LICENSE file
   was added.
3. **One-pager consistency.** THE_FOUR_QUESTIONS.md's "Moderator's Visit" section now
   carries the visit-before-ruling rule, and no longer restates the sweep-attribution
   sentence the pack audit struck from the pack itself (correction C8) — one record, one
   story.
4. **Certification demand.** CERTIFICATION.md now carries the stand's demand —
   "No certification, no ban hammer" — per the founder's Addendum 1 (2026-10-31). The
   honest limit is unchanged and stands in the same file: nothing in law compels
   certification; the public record is the leverage.

**What did not change.** The gate itself (Guard · Check · Judge · Stamp), the corrected
pack's substance, the recorder, the templates, and the scorecard format are exactly as
packaged and audited.
