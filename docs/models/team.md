# Team


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Unique team identifier                                               |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | Team name                                                            |
| `description`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Team description                                                     |
| `org_id`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Organization ID                                                      |
| `user_roles`                                                         | List[[models.UserRole](../models/userrole.md)]                       | :heavy_minus_sign:                                                   | Users and their roles in the team                                    |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Creation timestamp (ISO 8601)                                        |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Last update timestamp (ISO 8601)                                     |