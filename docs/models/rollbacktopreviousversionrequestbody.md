# RollBackToPreviousVersionRequestBody

Request payload


## Fields

| Field                                                     | Type                                                      | Required                                                  | Description                                               | Example                                                   |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `version`                                                 | *str*                                                     | :heavy_check_mark:                                        | Version number to rollback to (0-indexed)                 | 2                                                         |
| `note`                                                    | *str*                                                     | :heavy_check_mark:                                        | Reason for rollback (required for audit trail)            | Reverting to version 2 due to incorrect data in version 3 |