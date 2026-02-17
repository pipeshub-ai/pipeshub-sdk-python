# AddAIModelProviderRequestConfiguration

Provider-specific configuration


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  | Example                                      |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `model`                                      | *Optional[str]*                              | :heavy_minus_sign:                           | Model name/identifier                        | gpt-4                                        |
| `api_key`                                    | *Optional[str]*                              | :heavy_minus_sign:                           | API key for the provider                     |                                              |
| `endpoint`                                   | *Optional[str]*                              | :heavy_minus_sign:                           | Custom endpoint URL (for Azure, self-hosted) |                                              |
| `organization_id`                            | *Optional[str]*                              | :heavy_minus_sign:                           | Organization ID (OpenAI)                     |                                              |
| `deployment_name`                            | *Optional[str]*                              | :heavy_minus_sign:                           | Deployment name (Azure OpenAI)               |                                              |
| `aws_access_key_id`                          | *Optional[str]*                              | :heavy_minus_sign:                           | AWS access key (Bedrock)                     |                                              |
| `aws_access_secret_key`                      | *Optional[str]*                              | :heavy_minus_sign:                           | AWS secret key (Bedrock)                     |                                              |
| `region`                                     | *Optional[str]*                              | :heavy_minus_sign:                           | AWS region (Bedrock)                         |                                              |