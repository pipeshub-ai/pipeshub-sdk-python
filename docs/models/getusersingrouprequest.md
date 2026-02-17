# GetUsersInGroupRequest


## Fields

| Field                                | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `group_id`                           | *str*                                | :heavy_check_mark:                   | Unique identifier of the user group  | 507f1f77bcf86cd799439011             |
| `page`                               | *Optional[int]*                      | :heavy_minus_sign:                   | Page number for pagination (1-based) |                                      |
| `limit`                              | *Optional[int]*                      | :heavy_minus_sign:                   | Number of users per page             |                                      |