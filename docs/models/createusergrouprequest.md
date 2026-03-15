# CreateUserGroupRequest

Request payload


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `name`                                                         | *str*                                                          | :heavy_check_mark:                                             | Display name for the group                                     | Engineering Team                                               |
| `type`                                                         | [models.CreateUserGroupType](../models/createusergrouptype.md) | :heavy_check_mark:                                             | Group type determining behavior and privileges                 | standard                                                       |
| `description`                                                  | *Optional[str]*                                                | :heavy_minus_sign:                                             | Optional description of the group's purpose                    | All engineering department members                             |