# BadRequestError

Bad request. Possible reasons:<br>
<ul>
<li>SMTP not configured properly (missing host, port, or fromEmail)</li>
<li>Invalid or unknown email template type</li>
<li>Missing required templateData fields for the selected template</li>
<li>Invalid email format in sendEmailTo or sendCcTo</li>
</ul>



## Fields

| Field                        | Type                         | Required                     | Description                  | Example                      |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `error`                      | *Optional[str]*              | :heavy_minus_sign:           | N/A                          | Smtp not configured properly |