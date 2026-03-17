# UpdateAIModelProviderRequestConfiguration

Provider-specific configuration. Keys vary by provider.


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `model`                                      | *Optional[str]*                              | :heavy_minus_sign:                           | Model name/identifier                        |
| `api_key`                                    | *Optional[str]*                              | :heavy_minus_sign:                           | API key for the provider                     |
| `model_friendly_name`                        | *Optional[str]*                              | :heavy_minus_sign:                           | Human-readable display name for the model    |
| `endpoint`                                   | *Optional[str]*                              | :heavy_minus_sign:                           | Custom endpoint URL (for Azure, self-hosted) |
| `__pydantic_extra__`                         | Dict[str, *Any*]                             | :heavy_minus_sign:                           | N/A                                          |