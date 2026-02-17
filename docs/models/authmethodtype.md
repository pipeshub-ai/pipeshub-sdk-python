# AuthMethodType

Type of authentication method:
- `password`: Email/password authentication
- `otp`: One-time password via email (6-digit, expires in 10 minutes)
- `google`: Google OAuth 2.0
- `microsoft`: Microsoft OAuth 2.0
- `azureAd`: Azure Active Directory
- `samlSso`: SAML 2.0 Single Sign-On
- `oauth`: Generic OAuth 2.0 provider



## Values

| Name        | Value       |
| ----------- | ----------- |
| `SAML_SSO`  | samlSso     |
| `OTP`       | otp         |
| `PASSWORD`  | password    |
| `GOOGLE`    | google      |
| `MICROSOFT` | microsoft   |
| `AZURE_AD`  | azureAd     |
| `OAUTH`     | oauth       |