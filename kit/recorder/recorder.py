#!/usr/bin/env python3
"""Witness-pair recorder — minimal, stdlib only.

Reads a post text and a decision text, sha256-hashes both, and emits:
  (a) a frozen witness-pair record (JSON), and
  (b) one scorecard row in the stand's published format.

It keeps the tape. It does not grade — grading is the gate, and the stamp is a named human.

Usage:
  python recorder.py --post "..." --decision "..."
  python recorder.py --post-file post.txt --decision-file decision.txt
  python recorder.py --post "..." --decision "..." --out-dir ./out

Options:
  --community NAME   community name for the scorecard row (optional)
  --moderator NAME   moderator name for the scorecard row (optional)
  --decision-id ID   decision id / permalink for the scorecard row (optional)
  --out-dir DIR      write frozen record + scorecard row to files (optional)
"""

import argparse
import datetime
import hashlib
import json
import os
import sys


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_text(arg, path):
    if path:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return arg if arg is not None else ""


def main():
    ap = argparse.ArgumentParser(description="Witness-pair recorder")
    ap.add_argument("--post", help="post text")
    ap.add_argument("--post-file", help="path to file containing post text")
    ap.add_argument("--decision", help="decision text")
    ap.add_argument("--decision-file", help="path to file containing decision text")
    ap.add_argument("--community", default="", help="community name")
    ap.add_argument("--moderator", default="", help="moderator name")
    ap.add_argument("--decision-id", default="", help="decision id / permalink")
    ap.add_argument("--out-dir", default="", help="directory to write outputs")
    args = ap.parse_args()

    post_text = read_text(args.post, args.post_file)
    decision_text = read_text(args.decision, args.decision_file)

    post_hash = sha256_text(post_text)
    decision_hash = sha256_text(decision_text)
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()

    record = {
        "witness_pair": "v1",
        "timestamp_utc": now,
        "community": args.community,
        "moderator": args.moderator,
        "decision_id": args.decision_id,
        "post": {
            "text": post_text,
            "sha256": post_hash,
            "length_chars": len(post_text),
        },
        "decision": {
            "text": decision_text,
            "sha256": decision_hash,
            "length_chars": len(decision_text),
        },
    }
    # integrity hash over the canonical record (post + decision hashes + timestamp)
    record_sha = sha256_text(json.dumps(record, sort_keys=True, ensure_ascii=False))
    record["record_sha256"] = record_sha

    # Scorecard row in the stand's published format.
    # Columns: Decision | Verdict | L1 Read | L2 Cited | L3 Verified | L4 Stamp | Blocked anyway | Notes
    did = args.decision_id if args.decision_id else "-"
    row = "| {did} | PENDING (gate grades) | - | - | - | - | - | recorder keeps the tape; grading is the gate |".format(did=did)

    print(json.dumps(record, indent=2, ensure_ascii=False))
    print()
    print("--- scorecard row (published format) ---")
    print(row)

    if args.out_dir:
        os.makedirs(args.out_dir, exist_ok=True)
        stamp = now.replace(":", "").replace("-", "")
        record_path = os.path.join(args.out_dir, "witness_pair_{0}_{1}.json".format(stamp, post_hash[:8]))
        with open(record_path, "w", encoding="utf-8") as f:
            json.dump(record, f, indent=2, ensure_ascii=False)
            f.write("\n")
        scorecard_path = os.path.join(args.out_dir, "scorecard_row.md")
        with open(scorecard_path, "w", encoding="utf-8") as f:
            f.write(row + "\n")
        print()
        print("wrote: {0}".format(record_path))
        print("wrote: {0}".format(scorecard_path))


if __name__ == "__main__":
    main()
