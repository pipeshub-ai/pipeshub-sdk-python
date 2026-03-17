# AIModelProviderConfigConfiguration

Provider-specific configuration. Keys vary by provider (e.g., ollama includes endpoint).


## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `model`                                   | *Optional[str]*                           | :heavy_minus_sign:                        | Model name(s)                             |
| `api_key`                                 | *Optional[str]*                           | :heavy_minus_sign:                        | API key for the model                     |
| `endpoint`                                | *Optional[str]*                           | :heavy_minus_sign:                        | Endpoint URL for the model                |
| `model_friendly_name`                     | *Optional[str]*                           | :heavy_minus_sign:                        | Human-readable display name for the model |
| `__pydantic_extra__`                      | Dict[str, *Any*]                          | :heavy_minus_sign:                        | N/A                                       |