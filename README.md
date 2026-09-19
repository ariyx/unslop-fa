# Unslop FA

Persian anti-slop editing rules for agent-based writing tools.

`unslop-fa` detects formulaic, generic, or model-like patterns in Persian prose and makes targeted edits while preserving meaning and voice.

It does **not** claim to detect whether a text was written by AI. It flags observable writing patterns.

## Goals

- Preserve the writer's voice.
- Make the minimum effective edit.
- Detect Persian-specific formulaic prose, not just translated English patterns.
- Keep claims, uncertainty, citations, and technical meaning intact.
- Make behavior testable with small fixtures and regression cases.

## Modes

### Detect

Identify named slop patterns, quote the relevant passage, explain the issue briefly, and suggest a direction for revision. Do not rewrite the full text.

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
│       └── eval.md
└── tests/
    └── fixtures/
        ├── ai_like/
        ├── human/
        └── mixed/
```

## Current scope

The first version focuses on Persian prose. It starts with a small rule set and grows only when a repeated pattern is supported by examples.

The project currently targets:

- repetitive discourse connectors;
- stacked hedging and modal verbs;
- formulaic binary contrasts;
- fake-profound endings;
- bureaucratic and inflated phrasing;
- vague attribution;
- translated-English cadence;
- excessive symmetry and list rhythm;
- needless restatement in conclusions;
- generic abstractions where concrete wording is available.

## Design rule

A rule should not exist because a phrase "sounds AI." It should exist because the pattern is observable, repeated, and harmful to clarity or voice in context.

## Upstream

This project is inspired by and adapted from Peter Yang's `no-ai-slop` project. See `NOTICE.md` for attribution.

## License

MIT. See `LICENSE` and `NOTICE.md`.