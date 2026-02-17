# SendEmailInternalServerError

Internal server error. Email sending failed due to:<br>
<ul>
<li>SMTP server connection failure</li>
<li>Authentication failure with SMTP server</li>
<li>Template compilation error</li>
<li>Network issues</li>
</ul>



## Fields

| Field                | Type                 | Required             | Description          | Example              |
| -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| `error`              | *Optional[str]*      | :heavy_minus_sign:   | N/A                  | Failed to send email |