---
name: unslop-fa
description: Detect or edit formulaic AI-like patterns in Persian prose while preserving meaning, uncertainty, citations, and the writer's voice.
---

# Unslop FA

Edit Persian prose with restraint. Remove formulaic patterns without flattening the writer's voice or turning formal writing into casual writing.

Do not guess whether AI wrote the text. Detect observable patterns only.

## Jobs

### Detect

Use when the user asks to audit, scan, or identify slop without rewriting.

For each finding:

1. name the pattern;
2. quote the smallest relevant passage;
3. explain why it weakens the text in this context;
4. suggest a short revision direction.

Do not score the text. Do not estimate an "AI probability."

### Edit

Use when the user asks to improve or humanize a draft.

Make the minimum effective edit. Preserve factual claims, qualifiers, citations, technical terminology, and the author's level of formality unless the user asks otherwise.

## Workflow

1. Read the full draft before editing.
2. Identify the point, audience, register, and voice traits worth preserving.
3. Mark only patterns that are actually present in context.
4. For Detect, return findings and stop.
5. For Edit, change the smallest amount needed.
6. Run the checks in `eval.md`.
7. If an edit changes meaning, certainty, evidence, or voice unnecessarily, revert or revise it.

## Core principles

### Preserve voice

Do not make every paragraph equally polished. Keep deliberate roughness, humor, bluntness, technical density, or personal phrasing when it belongs to the writer.

### Prefer local edits

Do not rewrite an entire paragraph because one sentence is formulaic.

### Preserve epistemic strength

Do not turn "may" into certainty, or certainty into hedging, unless the original is unsupported or the user asks for a factual correction.

### Do not casualize by default

Formal Persian can be human. The goal is not conversational tone; the goal is natural, precise prose.

## Persian slop patterns

### 1. Repetitive discourse connectors

Watch for repeated paragraph openings such as:

- بنابراین
- در نتیجه
- به همین دلیل
- از این منظر
- در چنین شرایطی
- در مقابل
- به عبارت دیگر

These are not banned words. Flag them when they create a repeated mechanical cadence or state a relationship the reader already understands.

Fix: delete the connector, vary the sentence structure, or state the causal link directly.

### 2. Stacked hedging

Watch for dense repetition of:

- می‌تواند
- ممکن است
- احتمالاً
- به نظر می‌رسد
- تا حدی

Hedging can be necessary. The problem is stacked or habitual uncertainty that makes every claim sound equally tentative.

Fix: keep the qualifier only where the evidence requires it.

### 3. Formulaic binary contrast

Examples:

- مسئله X نیست، بلکه Y است.
- این فقط X نیست؛ Y هم هست.
- هدف رقابت با X نیست، بلکه استفاده از Y است.

These can be useful once. Repeated use produces a predictable rhetorical frame.

Fix: state the actual claim directly when the contrast adds no information.

### 4. Fake-profound ending

Watch for conclusions that turn the topic into a sweeping opposition, slogan, or universal lesson without adding evidence.

Typical shapes:

- آینده متعلق به کسانی است که...
- مسئله انسان در برابر فناوری نیست...
- آینده از راه نمی‌رسد؛ همین حالا اینجاست.

Fix: end on the most concrete implication, unresolved question, or supported conclusion.

### 5. Bureaucratic inflation

Watch for phrases such as:

- نقش بسزایی ایفا می‌کند
- حائز اهمیت است
- در راستای
- مورد استفاده قرار می‌گیرد
- به انجام رساندن
- از اهمیت ویژه‌ای برخوردار است

Do not replace formal language merely because it is formal. Edit when a shorter form says the same thing more clearly.

Fix: prefer direct verbs and concrete nouns.

### 6. Vague attribution

Examples:

- کارشناسان معتقدند
- تحقیقات نشان می‌دهد
- بسیاری بر این باورند
- گزارش‌ها حاکی از آن است

Fix: name the source when available. If the source is not available, avoid manufacturing authority.

### 7. Translated-English cadence

Look for grammatically valid Persian whose order or rhythm mirrors English too closely, especially repeated subject-first structures, unnecessary pronouns, and literal rhetorical templates.

Fix: rewrite for natural Persian information order without changing technical meaning.

### 8. Excessive symmetry

Watch for paragraphs built from repeated three-part or four-part lists, paired oppositions, or sentences with nearly identical length and grammar.

Fix: keep symmetry only when it genuinely clarifies categories or comparison.

### 9. Restated conclusion

A conclusion should not replay the article section by section using the same vocabulary.

Fix: compress repeated claims and preserve only the final synthesis, implication, or unresolved point.

### 10. Generic abstraction

Examples:

- تحولی بزرگ
- فرصت‌های گسترده
- چالش‌های مهم
- نقش کلیدی
- تأثیر قابل‌توجه

These phrases are not automatically wrong. Flag them when the surrounding text does not say what changed, for whom, by how much, or in what way.

Fix: replace with a concrete effect when the source text supports one.

### 11. Mechanical paragraph thesis

Watch for every paragraph opening with a neat thesis sentence followed by two explanatory sentences and a mini-conclusion.

Fix: vary paragraph function. Some paragraphs can present evidence, examples, qualifications, or transitions without announcing themselves.

### 12. Punchline sentence

Watch for compact rhetorical lines designed to sound quotable rather than precise.

Fix: keep them when they are genuinely the writer's voice. Otherwise replace with a concrete claim or merge them into the surrounding paragraph.

## Non-rules

Do not flag a phrase solely because it appears on a blacklist.

Do not remove:

- necessary technical terminology;
- source-required hedging;
- deliberate repetition for emphasis;
- formal register appropriate to academic, legal, or technical writing;
- a distinctive sentence merely because it is polished.

Context decides.

## Output

### Detect output

Return findings grouped by named pattern. Keep each finding brief and specific. Do not rewrite the full draft unless asked.

### Edit output

Return the full edited text, then a short `What changed` section naming only the main interventions.
