# StageStateSummary

Status of one pipeline stage (e.g. `classify`) for the record's current
content revision.



## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           | Example                                               |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `stage`                                               | *str*                                                 | :heavy_check_mark:                                    | Pipeline stage name.                                  | classify                                              |
| `status`                                              | *str*                                                 | :heavy_check_mark:                                    | Stage status (same values as `indexingStatus`).       | COMPLETED                                             |
| `reason`                                              | *Nullable[str]*                                       | :heavy_check_mark:                                    | Failure or skip reason, when there is one.            |                                                       |
| `attempt`                                             | *int*                                                 | :heavy_check_mark:                                    | Number of times this stage has run for this revision. |                                                       |
| `started_at_ms`                                       | *Nullable[int]*                                       | :heavy_check_mark:                                    | N/A                                                   |                                                       |
| `finished_at_ms`                                      | *Nullable[int]*                                       | :heavy_check_mark:                                    | N/A                                                   |                                                       |
| `updated_at_ms`                                       | *Nullable[int]*                                       | :heavy_check_mark:                                    | N/A                                                   |                                                       |