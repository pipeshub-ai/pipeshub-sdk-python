# ResetPasswordTemplateData

Template data for password reset email


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `name`                                                  | *str*                                                   | :heavy_check_mark:                                      | User's display name shown in the email greeting         | John Doe                                                |
| `link`                                                  | *str*                                                   | :heavy_check_mark:                                      | Password reset URL with secure token                    | https://app.pipeshub.com/reset-password?token=abc123xyz |