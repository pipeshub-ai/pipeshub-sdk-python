# ExpiryDays

Token lifetime. Defaults to `30` if omitted — a token minted
without an explicit choice shouldn't default to the longest
lifetime. `"never"` is stored as a ~100-year expiry (the
underlying schema field is required and TTL-indexed, so there's
no literal null option).



## Supported Types

### `models.ExpiryDaysEnum`

```python
value: models.ExpiryDaysEnum = /* values here */
```

### `models.ExpiryDaysNever`

```python
value: models.ExpiryDaysNever = /* values here */
```

