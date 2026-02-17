# AppUserInviteTemplateData

Template data for user invitation email


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           | Example                                               |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `invitee`                                             | *str*                                                 | :heavy_check_mark:                                    | Name of the person who sent the invitation            | Admin User                                            |
| `org_name`                                            | *str*                                                 | :heavy_check_mark:                                    | Name of the organization the user is being invited to | Acme Corporation                                      |
| `link`                                                | *str*                                                 | :heavy_check_mark:                                    | Invitation acceptance URL with secure token           | https://app.pipeshub.com/invite?token=invite123abc    |