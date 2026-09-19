# Contributing

Keep contributions evidence-based and small.

## Adding a rule

A new rule should include:

1. a clear name;
2. a description of the observable pattern;
3. at least two Persian examples from different contexts;
4. a note explaining when the pattern is acceptable;
5. a fixture or regression case.

Avoid universal banned-word rules. Most Persian phrases are context-dependent.

## Adding a fixture

Put examples in one of:

- `tests/fixtures/ai_like/`
- `tests/fixtures/human/`
- `tests/fixtures/mixed/`

Fixtures should be short enough that a reviewer can inspect them manually.

## Pull requests

Prefer one rule or one behavior change per pull request. Explain what false positive or missed pattern the change fixes.
