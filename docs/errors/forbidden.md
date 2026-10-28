# Forbidden

Forbidden. Returned when the OAuth token is missing the required `kb:read` scope
(`ErrorResponse`), or as `{"error": "You do not have permission to access this record"}`
when the caller has no access to the record or the record is in the trash.



## Supported Types

### `errors.ErrorResponse`

```python
value: errors.ErrorResponse = /* values here */
```

### `errors.StreamRecordErrorResponse`

```python
value: errors.StreamRecordErrorResponse = /* values here */
```

