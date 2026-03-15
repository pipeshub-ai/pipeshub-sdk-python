# Jwk

JSON Web Key (RFC 7517).
Public key for verifying JWT signatures.



## Fields

| Field                            | Type                             | Required                         | Description                      | Example                          |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `kty`                            | *Optional[str]*                  | :heavy_minus_sign:               | Key type                         | RSA                              |
| `use`                            | *Optional[str]*                  | :heavy_minus_sign:               | Key use (sig = signature)        | sig                              |
| `alg`                            | *Optional[str]*                  | :heavy_minus_sign:               | Algorithm                        | RS256                            |
| `kid`                            | *Optional[str]*                  | :heavy_minus_sign:               | Key ID                           |                                  |
| `n`                              | *Optional[str]*                  | :heavy_minus_sign:               | RSA modulus (base64url encoded)  |                                  |
| `e`                              | *Optional[str]*                  | :heavy_minus_sign:               | RSA exponent (base64url encoded) | AQAB                             |