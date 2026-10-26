# UpdateOAuthConfigConfig2

OAuth app fields to change, merged over the saved ones. Keys follow
the connector type's OAuth fields; a masked secret sent back as
returned is ignored, so the saved value is kept.



## Fields

| Field                | Type                 | Required             | Description          |
| -------------------- | -------------------- | -------------------- | -------------------- |
| `client_id`          | *Optional[str]*      | :heavy_minus_sign:   | N/A                  |
| `client_secret`      | *Optional[str]*      | :heavy_minus_sign:   | N/A                  |
| `tenant_id`          | *Optional[str]*      | :heavy_minus_sign:   | N/A                  |
| `__pydantic_extra__` | Dict[str, *Any*]     | :heavy_minus_sign:   | N/A                  |