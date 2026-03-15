# RemoveUsersFromGroupRequest

Request payload


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 | Example                                     |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `group_ids`                                 | List[*str*]                                 | :heavy_check_mark:                          | Array of group IDs to remove users from     | [<br/>"507f1f77bcf86cd799439011"<br/>]      |
| `user_ids`                                  | List[*str*]                                 | :heavy_check_mark:                          | Array of user IDs to remove from the groups | [<br/>"507f1f77bcf86cd799439012"<br/>]      |