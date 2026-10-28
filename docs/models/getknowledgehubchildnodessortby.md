# GetKnowledgeHubChildNodesSortBy

Field to sort results by. Omitted → default `updatedAt`.
Any other value is answered `400` ("Invalid sort_by: ...").


## Example Usage

```python
from pipeshub_sdk.models import GetKnowledgeHubChildNodesSortBy
value: GetKnowledgeHubChildNodesSortBy = "name"
```


## Values

- `"name"`
- `"createdAt"`
- `"updatedAt"`
- `"size"`
- `"type"`
