# GetRecordContentMode

`record` (default) reads this record. `thread` reads every record of the Slack thread this message belongs to, oldest first; a record outside any thread answers `422`.

## Example Usage

```python
from pipeshub_sdk.models import GetRecordContentMode
value: GetRecordContentMode = "record"
```


## Values

- `"record"`
- `"thread"`
