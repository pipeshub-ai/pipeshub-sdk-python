# AgentCreateModelEntryUnion

Accepted model entry for `POST /agents/create`.
The gateway accepts either a non-empty string model entry or an object entry
with a required `modelKey`.

The `models` array must include at least one object entry with `isReasoning: true`.
String-only entries are schema-valid but are rejected at the gateway with HTTP 400.



## Supported Types

### `str`

```python
value: str = /* values here */
```

### `models.AgentCreateModelEntry`

```python
value: models.AgentCreateModelEntry = /* values here */
```

