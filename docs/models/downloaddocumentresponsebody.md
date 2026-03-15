# DownloadDocumentResponseBody

Download URL generated or file stream


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       | Example                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `success`                                                         | *Optional[bool]*                                                  | :heavy_minus_sign:                                                | N/A                                                               | true                                                              |
| `signed_url`                                                      | *Optional[str]*                                                   | :heavy_minus_sign:                                                | Presigned URL for download (S3/Azure only)                        | https://bucket.s3.amazonaws.com/docs/file.pdf?X-Amz-Signature=... |