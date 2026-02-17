# OrgAuthConfigCreateRequest

Request to create initial organization auth configuration


## Fields

| Field                         | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `contact_email`               | *str*                         | :heavy_check_mark:            | Organization contact email    |
| `registered_name`             | *str*                         | :heavy_check_mark:            | Organization registered name  |
| `admin_full_name`             | *str*                         | :heavy_check_mark:            | Admin user full name          |
| `send_email`                  | *Optional[bool]*              | :heavy_minus_sign:            | Whether to send welcome email |