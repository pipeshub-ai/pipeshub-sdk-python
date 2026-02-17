# UpdateOnboardingStatusRequest

Request payload


## Fields

| Field                                | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `step_id`                            | *str*                                | :heavy_check_mark:                   | ID of the step to update             | invite_team                          |
| `action`                             | [models.Action](../models/action.md) | :heavy_check_mark:                   | Action to perform on the step        | complete                             |