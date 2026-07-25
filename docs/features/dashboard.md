# Dashboard

The Dashboard is a health summary, not the source of truth for a particular
concept. Use it to decide where investigation is needed.

## What it shows

The current implementation exposes:

- latest CIEL release information;
- active and retired concept totals;
- mapping totals and distribution by source;
- locale and translated-name coverage;
- concept and mapping trends;
- recent refresh state.

## Recommended use

1. Confirm that the displayed release and refresh timestamps are expected.
2. Look for abrupt changes in concept, mapping, or translation totals.
3. Follow a suspicious metric into the matching QA or tool page.
4. Refresh derived dashboard metrics only when the scheduled job is stale.

Dashboard data has a persisted projection and may fall back to live data. Small
timing differences during a refresh do not necessarily indicate data loss.

