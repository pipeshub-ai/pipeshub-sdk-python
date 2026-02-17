# User

User account in an organization


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `id`                                             | *Optional[str]*                                  | :heavy_minus_sign:                               | Unique user identifier (MongoDB ObjectId)        |
| `slug`                                           | *Optional[str]*                                  | :heavy_minus_sign:                               | Unique slug for the user                         |
| `org_id`                                         | *str*                                            | :heavy_check_mark:                               | Organization ID the user belongs to              |
| `full_name`                                      | *Optional[str]*                                  | :heavy_minus_sign:                               | Full name of the user                            |
| `first_name`                                     | *Optional[str]*                                  | :heavy_minus_sign:                               | First name                                       |
| `last_name`                                      | *Optional[str]*                                  | :heavy_minus_sign:                               | Last name                                        |
| `middle_name`                                    | *Optional[str]*                                  | :heavy_minus_sign:                               | Middle name                                      |
| `email`                                          | *str*                                            | :heavy_check_mark:                               | Email address (unique, lowercase)                |
| `mobile`                                         | *Optional[str]*                                  | :heavy_minus_sign:                               | Mobile number (10-15 digits with optional +)     |
| `has_logged_in`                                  | *Optional[bool]*                                 | :heavy_minus_sign:                               | Whether user has logged in at least once         |
| `designation`                                    | *Optional[str]*                                  | :heavy_minus_sign:                               | Job title/designation                            |
| `address`                                        | [Optional[models.Address]](../models/address.md) | :heavy_minus_sign:                               | N/A                                              |
| `data_collection_consent`                        | *Optional[bool]*                                 | :heavy_minus_sign:                               | Whether user has consented to data collection    |
| `is_deleted`                                     | *Optional[bool]*                                 | :heavy_minus_sign:                               | Soft delete flag                                 |
| `deleted_by`                                     | *Optional[str]*                                  | :heavy_minus_sign:                               | ID of user who deleted this user                 |
| `created_at`                                     | *Optional[int]*                                  | :heavy_minus_sign:                               | Creation timestamp (milliseconds since epoch)    |
| `updated_at`                                     | *Optional[int]*                                  | :heavy_minus_sign:                               | Last update timestamp (milliseconds since epoch) |