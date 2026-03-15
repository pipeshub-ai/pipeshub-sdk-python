# UpdateOrganizationRequest

Request payload


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `registered_name`                                | *Optional[str]*                                  | :heavy_minus_sign:                               | Official registered/legal name                   | Acme Corporation Inc.                            |
| `short_name`                                     | *Optional[str]*                                  | :heavy_minus_sign:                               | Short display name for UI                        | Acme Corp                                        |
| `phone_number`                                   | *Optional[str]*                                  | :heavy_minus_sign:                               | Contact phone number (international format)      | +15551234567                                     |
| `permanent_address`                              | [Optional[models.Address]](../models/address.md) | :heavy_minus_sign:                               | N/A                                              |                                                  |