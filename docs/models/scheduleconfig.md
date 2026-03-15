# ScheduleConfig

Schedule configuration for crawling jobs. The structure varies based on <code>scheduleType</code>.<br><br>
<b>Schedule Type Configurations:</b><br>
<ul>
<li><b>hourly:</b> <code>minute</code>, <code>interval</code> (optional)</li>
<li><b>daily:</b> <code>hour</code>, <code>minute</code></li>
<li><b>weekly:</b> <code>daysOfWeek</code>, <code>hour</code>, <code>minute</code></li>
<li><b>monthly:</b> <code>dayOfMonth</code>, <code>hour</code>, <code>minute</code></li>
<li><b>custom:</b> <code>cronExpression</code>, <code>description</code> (optional)</li>
<li><b>once:</b> <code>scheduledTime</code></li>
</ul>



## Supported Types

### `models.HourlyScheduleConfig`

```python
value: models.HourlyScheduleConfig = /* values here */
```

### `models.DailyScheduleConfig`

```python
value: models.DailyScheduleConfig = /* values here */
```

### `models.WeeklyScheduleConfig`

```python
value: models.WeeklyScheduleConfig = /* values here */
```

### `models.MonthlyScheduleConfig`

```python
value: models.MonthlyScheduleConfig = /* values here */
```

### `models.CustomScheduleConfig`

```python
value: models.CustomScheduleConfig = /* values here */
```

### `models.OnceScheduleConfig`

```python
value: models.OnceScheduleConfig = /* values here */
```

