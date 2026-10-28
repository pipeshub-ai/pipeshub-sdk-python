# GetRecordContentExtract

With `query`, in record mode and without `startBlock`: return only the passages that answer `query`, as the model assigned to the `reader` role (else the default model) copies them out, instead of the record's text. The model is told to copy word for word, and `extract.unverifiedLines` counts the lines it did not. The response's `order` is `extract`, and its `extract` object names the model and the tokens it used. When the model cannot be reached, the usual read is returned with `extract.error` set.

## Example Usage

```python
from pipeshub_sdk.models import GetRecordContentExtract
value: GetRecordContentExtract = "true"
```


## Values

- `"true"`
- `"false"`
