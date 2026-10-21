# ResyncConnectorConflict

Conflict. Possible reasons:<br>
<ul>
<li>A sync is already running, or the connector is locked</li>
<li><code>DESKTOP_OFFLINE</code> - Local FS: the owner device's desktop app is not connected</li>
<li><code>DESKTOP_UNCLAIMED</code> - Local FS: no device owns the connector yet</li>
</ul>
Local FS refusals carry <code>details.code</code> and use the
LocalFsDesktopRefusal body; the others use the standard error body.



## Supported Types

### `errors.LocalFsDesktopRefusalError`

```python
value: errors.LocalFsDesktopRefusalError = /* values here */
```

### `errors.ErrorResponse`

```python
value: errors.ErrorResponse = /* values here */
```

