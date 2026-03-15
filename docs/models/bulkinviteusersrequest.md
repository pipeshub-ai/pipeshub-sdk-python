# BulkInviteUsersRequest

Request payload


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    | Example                                        |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `emails`                                       | List[*str*]                                    | :heavy_check_mark:                             | Array of email addresses to invite (max 100)   | [<br/>"user1@company.com",<br/>"user2@company.com"<br/>] |
| `group_ids`                                    | List[*str*]                                    | :heavy_minus_sign:                             | Optional group IDs to add all invited users to | [<br/>"507f1f77bcf86cd799439011"<br/>]         |
| `send_email`                                   | *Optional[bool]*                               | :heavy_minus_sign:                             | Whether to send invitation emails immediately  |                                                |