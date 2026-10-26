# AgentModelDefaultReasoningEffort

The model's own reasoning effort, read from its stored configuration. It applies only when the chat request sets no `reasoningEffort` and the agent has no `defaultReasoningEffort`. Omitted when nothing valid is stored; `none` is a legacy value that runs as `low`.

## Example Usage

```python
from pipeshub_sdk.models import AgentModelDefaultReasoningEffort

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AgentModelDefaultReasoningEffort = "none"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"none"`
- `"low"`
- `"medium"`
- `"high"`
- `"max"`
