# Credentials

Credentials based on the authentication method; the shape each method needs is
listed above. The validator only checks that this is a non-empty string or an
object whose `password`, `otp`, `token`, `code`, `accessToken` and `idToken`,
when present, are strings; other fields of the object are passed through. An
object without the field its method needs is refused later as a failed sign-in,
not as a validation error: `microsoft` without `idToken` answers `400`, and a Google
token that is not a JWT answers `500`.



## Supported Types

### `models.PasswordCredentials`

```python
value: models.PasswordCredentials = /* values here */
```

### `models.OtpCredentials`

```python
value: models.OtpCredentials = /* values here */
```

### `models.GoogleCredentials`

```python
value: models.GoogleCredentials = /* values here */
```

### `models.MicrosoftCredentials`

```python
value: models.MicrosoftCredentials = /* values here */
```

### `str`

```python
value: str = /* values here */
```

