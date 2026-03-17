# RecordType

Type of content:
- FILE: Uploaded documents (PDF, DOCX, etc.)
- WEBPAGE: Web pages crawled or bookmarked
- COMMENT: Comments from collaboration tools
- MESSAGE: Chat/messaging content (Slack, Teams)
- EMAIL: Email messages (Gmail, Outlook)
- TICKET: Support tickets (Jira, ServiceNow)
- OTHERS: Miscellaneous content types


## Example Usage

```python
from pipeshub_sdk.models import RecordType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: RecordType = "FILE"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"FILE"`
- `"WEBPAGE"`
- `"COMMENT"`
- `"MESSAGE"`
- `"EMAIL"`
- `"TICKET"`
- `"OTHERS"`
