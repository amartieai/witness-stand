# Batch 1 — Repository inventory

**Status: COMPLETE.** Inventory scope: public GitHub repository `amartieai/witness-stand`, default branch `main`, reviewed against the repository tree at commit [`eace2cfa971a89e5b9688166655dd02c752e235b`](https://github.com/amartieai/witness-stand/tree/eace2cfa971a89e5b9688166655dd02c752e235b). Findings below distinguish repository-verified facts from project assertions; citations point to the records reviewed.

## What the project is

- **VERIFIED (repository contents):** The README describes The Witness Stand as an open process for grading moderation decisions, based on four questions about whether the material was read, the exact rule cited, claims checked, and a named human providing the stamp. The README also links to the project's Reddit community and an external scorecard. [README](https://github.com/amartieai/witness-stand/blob/eace2cfa971a89e5b9688166655dd02c752e235b/README.md)
- **VERIFIED (implementation artifacts exist):** The downloadable kit contains moderator instructions, the four-question gate, AutoModerator YAML, response templates, a Python recorder, a scorecard template, and certification material. The recorder README describes it as stdlib-only, hash-and-record tooling that leaves grading to the gate and does not connect to Reddit or an external service. [Kit README](https://github.com/amartieai/witness-stand/blob/eace2cfa971a89e5b/kit/README.md) · [Recorder README](https://github.com/amartieai/witness-stand/blob/eace2cfa971a89e5b/kit/recorder/README.md)
- **ASSERTION (project statement, not independently established by this inventory):** The README says 12 moderation decisions have been graded (1 pass, 11 fails), and calls the scorecard public. The linked scorecard itself was not independently audited in this batch. [README](https://github.com/amartieai/witness-stand/blob/eace2cfa971a89e5b/README.md)
- **ASSERTION / explicitly proposed, not implemented:** `FAKE_WITNESS.md` calls the speaker-grading instrument a design and says it is not yet built; a companion challenge file nevertheless records a specific verdict against a Reddit account. That file's account, comment, document, and verdict claims have not been independently verified here. [FAKE_WITNESS spec](https://github.com/amartieai/witness-stand/blob/eace2cfa971a89e5b/FAKE_WITNESS.md) · [Challenge #1](https://github.com/amartieai/witness-stand/blob/eace2cfa971a89e5b/fake_witness_challenge_001_opening_map_6898.md)

## Repository contents

**VERIFIED:** The recursive repository tree at the reviewed commit contains these files and directories; no additional tracked paths appeared in that tree. [Repository tree](https://github.com/amartieai/witness-stand/tree/eace2cfa971a89e5b9688166655dd02c752e235b)

```text
FAKE_WITNESS.md                         speaker-grading design spec
LICENSE                                 repository license
README.md                               project overview and links
fake_witness_challenge_001_opening_map_6898.md  one speaker-challenge case file
kit/
  CERTIFICATION.md                      audit/certification process
  LICENSE                               kit license
  MARTY_FOR_MODERATORS.md               moderator policy pack
  PUBLISH_NOTES.md                      publication/correction notes
  README.md                             kit guide and stated limits
  SCORECARD_TEMPLATE.md                scorecard form
  THE_FOUR_QUESTIONS.md                 gate summary
  automod/
    judgement-hold-human-stamp.yaml     AutoModerator configuration
    objective-removal-link-with-body.yaml AutoModerator configuration
  recorder/
    README.md                           recorder usage/limits
    recorder.py                         witness-pair recorder
  templates/
    ban_message.md                      ban message template
    saved_response_judgement_hold.md    saved response template
    saved_response_objective_removal.md saved response template
```

## What the project asserts

These are **project assertions**, not findings independently proved by this batch:

1. A four-check, pre-action process should govern removals, bans, or refusals, with a named human responsible for the stamp; the project presents this as a method for accountability. [README](https://github.com/amartieai/witness-stand/blob/eace2cfa971a89e5b9688166655dd02c752e235b/README.md) · [MARTY pack](https://github.com/amartieai/witness-stand/blob/eace2cfa971a89e5b9688166655dd02c752e235b/kit/MARTY_FOR_MODERATORS.md)
2. The kit is free/MIT and intended for reuse; the kit documentation also states that it does not bind Reddit and cannot override sitewide or administrative actions. [Kit README](https://github.com/amartieai/witness-stand/blob/eace2cfa971a89e5b9688166655dd02c752e235b/kit/README.md) · [Kit license](https://github.com/amartieai/witness-stand/blob/eace2cfa971a89e5b9688166655dd02c752e235b/kit/LICENSE)
3. The Fake Witness design proposes auditing speakers' claims against source chains and their own prior statements, with FAKE / NORMAL / TRUE tiers, public records, and a reader-side feed filter. It explicitly labels this as a design/proposed build path. [FAKE_WITNESS spec](https://github.com/amartieai/witness-stand/blob/eace2cfa971a89e5b9688166655dd02c752e235b/FAKE_WITNESS.md)
4. The challenge document asserts that its subject made seven comments, made claims contradicted or unsupported by documents, and was stamped FAKE by the author. These are allegations in a project-authored case file, not confirmed facts from this inventory. [Challenge #1](https://github.com/amartieai/witness-stand/blob/eace2cfa971a89e5b9688166655dd02c752e235b/fake_witness_challenge_001_opening_map_6898.md)

## GitHub project activity and publication

- **VERIFIED:** Repository metadata reports the project is public, Python is its GitHub-detected language, its default branch is `main`, and Issues are enabled. The metadata reports Discussions are disabled. [Repository page](https://github.com/amartieai/witness-stand)
- **VERIFIED:** Five open issues (#1–#5) were returned by the repository issue query. They solicit contributions on a speaker challenge, speaker scorecard/registry, media/deepfake checks, platform accountability data, and a reader-side feed gate. [Issue #1](https://github.com/amartieai/witness-stand/issues/1) · [#2](https://github.com/amartieai/witness-stand/issues/2) · [#3](https://github.com/amartieai/witness-stand/issues/3) · [#4](https://github.com/amartieai/witness-stand/issues/4) · [#5](https://github.com/amartieai/witness-stand/issues/5)
- **VERIFIED (query result):** The closed-issues query returned no items. Discussions could not be enumerated as a discussion feed; repository metadata says discussions are disabled. [Repository page](https://github.com/amartieai/witness-stand)
- **VERIFIED:** The repository has a v1.0 release titled “The Witness Stand — Kit v1.0”, published 2026-11-01. The release description says it publishes the moderator kit, templates, recorder, scorecard, and certification papers. This is the release's own description. [Release v1.0](https://github.com/amartieai/witness-stand/releases/tag/v1.0)

## Material not found / gaps in repository

- **NOT FOUND in tracked tree:** No separate `docs/`, changelog, architecture document, package/dependency manifest, test suite, or CI workflow appeared in the reviewed tree. This records absence in the tree, not proof such material does not exist elsewhere. [Repository tree](https://github.com/amartieai/witness-stand/tree/eace2cfa971a89e5b9688166655dd02c752e235b)
- **NOT VERIFIED in this batch:** Whether the linked subreddit scorecard actually contains 12 entries with the reported 1/11 result; whether the underlying moderation decisions, source documents, or independent review support the asserted grades; and whether the Fake Witness challenge's account-level assertions and verdict are accurate. The project README, design spec, and challenge file are primary project statements, not independent corroboration. [README](https://github.com/amartieai/witness-stand/blob/eace2cfa971a89e5b9688166655dd02c752e235b/README.md) · [Challenge #1](https://github.com/amartieai/witness-stand/blob/eace2cfa971a89e5b9688166655dd02c752e235b/fake_witness_challenge_001_opening_map_6898.md)
- **NOT FOUND via repository metadata:** No Discussions feature is enabled, so there is no repository Discussions collection to inventory. [Repository page](https://github.com/amartieai/witness-stand)

## Batch 1 completion

Batch 1 is complete: repository tree and primary project documents were inventoried; GitHub issues, discussions status, and releases were checked; repository assertions and missing/unchecked materials are separated. Batch 2 (claims register), Batch 3 (subject research), and Batch 4 (gaps and next steps) remain.
