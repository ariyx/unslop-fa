# Detect baseline — mixed-technical-001

Only the formulaic middle paragraph should be flagged. The surrounding technical prose is substantive and should be preserved.

## P06 — Stock Persian opener

> «در دنیای امروز، انتخاب درست دیتابیس و طراحی بهینه آن نقشی کلیدی در موفقیت محصولات نرم‌افزاری ایفا می‌کند.»

The opener is generic and portable; the concrete discussion before and after it already establishes the technical context.

**Revision direction:** remove the stock framing and move directly to the relevant technical constraint.

## C03 — Formulaic binary contrast

> «مسئله فقط performance نیست، بلکه ساخت سیستمی است که بتواند هم‌زمان سریع، پایدار و مقیاس‌پذیر باقی بماند.»

The «فقط X نیست، بلکه Y» frame adds rhetorical polish but no technical detail.

**Revision direction:** state the constraint directly or omit the sentence if the surrounding paragraphs already cover it.

## Preserve

Do not flag or rewrite the `EXPLAIN ANALYZE` sentence, the read/write caveat, or the point about composite-index column order. Those are informative technical constraints, not slop.
