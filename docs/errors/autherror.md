# AuthError

Authentication error response with details for debugging and user feedback.<br><br>
<b>Common Error Codes:</b><br>
<ul>
<li><code>HTTP_UNAUTHORIZED</code> - Invalid session or token</li>
<li><code>HTTP_BAD_REQUEST</code> - Invalid request data</li>
<li><code>HTTP_NOT_FOUND</code> - Resource not found</li>
</ul>



## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `error`                                                        | [Optional[models.AuthErrorError]](../models/autherrorerror.md) | :heavy_minus_sign:                                             | Error details                                                  |