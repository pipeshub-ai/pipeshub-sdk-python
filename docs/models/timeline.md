# Timeline

Search a span of time period by period instead of ranking matches over the whole
span, for questions such as "how did this evolve" or "what changed between March
and May". A plain search returns the best matches overall, which bunch around one
moment; a timeline splits the span into up to 6 periods (calendar months, or weeks
within one month), searches each period on its own and beside one search of the
whole span, and returns the matches in date order, each labelled with its period.

The value is the date records are placed by: `created` (when the record was
created at its source) or `modified` (its last change). The span is that date's
bounds (`createdAfter` / `createdBefore`, or `modifiedAfter` / `modifiedBefore`);
with no start it covers the year before the end, or further back to the earliest
of the best matches. Bounds on the other date apply to every period. `limit` is the
number of matches each period's own search asks for; matches from
the search of the whole span (up to 50) are added to the periods their records are
dated in, so a period can hold more than `limit`. Each search applies the same permissions
and filters as a plain search.

Left out, a search whose bounds on one date have a start and cover more than 31
days (a missing end is today) runs as a timeline on that date, and
`timeline.automatic` is `true`; any other search is a plain ranked search. `off`
is always a plain ranked search. A server whose `TIMELINE_SUMMARIES` setting is
`false` ignores the field and never runs a timeline.


## Example Usage

```python
from pipeshub_sdk.models import Timeline
value: Timeline = "created"
```


## Values

- `"created"`
- `"modified"`
- `"off"`
