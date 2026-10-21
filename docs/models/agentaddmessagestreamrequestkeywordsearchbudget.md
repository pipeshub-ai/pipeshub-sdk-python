# AgentAddMessageStreamRequestKeywordSearchBudget

How long each search waits for the keyword (grep) match after its semantic results are in. `short` waits at most 5 seconds and keeps the keyword matches found by then, for callers that would rather answer sooner, such as agents calling chat over MCP. `full`, or leaving it out, waits for all of it. Deployments running `HIGH_ACCURACY_MODE` always wait in full.

## Example Usage

```python
from pipeshub_sdk.models import AgentAddMessageStreamRequestKeywordSearchBudget
value: AgentAddMessageStreamRequestKeywordSearchBudget = "short"
```


## Values

- `"short"`
- `"full"`
