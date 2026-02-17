# SSEEvent

Server-Sent Event structure for streaming responses.<br><br>
<b>Event Types:</b>
<ul>
<li><code>connected</code> - Initial connection established</li>
<li><code>chunk</code> - Partial response content</li>
<li><code>citation</code> - Citation reference</li>
<li><code>complete</code> - Final response with all data</li>
<li><code>error</code> - Error occurred during streaming</li>
</ul>



## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `event`                                      | [Optional[models.Event]](../models/event.md) | :heavy_minus_sign:                           | N/A                                          |
| `data`                                       | *Optional[str]*                              | :heavy_minus_sign:                           | JSON-encoded event payload                   |