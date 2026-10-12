# AgentStreamSSEEventEvent

## Example Usage

```python
from pipeshub_sdk.models import AgentStreamSSEEventEvent

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AgentStreamSSEEventEvent = "RUN_STARTED"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"RUN_STARTED"`
- `"RUN_FINISHED"`
- `"RUN_ERROR"`
- `"STEP_STARTED"`
- `"STEP_FINISHED"`
- `"TEXT_MESSAGE_START"`
- `"TEXT_MESSAGE_CONTENT"`
- `"TEXT_MESSAGE_END"`
- `"REASONING_START"`
- `"REASONING_MESSAGE_START"`
- `"REASONING_MESSAGE_CONTENT"`
- `"REASONING_MESSAGE_END"`
- `"REASONING_END"`
- `"TOOL_CALL_START"`
- `"TOOL_CALL_ARGS"`
- `"TOOL_CALL_END"`
- `"TOOL_CALL_RESULT"`
- `"STATE_DELTA"`
- `"STATE_SNAPSHOT"`
- `"CUSTOM"`
- `"HEARTBEAT"`
