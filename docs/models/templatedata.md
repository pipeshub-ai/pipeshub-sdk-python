# TemplateData

Dynamic data to populate the email template. Required fields depend on <code>emailTemplateType</code>.<br><br>
<b>Template Data Requirements:</b><br>
<ul>
<li><b>loginWithOTP:</b> See <code>LoginWithOTPTemplateData</code> - requires <code>name</code>, <code>otp</code></li>
<li><b>resetPassword:</b> See <code>ResetPasswordTemplateData</code> - requires <code>name</code>, <code>link</code></li>
<li><b>accountCreation:</b> See <code>AccountCreationTemplateData</code> - requires <code>orgName</code>, <code>link</code></li>
<li><b>appuserInvite:</b> See <code>AppUserInviteTemplateData</code> - requires <code>invitee</code>, <code>orgName</code>, <code>link</code></li>
<li><b>suspiciousLoginAttempt:</b> See <code>SuspiciousLoginTemplateData</code> - requires <code>link</code></li>
</ul>



## Supported Types

### `models.LoginWithOTPTemplateData`

```python
value: models.LoginWithOTPTemplateData = /* values here */
```

### `models.ResetPasswordTemplateData`

```python
value: models.ResetPasswordTemplateData = /* values here */
```

### `models.AccountCreationTemplateData`

```python
value: models.AccountCreationTemplateData = /* values here */
```

### `models.AppUserInviteTemplateData`

```python
value: models.AppUserInviteTemplateData = /* values here */
```

### `models.SuspiciousLoginTemplateData`

```python
value: models.SuspiciousLoginTemplateData = /* values here */
```

