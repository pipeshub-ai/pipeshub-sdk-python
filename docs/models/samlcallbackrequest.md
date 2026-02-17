# SamlCallbackRequest

Request payload


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `saml_response`                                | *str*                                          | :heavy_check_mark:                             | Base64-encoded SAML Response from IDP          |
| `relay_state`                                  | *Optional[str]*                                | :heavy_minus_sign:                             | State parameter containing session information |