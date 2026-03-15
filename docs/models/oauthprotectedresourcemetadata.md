# OAuthProtectedResourceMetadata

OAuth Protected Resource Metadata (RFC 9728).
Describes the protected resource, its authorization servers, supported scopes, and bearer token methods.



## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   | Example                                                       |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `resource`                                                    | *str*                                                         | :heavy_check_mark:                                            | Protected resource identifier                                 |                                                               |
| `authorization_servers`                                       | List[*str*]                                                   | :heavy_check_mark:                                            | Authorization servers that can issue tokens for this resource |                                                               |
| `scopes_supported`                                            | List[*str*]                                                   | :heavy_minus_sign:                                            | OAuth scopes supported by this resource                       | [<br/>"read:records",<br/>"write:records",<br/>"admin:connectors"<br/>] |
| `bearer_methods_supported`                                    | List[*str*]                                                   | :heavy_minus_sign:                                            | Methods supported for sending bearer tokens                   | [<br/>"header"<br/>]                                          |
| `resource_documentation`                                      | *Optional[str]*                                               | :heavy_minus_sign:                                            | URL to human-readable documentation for the resource          |                                                               |