# UpdateConnectorAuthRequest

Request to update authentication config (clears OAuth tokens, requires re-auth)


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `auth`                                                         | [models.ConnectorAuthConfig](../models/connectorauthconfig.md) | :heavy_check_mark:                                             | Authentication configuration for a connector instance          |
| `base_url`                                                     | *Optional[str]*                                                | :heavy_minus_sign:                                             | Base URL (if changed with auth update)                         |