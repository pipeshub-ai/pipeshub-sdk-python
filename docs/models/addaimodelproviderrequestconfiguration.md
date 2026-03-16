# AddAIModelProviderRequestConfiguration

Provider-specific configuration. Required fields vary by provider:<br>
<ul>
<li><b>OpenAI/Anthropic/Cohere/etc:</b> model, apiKey</li>
<li><b>Azure OpenAI:</b> model, apiKey, endpoint, deploymentName</li>
<li><b>AWS Bedrock:</b> model, awsAccessKeyId, awsAccessSecretKey, region</li>
<li><b>Ollama/self-hosted:</b> model, endpoint</li>
</ul>



## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `model`                                                                | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Model name/identifier                                                  | gpt-4o                                                                 |
| `api_key`                                                              | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | API key for the provider                                               | sk-example-key                                                         |
| `endpoint`                                                             | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Custom endpoint URL (for Azure, self-hosted)                           |                                                                        |
| `organization_id`                                                      | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Organization ID (OpenAI)                                               |                                                                        |
| `deployment_name`                                                      | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Deployment name (Azure OpenAI)                                         |                                                                        |
| `aws_access_key_id`                                                    | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | AWS access key (Bedrock). Optional - omit to use IAM role credentials. |                                                                        |
| `aws_access_secret_key`                                                | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | AWS secret key (Bedrock). Optional - omit to use IAM role credentials. |                                                                        |
| `region`                                                               | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | AWS region (Bedrock)                                                   |                                                                        |