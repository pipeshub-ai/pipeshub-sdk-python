# AgentKnowledgeFilters

Knowledge scope filter as stored on the graph edge. The Node `getAgent`
handler proxies this field unchanged from the AI service (only `agent.id`
is stripped). May be a JSON string (typical graph storage) or an object.
Prefer `filtersParsed` on GET for a guaranteed parsed object with the
same keys as the object branch below.



## Supported Types

### `models.AgentKnowledgeFiltersParsed`

```python
value: models.AgentKnowledgeFiltersParsed = /* values here */
```

### `str`

```python
value: str = /* values here */
```

