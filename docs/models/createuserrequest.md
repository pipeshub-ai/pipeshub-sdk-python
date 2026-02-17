# CreateUserRequest

Request payload


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  | Example                                      |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `full_name`                                  | *str*                                        | :heavy_check_mark:                           | User's full display name                     | John Smith                                   |
| `email`                                      | *str*                                        | :heavy_check_mark:                           | User's email address (must be unique)        | john.smith@company.com                       |
| `mobile`                                     | *Optional[str]*                              | :heavy_minus_sign:                           | Mobile phone number with country code        | +15551234567                                 |
| `designation`                                | *Optional[str]*                              | :heavy_minus_sign:                           | Job title or designation                     | Software Engineer                            |
| `send_invite`                                | *Optional[bool]*                             | :heavy_minus_sign:                           | Whether to send invitation email immediately |                                              |