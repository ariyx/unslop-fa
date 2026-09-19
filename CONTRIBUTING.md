# Contributing

Keep contributions evidence-based, small, and regression-driven.

## Adding or changing a rule

A rule should include:

1. a stable rule ID;
2. a clear name;
3. an observable pattern;
4. a `Do not flag` or safeguard section describing false positives;
5. a rewrite direction that does not require invented facts;
6. an example when useful;
7. a fixture or regression case when the behavior came from a real failure.

Avoid universal banned-word rules. Most Persian phrases are context-dependent.

## Where a rule belongs

Use `core.md` only when the behavior is broadly useful across genres. Put Persian-language phenomena in `persian.md`. Put behavior that should change by genre in the relevant genre file.

Do not add the same rule to several files just because it appears in several genres.

## Adding a fixture

Use:

- `tests/fixtures/ai_like/seed/` for long real-world seed cases;
- `tests/fixtures/ai_like/` for small isolated pattern examples;
- `tests/fixtures/human/` for false-positive protection;
- `tests/fixtures/mixed/` for cases where some patterns should change and others should stay.

Fixtures are not factual reference sources. Do not silently "correct" their content during style regression work.

If the fixture participates in the v0.1 regression suite, add or update its entry in `tests/expected/cases.json` and run:

```bash
python tests/validate_cases.py
```

## Pull requests

Prefer one rule, one safeguard, or one behavior change per pull request. Explain:

- the missed pattern or false positive;
- the smallest example that reproduces it;
- why the proposed rule belongs in its chosen layer;
- what existing behavior must remain unchanged.
