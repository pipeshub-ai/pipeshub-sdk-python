# ReferenceDataItem

A reference to an external resource associated with a message


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `name`                                                                       | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Display name of the referenced item                                          |
| `id`                                                                         | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Unique identifier of the referenced item                                     |
| `type`                                                                       | [Optional[models.ReferenceDataItemType]](../models/referencedataitemtype.md) | :heavy_minus_sign:                                                           | Type of the referenced item                                                  |
| `key`                                                                        | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Key identifier (e.g., Jira project key, Confluence space key)                |
| `account_id`                                                                 | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Account ID associated with the reference                                     |
| `url`                                                                        | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | Direct URL to the referenced item                                            |