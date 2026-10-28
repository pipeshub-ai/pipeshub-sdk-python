# ChatAttachmentRefSource

How the attachment was produced: a file upload, or text pasted into the
composer and sent as a file. Stored on the saved message as sent.


## Example Usage

```python
from pipeshub_sdk.models import ChatAttachmentRefSource

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ChatAttachmentRefSource = "upload"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"upload"`
- `"paste-text"`
