# SamlSignInCallbackRequest

SAML response from Identity Provider


## Fields

| Field                                 | Type                                  | Required                              | Description                           |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `saml_response`                       | *Optional[str]*                       | :heavy_minus_sign:                    | Base64-encoded SAML response          |
| `relay_state`                         | *Optional[str]*                       | :heavy_minus_sign:                    | Relay state from the original request |