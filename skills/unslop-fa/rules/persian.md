# Persian-specific rules

These rules target patterns that are especially common in generated, translated, bureaucratic, or over-formal Persian.

## P01 — Bureaucratic inflation

**Detect:** Inflated phrases where a direct Persian verb would carry the same meaning, especially repeated forms such as «نقش بسزایی ایفا می‌کند»، «حائز اهمیت است»، «مورد استفاده قرار می‌گیرد»، «به انجام رساندن»، «در راستای».

**Do not flag:** Legal, administrative, or institutional register where the wording is required or conventional.

**Rewrite:** Prefer a direct verb or concrete noun while preserving formality.

## P02 — Translationese cadence

**Detect:** Grammatically acceptable Persian whose word order, pronouns, rhetorical structure, or clause chaining closely mirrors English and feels unnatural in Persian.

**Do not flag:** Technical prose that necessarily follows source terminology or parallel documentation.

**Rewrite:** Reorder information for natural Persian. Preserve technical terms and scope.

## P03 — Nominalized prose

**Detect:** Dense chains of abstract nouns and light verbs where ordinary verbs would be clearer: «انجام فرایند بررسی»، «ایجاد امکان مدیریت»، «ارائه قابلیت انجام...».

**Do not flag:** Terminology where the noun phrase is the established term.

**Rewrite:** Convert only unnecessary noun stacks into direct verbs.

## P04 — Ezafe-chain overload

**Detect:** Long noun phrases linked by several ezafe relations that force the reader to hold too much structure before reaching the verb.

**Do not flag:** Proper names, technical labels, or compact domain terms.

**Rewrite:** Split the phrase, move a modifier into a clause, or use a shorter head noun.

## P05 — Habitual modal stacking

**Detect:** Dense repetition of «می‌تواند»، «ممکن است»، «احتمالاً»، «به نظر می‌رسد»، «تا حدی» beyond what uncertainty requires.

**Do not flag:** Scientific, legal, forecasting, or risk language where epistemic caution is substantive.

**Rewrite:** Preserve the qualifier where evidence requires it; remove only habitual or duplicated hedging.

## P06 — Stock Persian opener

**Detect:** Generic openings such as «در دنیای امروز»، «در عصر حاضر»، «با پیشرفت روزافزون فناوری»، or a sweeping statement that delays the actual subject.

**Do not flag:** Historical framing that is specific and necessary.

**Rewrite:** Start with the concrete situation, event, or claim.

## P07 — Decorative intensifier

**Detect:** Repeated «بسیار»، «به‌شدت»، «قابل‌توجه»، «چشمگیر»، «ویژه»، «کلیدی» when no scale or reason is given.

**Do not flag:** A supported comparison or measured magnitude.

**Rewrite:** Remove the intensifier or replace it with the evidence already present.

## P08 — Imported English terminology without need

**Detect:** English terms inserted where a clear established Persian equivalent would be more natural and no technical precision is gained.

**Do not flag:** API names, product names, code terms, standard industry vocabulary, or cases where the English form is the clearer convention.

**Rewrite:** Prefer the natural term for the intended audience. Do not Persianize code or identifiers.
