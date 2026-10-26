# WebSearchProviderType

Supported web search provider. crawl4ai only reads pages (it backs up the built-in page reader) and cannot be the default; firecrawl both searches and reads pages. searxng, firecrawl and crawl4ai take a baseUrl; firecrawl defaults to its cloud API.

## Example Usage

```python
from pipeshub_sdk.models import WebSearchProviderType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: WebSearchProviderType = "duckduckgo"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"duckduckgo"`
- `"serper"`
- `"tavily"`
- `"exa"`
- `"brave"`
- `"searxng"`
- `"firecrawl"`
- `"crawl4ai"`
