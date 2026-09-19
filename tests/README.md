# Tests

The test suite is intentionally small and regression-oriented.

## Fixture groups

- `fixtures/ai_like/seed/` — real seed drafts collected for v0.1 across five genres.
- `fixtures/ai_like/` — smaller synthetic examples for isolated patterns.
- `fixtures/human/` — prose that contains words associated with slop but should generally be preserved.
- `fixtures/mixed/` — drafts containing both useful and formulaic patterns.

Fixtures are writing samples, not factual reference material. A style edit should preserve their claims unless factual verification is explicitly part of the task.

## Expected cases

`expected/cases.json` records:

- which rule IDs should be discoverable in each seed fixture;
- which safeguards matter for that genre;
- tokens or facts that must survive an edit unchanged;
- notes about likely false positives.

These are not exact-output golden files. Natural-language editing can have multiple valid rewrites.

## Structural validation

Run:

```bash
python tests/validate_cases.py
```

The validator checks that fixtures exist, rule IDs referenced by cases exist in the rule set, and case metadata is well formed.

## Regression philosophy

Add a regression case when one of these happens:

1. a real AI-like pattern is missed repeatedly;
2. a useful human sentence is incorrectly flagged;
3. an edit changes meaning, evidence, uncertainty, or technical terminology;
4. a genre-specific pattern needs behavior different from the core rule.

Prefer a small reproducible case over adding a broad new blacklist rule.

## Human benchmarks

Human false-positive fixtures live directly in `fixtures/human/`. Third-party excerpts must be short, attributed, and include the original URL and publication date in front matter. Do not copy full articles into the repository.

The primary failure condition is over-editing: distinctive human prose should not be normalized merely because it contains a pattern that also appears in generated text.
