# Unslop FA

Persian anti-slop editing rules for agent-based writing tools.

`unslop-fa` detects formulaic, generic, or model-like patterns in Persian prose and makes targeted edits while preserving meaning, uncertainty, technical precision, and the writer's voice.

It does **not** detect whether a text was written by AI. It flags observable writing patterns.

## Status

`v0.1` is a small rule set built from real Persian test cases across analytical, technical, social, marketing, and argumentative writing. The project intentionally grows from regression cases rather than from a large phrase blacklist.

## Goals

- Preserve the writer's voice.
- Make the minimum effective edit.
- Detect Persian-specific formulaic prose, not only translated English patterns.
- Keep claims, uncertainty, citations, numbers, and technical meaning intact.
- Adapt editing behavior to genre.
- Make rule behavior inspectable and testable.

## Modes

### Detect

Identify named patterns, quote the relevant passage, explain the contextual issue, and suggest a revision direction. Do not rewrite the full text or guess authorship.

### Edit

Rewrite only what is necessary, then run the checks in `eval.md` before returning the result.

## Repository structure

```text
unslop-fa/
├── README.md
├── LICENSE
├── NOTICE.md
├── CONTRIBUTING.md
├── skills/
│   └── unslop-fa/
│       ├── SKILL.md
│       ├── eval.md
│       └── rules/
│           ├── core.md
│           ├── persian.md
│           ├── analytical.md
│           ├── argumentative.md
│           ├── technical.md
│           ├── social.md
│           └── marketing.md
└── tests/
    ├── README.md
    ├── fixtures/
    │   ├── ai_like/
    │   ├── human/
    │   └── mixed/
    └── expected/
```

## Design principles

### A pattern is not a verdict

A phrase is not slop by itself. Context determines whether it is redundant, formulaic, generic, or harmful to the writer's voice.

### Preserve facts; remove predictability

The project is stricter about style than about content. Editing should never silently alter numbers, evidence, source attribution, technical scope, or uncertainty.

### Genre matters

An analytical article, technical comparison, LinkedIn post, and landing page fail in different ways. `unslop-fa` uses shared core rules plus genre-specific checks.

### No Persian blacklist

Words such as `بنابراین`, `در نهایت`, or `می‌تواند` are not banned. Repetition and context matter more than isolated vocabulary.

## Seed corpus

The first regression corpus includes five long-form AI-generated Persian drafts, plus focused regression fixtures for individual patterns:

- analytical article;
- technical database comparison;
- professional social post;
- SaaS marketing copy;
- balanced argumentative essay.

Fixtures are editing samples, not factual reference material. Their claims are intentionally preserved during style tests unless a separate verification task is performed. Human benchmarks live directly in `tests/fixtures/human/` to catch false positives without fetch scripts or runtime dependencies. Each benchmark records its source and provenance; full third-party text should only be committed when redistribution is permitted.

## Upstream

This project is inspired by and partially adapted from Peter Yang's [`no-ai-slop`](https://github.com/petergyang/no-ai-slop), especially its detect/edit split, minimum-edit philosophy, named-pattern approach, and post-edit evaluation. Persian rules, genre handling, safeguards, examples, and regression cases are developed independently for Persian prose.

See `NOTICE.md` for attribution.

## License

MIT. See `LICENSE` and `NOTICE.md`.
