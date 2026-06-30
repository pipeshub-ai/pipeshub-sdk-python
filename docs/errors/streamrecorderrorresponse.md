# StreamRecordErrorResponse

Error payload returned by the legacy record-stream proxy when the downstream
streaming request fails after route middleware has passed.



## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `error`                                                                    | *str*                                                                      | :heavy_check_mark:                                                         | Human-readable error message from the gateway or downstream stream service |