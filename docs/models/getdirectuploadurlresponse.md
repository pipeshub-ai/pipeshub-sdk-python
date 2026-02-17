# GetDirectUploadURLResponse

Direct upload URL generated successfully


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       | Example                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `success`                                                         | *Optional[bool]*                                                  | :heavy_minus_sign:                                                | N/A                                                               | true                                                              |
| `signed_url`                                                      | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Presigned URL for direct PUT upload                               | https://bucket.s3.amazonaws.com/path/file.pdf?X-Amz-Signature=... |
| `document_id`                                                     | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Document ID for reference                                         | 507f1f77bcf86cd799439011                                          |