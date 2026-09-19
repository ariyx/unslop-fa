# technical-001 — Detect baseline

Genre: technical

This baseline records style patterns that are worth editing while explicitly protecting technical qualifiers, terminology, and examples that carry information.

| Rule | Passage | Why it is a problem here | Revision direction |
| --- | --- | --- | --- |
| C03 — Formulaic binary contrast | «بنابراین سؤال اصلی این نیست که «کدام دیتابیس بهتر است؟»، بلکه این است که...» | The distinction is useful, but the staged «X نیست، بلکه Y است» frame is a reusable rhetorical template rather than necessary technical structure. | State the actual decision criteria directly. |
| C05 — Canned transition | Repeated openers such as «در عمل»، «با این حال»، «البته»، «در مقابل» and «در نهایت» | Several connectors merely announce a contrast or conclusion already clear from the surrounding comparison. | Remove only redundant connectors; keep those that prevent an actual logical jump. |
| P05 — Habitual modal stacking | Repeated «معمولاً»، «می‌تواند»، «ممکن است» and «احتمالاً» across descriptive paragraphs | Some qualifiers are necessary because performance and scaling are workload-dependent, but others are habitual hedging around ordinary descriptive claims. | Preserve uncertainty where the claim truly depends on workload, future needs, or deployment context; make settled descriptive claims more direct. |
| C11 — Summary-recap ending | The conclusion repeats the same MySQL-for-common-web-workloads / PostgreSQL-for-richer-data-needs distinction already developed in the body. | The conclusion spends several paragraphs re-running the comparison before reaching the practical decision criteria. | Compress the recap and keep the concrete selection criteria. |
| C10 — Aphoristic or fake-profound ending | «در نهایت، معماری صحیح schema، indexگذاری مناسب، monitoring و طراحی درست queryها معمولاً تأثیر بسیار بیشتری بر موفقیت پروژه دارند تا نام دیتابیسی که انتخاب شده است.» | The point is useful, but as the final standalone sentence it reads like a universal maxim and overstates a context-dependent comparison. | Tie the point back to early-stage startup selection and retain the concrete factors instead of ending on a slogan-like generalization. |

## Safeguards

The edit must preserve these substantive technical points even when their wording resembles common AI patterns:

- **T01 — Caveats:** Keep the statement that PostgreSQL/MySQL performance cannot be compared meaningfully without a workload, and keep the context-dependence of scaling, cost, and operational complexity.
- **T02 — Terminology:** Keep stable technical naming such as `query`, `schema`, `index`, `workload`, `replication`, `sharding`, `JSONB`, `transaction`, `constraint`, and `managed database` where it is natural for the intended audience.
- **T03 — Named technologies:** Do not alter names such as PostgreSQL, MySQL, InnoDB, BigQuery, Snowflake, ClickHouse, and PostGIS.
- **T04 — Informative comparisons:** Do not remove the workload caveat or flatten the differences around JSONB, complex queries, data integrity, replication, or team experience.
- **T05 — Examples:** Keep examples that explain why a feature matters, including product attributes in JSONB and SaaS analytics queries.
- **T06 — Technical register:** Do not force Persian equivalents where they make the text less precise or less natural for a technical reader.

## Non-findings

The following should **not** be flagged merely for looking structured:

- the six decision questions near the end; they form a useful checklist rather than ornamental symmetry;
- the performance caveat in the first paragraph of the Performance section;
- the note that large-scale analytics may move to BigQuery, Snowflake, or ClickHouse;
- the statement that team familiarity can reduce operational risk.
