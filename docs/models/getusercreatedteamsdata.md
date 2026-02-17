# GetUserCreatedTeamsData


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `team`                                                               | [Optional[models.Team]](../models/team.md)                           | :heavy_minus_sign:                                                   | N/A                                                                  |
| `current_role`                                                       | [Optional[models.CurrentRole]](../models/currentrole.md)             | :heavy_minus_sign:                                                   | User's current role (none if no longer a member)                     |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |