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

Hover over a legend entry in the concept and mapping trends or **Mappings by
reference source** chart to emphasize that series and dim the others. Move the
pointer away to restore all series. This interaction depends on the deployed
application version.

Dashboard data has a persisted projection and may fall back to live data. Small
timing differences during a refresh do not necessarily indicate data loss.

## Public statistics and locale coverage

The public statistics endpoint used by the wiki is anonymous and cacheable. Its
figures separate active from retired concepts and mappings, so a total is not a
claim that every record is current or active. Public badge values can therefore
lag a completed change briefly; refresh the source application before treating a
cached figure as an operational discrepancy.

Locale coverage is derived from translated-content rows and is capped at 100%.
It is not the count of configured locales and it is not a clinical-quality score.
Use it to identify where translation review may be needed, then inspect the
source/version and the corresponding concepts before drawing a conclusion.

