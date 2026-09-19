---
name: unslop-fa
description: Detect or edit formulaic AI-like patterns in Persian prose while preserving meaning, uncertainty, technical precision, citations, and the writer's voice.
---

# Unslop FA

Edit Persian prose with restraint. Remove observable formulaic patterns without flattening the writer's voice or turning formal writing into casual writing.

Never claim that a text was written by AI. This skill detects writing patterns, not authorship.

## Modes

### Detect

Use when the user asks to audit, scan, flag, or inspect a draft without rewriting it.

For each finding:

1. name the rule;
2. quote the smallest useful passage;
3. explain why it weakens this specific text;
4. give a short revision direction.

Do not score the text, estimate an AI probability, or rewrite the full draft unless asked.

### Edit

Use when the user asks to improve, humanize, de-slop, or rewrite a draft.

Make the minimum effective edit. Preserve claims, uncertainty, citations, numbers, technical terms, register, and distinctive voice unless the user asks for a different goal.

## Rule loading

Always apply:

- `rules/core.md`
- `rules/persian.md`

Then apply the relevant genre file when the genre is clear:

- `rules/analytical.md` — reports, explainers, analytical essays
- `rules/argumentative.md` — balanced arguments, compare-both-sides essays
- `rules/technical.md` — engineering, software, scientific, technical prose
- `rules/social.md` — LinkedIn, personal posts, threads, captions
- `rules/marketing.md` — landing pages, product copy, launch copy

A draft may use more than one genre file. Genre rules are additional checks, not permission to rewrite more aggressively.

## Editing principles

### Preserve the writer

Before editing, notice vocabulary, cadence, bluntness, humor, uncertainty, digressions, and level of polish. Keep traits that appear intentional.

### Minimum effective edit

Fix the pattern, not the whole paragraph. Leave strong sentences alone.

### Preserve factual precision

Do not change a number, date, source, proper noun, technical term, quoted claim, scope, or degree of certainty merely to improve style.

### Preserve quoted and embedded voices

Treat quotations, pasted comments, correspondence, interview answers, cited examples, and other clearly attributed passages as protected voice boundaries. Do not use their style as evidence about the surrounding author's voice, and do not rewrite them unless the user explicitly asks to edit the quoted material itself.

When a draft alternates between the author's prose and another person's words, evaluate each voice in its own context. A formulaic-looking phrase inside an attributed passage is not, by itself, a finding against the surrounding prose.

### Concrete beats generic

When the source already contains a mechanism, example, number, consequence, or observable behavior, prefer it over a broad statement about importance, impact, efficiency, or transformation.

Never invent specificity that is not in the draft.

### Context beats blacklist

No Persian word is banned merely because models often use it. «بنابراین»، «در نهایت»، «می‌تواند»، and similar words may be correct. Flag them only when their use is habitual, redundant, or structurally formulaic.

### When uncertain, preserve

A possible pattern is not enough to justify an edit. If the same feature plausibly comes from personal voice, narrative timing, colloquial Persian, technical precision, or deliberate emphasis, leave it alone unless the surrounding text makes the formulaic pattern clear.

### Do not casualize by default

Formal Persian can be natural. Academic, technical, legal, and professional prose may need formality.

### Technical prose is conservative by default

When technical correctness and stylistic variation conflict, preserve correctness. Consistent terminology, caveats, and repeated domain terms are often desirable.

## Workflow

1. Read the entire draft.
2. Identify its purpose, audience, register, and genre.
3. Identify the voice traits worth preserving.
4. Apply core and Persian rules, then the relevant genre rules.
5. For Detect, report only observable findings and stop.
6. For Edit, make the smallest set of changes that removes the real patterns.
7. Run `eval.md`.
8. If a check fails, revise the edit before returning it.

## Detect output

Prefer a compact list or table with:

- rule ID and name;
- quoted passage;
- why it is a problem here;
- revision direction.

Avoid speculative statements about authorship.

## Edit output

Return:

1. the full edited text;
2. a short `What changed` section naming only the main interventions.

Do not produce a change log for every sentence unless the user asks.
