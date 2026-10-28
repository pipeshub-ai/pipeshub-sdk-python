# AgentCreateKnowledgeFilters

The source's limit, as an object or its JSON text. An empty string or an empty
array means no limit. A non-empty array, `null`, or text that is not the JSON of
an object is refused with `400` (`VALIDATION_ERROR`, "Knowledge filters must be
an object, with recordGroups and records as lists of ids").



## Supported Types

### `models.AgentKnowledgeFiltersParsed`

```python
value: models.AgentKnowledgeFiltersParsed = /* values here */
```

### `str`

```python
value: str = /* values here */
```

### `List[Any]`

```python
value: List[Any] = /* values here */
```

