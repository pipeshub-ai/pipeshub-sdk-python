# StreamRecordBufferInternalServerError

Internal streaming failure, downstream conversion failure, or connector/backend
error proxied by the gateway.


A JSON body larger than 10 MB, or a form-encoded body larger than 100 KB or with more than 1000 fields, is answered `413` by the app-wide body parsers instead, also before authentication.



## Supported Types

### `errors.StreamRecordErrorResponse`

```python
value: errors.StreamRecordErrorResponse = /* values here */
```

### `errors.ErrorResponse`

```python
value: errors.ErrorResponse = /* values here */
```

