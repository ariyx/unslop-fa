#!/usr/bin/env python3
"""Validate Unslop FA regression-case metadata without external dependencies."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULES_DIR = ROOT / "skills" / "unslop-fa" / "rules"
CASES_FILE = ROOT / "tests" / "expected" / "cases.json"
RULE_ID_RE = re.compile(r"^##\s+([A-Z]\d{2})\s+—", re.MULTILINE)


def load_rule_ids() -> set[str]:
    rule_ids: set[str] = set()
    for path in RULES_DIR.glob("*.md"):
        rule_ids.update(RULE_ID_RE.findall(path.read_text(encoding="utf-8")))
    return rule_ids


def main() -> int:
    errors: list[str] = []
    rule_ids = load_rule_ids()
    cases = json.loads(CASES_FILE.read_text(encoding="utf-8"))

    seen_ids: set[str] = set()
    for case in cases:
        case_id = case.get("id")
        if not case_id or case_id in seen_ids:
            errors.append(f"invalid or duplicate case id: {case_id!r}")
            continue
        seen_ids.add(case_id)

        fixture = ROOT / "tests" / case.get("fixture", "")
        if not fixture.is_file():
            errors.append(f"{case_id}: missing fixture {fixture}")
            continue

        text = fixture.read_text(encoding="utf-8")
        for key in ("expected_rules", "safeguards"):
            for rule_id in case.get(key, []):
                if rule_id not in rule_ids:
                    errors.append(f"{case_id}: unknown rule id {rule_id} in {key}")

        preserve_tokens = case.get("preserve_tokens", [])
        for token in preserve_tokens:
            if token not in text:
                errors.append(f"{case_id}: preserve token not found in fixture: {token!r}")

        expected_paths: dict[str, Path] = {}
        for key in ("expected_detect", "expected_edit"):
            rel = case.get(key)
            if rel:
                expected_path = ROOT / "tests" / rel
                expected_paths[key] = expected_path
                if not expected_path.is_file():
                    errors.append(f"{case_id}: missing {key} file {expected_path}")

        edit_path = expected_paths.get("expected_edit")
        if edit_path and edit_path.is_file():
            edit_text = edit_path.read_text(encoding="utf-8")
            for token in preserve_tokens:
                if token not in edit_text:
                    errors.append(f"{case_id}: preserve token missing from expected edit: {token!r}")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: {len(cases)} cases, {len(rule_ids)} rule IDs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
