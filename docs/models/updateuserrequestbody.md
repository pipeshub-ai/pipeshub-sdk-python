# UpdateUserRequestBody

Request payload


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `full_name`                                      | *Optional[str]*                                  | :heavy_minus_sign:                               | Full display name                                | John Smith                                       |
| `first_name`                                     | *Optional[str]*                                  | :heavy_minus_sign:                               | First name only                                  | John                                             |
| `last_name`                                      | *Optional[str]*                                  | :heavy_minus_sign:                               | Last name only                                   | Smith                                            |
| `email`                                          | *Optional[str]*                                  | :heavy_minus_sign:                               | Email address (admin only)                       | john.smith@company.com                           |
| `mobile`                                         | *Optional[str]*                                  | :heavy_minus_sign:                               | Mobile phone with country code                   | +15551234567                                     |
| `designation`                                    | *Optional[str]*                                  | :heavy_minus_sign:                               | Job title or role                                | Senior Software Engineer                         |
| `address`                                        | [Optional[models.Address]](../models/address.md) | :heavy_minus_sign:                               | N/A                                              |                                                  |