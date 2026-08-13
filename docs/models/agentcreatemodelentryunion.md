# AgentCreateModelEntryUnion

Accepted model entry for `POST /agents/create`.
The gateway accepts either a non-empty string model entry or an object entry
with a required `modelKey`.

The `models` array itself is optional and may be empty (the agent then uses
the organization's default LLM). When the array is non-empty, it must include
at least one object entry with `isReasoning: true`. String-only entries are
schema-valid but, if present without any reasoning-flagged object entry, are
rejected at the gateway with HTTP 400.



## Supported Types

### `str`

```python
value: str = /* values here */
```

### `models.AgentCreateModelEntry`

```python
value: models.AgentCreateModelEntry = /* values here */
```

