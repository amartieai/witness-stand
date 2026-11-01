# Witness-pair recorder

Minimal recorder for the Marty witness stand. Stdlib Python only — no dependencies.

## What it does

- Takes a post text and a decision text (as arguments or files).
- sha256-hashes both, independently, so neither can be silently altered later.
- Emits (a) a frozen witness-pair record (JSON) containing both texts, both hashes, lengths,
  timestamp, and an integrity hash over the canonical record.
- Emits (b) one scorecard row in the stand's published format, with the verdict left as
  PENDING (gate grades).

## What it does not do

- It does not grade. Grading is the gate; the stamp is a named human.
- It does not remove, hold, ban, or refuse anything.
- It does not contact Reddit or any external service. Data is inbound-only.
- It does not store anything unless you pass `--out-dir`.

## Run

    python3 recorder.py --post "post body" --decision "removal reason"
    python3 recorder.py --post-file post.txt --decision-file decision.txt --out-dir ./out
