# CreateTeamRequest

Request payload


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    | Example                                        |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `name`                                         | *str*                                          | :heavy_check_mark:                             | Team display name (must be unique in org)      | Engineering Team                               |
| `description`                                  | *Optional[str]*                                | :heavy_minus_sign:                             | Team description and purpose                   | Core engineering team for product development  |
| `user_roles`                                   | List[[models.UserRole](../models/userrole.md)] | :heavy_minus_sign:                             | Optional initial members with roles            |                                                |