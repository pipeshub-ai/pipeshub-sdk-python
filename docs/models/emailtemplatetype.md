# EmailTemplateType

Type of email template to use. Each template has specific `templateData` requirements:
- `loginWithOTP`: OTP authentication email
- `resetPassword`: Password reset link email
- `accountCreation`: Welcome email for new organizations
- `appuserInvite`: Invitation email to join an organization
- `suspiciousLoginAttempt`: Security alert for multiple failed OTP attempts



## Values

| Name                       | Value                      |
| -------------------------- | -------------------------- |
| `LOGIN_WITH_OTP`           | loginWithOTP               |
| `RESET_PASSWORD`           | resetPassword              |
| `ACCOUNT_CREATION`         | accountCreation            |
| `APPUSER_INVITE`           | appuserInvite              |
| `SUSPICIOUS_LOGIN_ATTEMPT` | suspiciousLoginAttempt     |