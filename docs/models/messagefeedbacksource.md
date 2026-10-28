# MessageFeedbackSource

Origin of the feedback. Always present in responses (server applies the default `user`).

## Example Usage

```python
from pipeshub_sdk.models import MessageFeedbackSource

# Open enum: unrecognized values are captured as UnrecognizedStr
value: MessageFeedbackSource = "user"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"user"`
- `"system"`
- `"admin"`
- `"auto"`
