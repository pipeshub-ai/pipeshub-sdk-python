# AIModelConfigurationConfiguration

Provider-specific configuration


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `model`                                                    | *Optional[str]*                                            | :heavy_minus_sign:                                         | Model name(s) - can be comma-separated for multiple models | gpt-4o                                                     |
| `model_friendly_name`                                      | *Optional[str]*                                            | :heavy_minus_sign:                                         | Friendly display name for the model                        |                                                            |
| `api_key`                                                  | *Optional[str]*                                            | :heavy_minus_sign:                                         | API key for the model                                      |                                                            |
| `endpoint`                                                 | *Optional[str]*                                            | :heavy_minus_sign:                                         | Endpoint URL for the model                                 |                                                            |
| `deployment_name`                                          | *Optional[str]*                                            | :heavy_minus_sign:                                         | Azure deployment name                                      |                                                            |
| `region`                                                   | *Optional[str]*                                            | :heavy_minus_sign:                                         | AWS region                                                 |                                                            |