# State

Current state of the job in the queue:<br>
<ul>
<li><b>waiting</b>: Queued and waiting to be processed</li>
<li><b>active</b>: Currently being processed by a worker</li>
<li><b>completed</b>: Successfully finished</li>
<li><b>failed</b>: Failed after all retry attempts</li>
<li><b>delayed</b>: Scheduled to run at a future time</li>
<li><b>paused</b>: Manually paused by user</li>
<li><b>stuck</b>: Job is stuck (worker crashed mid-processing)</li>
</ul>


## Example Usage

```python
from pipeshub_sdk.models import State

# Open enum: unrecognized values are captured as UnrecognizedStr
value: State = "waiting"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"waiting"`
- `"active"`
- `"completed"`
- `"failed"`
- `"delayed"`
- `"paused"`
- `"stuck"`
