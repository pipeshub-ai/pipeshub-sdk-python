# AgentCreateResponseAgentDefaultReasoningEffort

Agent-level reasoning effort used when a chat request omits its own. Null when unset.

## Example Usage

```python
from pipeshub_sdk.models import AgentCreateResponseAgentDefaultReasoningEffort

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AgentCreateResponseAgentDefaultReasoningEffort = "none"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"none"`
- `"low"`
- `"medium"`
- `"high"`
- `"max"`
