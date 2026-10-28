# BadRequest

The grant is refused with the flat OAuth body `{ error, error_description }`:
- `invalid_request` - the body fails validation (`unsupported_grant_type` instead when
  `grant_type` is a non-empty string the schema does not accept)
- `invalid_grant` - `code`, `redirect_uri`, `refresh_token` or `device_code` missing,
  or an unknown, expired or already used authorization code. Also an authorization code
  or approved device code whose `knowledgeLimit` the app's current limit no longer
  contains, because the app's limit was narrowed after it was issued ("The
  application's permissions changed after you allowed it. Sign in again."). A widened
  limit does not refuse it; the token carries the limit the user agreed to. Also a
  `refresh_token` that another refresh presenting it at the same time rotated first
  ("Refresh token has already been used"); only one of them gets a new pair.
- `unsupported_grant_type` - the app does not have the grant
- `invalid_scope` - a requested scope is not allowed for the app, or the token would carry
  no scope at all ("A token must carry at least one scope"). A `client_credentials` grant
  drops `openid`, `profile`, `email` and `offline_access`, so it needs at least one other
  scope, requested or allowed for the app.
- `authorization_pending`, `slow_down`, `expired_token`, `access_denied` - device_code
  polling (RFC 8628 Section 3.5): still pending, polled sooner than `interval`, unknown,
  expired or already redeemed, or denied by the user. `access_denied` is a `400` here,
  not a `403`.
- `invalid_target`, `invalid_request`, `invalid_grant`, `invalid_scope`,
  `unsupported_grant_type` - a refusal from the token-exchange grant (see above)
- `server_error` - any other failure, also with status `400`. This includes an unknown or
  revoked `refresh_token` ("Invalid refresh token") and a `client_credentials` request
  without `client_secret`, whose `error_description` is the Node `TypeError` text
  (`The "data" argument must be of type string ... Received undefined`). A
  `client_credentials` grant whose identity is gone, disabled or being restored is also
  refused this way ("The identity this application acts as no longer exists", "... is
  disabled", "... is being restored. Try again once that has finished.").

Also returned, before authentication, when a query value, or any string in a JSON or form-encoded body, looks like markup to the app-wide XSS filter: an HTML tag, a script tag, `<iframe`, `<object`, `<embed` or `<svg` tag, a word starting with `on` followed by `=` (meant for inline event handlers such as `onerror=`, it also catches plain text such as `one=1`), a `javascript:` or `data:text/html` URL, an encoded script tag (`&lt;script`, `%3cscript`), or any string longer than 100,000 characters (`HTTP_BAD_REQUEST`, "HTML tags, scripts, and XSS content are not allowed in ...", naming the field or query parameter; a string over 100,000 characters is refused as too long instead). A JSON body that does not parse is refused the same way, also before authentication (`HTTP_BAD_REQUEST`, "The request body is not valid JSON.").



## Supported Types

### `errors.ErrorResponse`

```python
value: errors.ErrorResponse = /* values here */
```

### `errors.OAuthErrorResponse`

```python
value: errors.OAuthErrorResponse = /* values here */
```

