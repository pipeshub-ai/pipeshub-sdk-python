# ConnectorAuthConfig

Authentication configuration for a connector instance


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `values`                                                       | Dict[str, *Any*]                                               | :heavy_minus_sign:                                             | Authentication values (keys depend on connector's auth schema) | {<br/>"apiKey": "sk-xxxxx",<br/>"baseUrl": "https://api.example.com"<br/>} |
| `oauth_config_id`                                              | *Optional[str]*                                                | :heavy_minus_sign:                                             | ID of admin-created OAuth configuration to use                 | oauth_config_123                                               |
| `custom_values`                                                | Dict[str, *Any*]                                               | :heavy_minus_sign:                                             | Custom authentication values specific to the connector         |                                                                |