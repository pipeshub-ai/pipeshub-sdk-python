# AgentDefaultReasoningEffort

Agent-level reasoning effort used when a chat request omits its own. Null when unset.

## Example Usage

```python
from pipeshub_sdk.models import AgentDefaultReasoningEffort

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AgentDefaultReasoningEffort = "none"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"none"`
- `"low"`
- `"medium"`
- `"high"`
- `"max"`
