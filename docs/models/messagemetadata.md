# MessageMetadata


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `processing_time_ms`                            | *Optional[float]*                               | :heavy_minus_sign:                              | Time taken to generate response in milliseconds |
| `model_version`                                 | *Optional[str]*                                 | :heavy_minus_sign:                              | Version of the AI model used                    |
| `ai_transaction_id`                             | *Optional[str]*                                 | :heavy_minus_sign:                              | Transaction ID for tracking in AI backend       |
| `reason`                                        | *Optional[str]*                                 | :heavy_minus_sign:                              | Additional context or reasoning                 |