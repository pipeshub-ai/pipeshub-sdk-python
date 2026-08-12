# RevokePatRequest

Optional request body for `DELETE /personal-access-tokens/{tokenId}`
and `DELETE /personal-access-tokens/admin/{tokenId}`. The body itself
is optional; `reason`, if present, is stored on the revocation for
auditing.



## Fields

| Field              | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `reason`           | *Optional[str]*    | :heavy_minus_sign: | N/A                | rotated            |