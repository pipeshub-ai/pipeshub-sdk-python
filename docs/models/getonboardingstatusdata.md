# GetOnboardingStatusData


## Fields

| Field                                  | Type                                   | Required                               | Description                            | Example                                |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `is_completed`                         | *Optional[bool]*                       | :heavy_minus_sign:                     | Whether onboarding is fully complete   | false                                  |
| `current_step`                         | *Optional[str]*                        | :heavy_minus_sign:                     | Current active onboarding step         | invite_team                            |
| `completed_steps`                      | List[*str*]                            | :heavy_minus_sign:                     | N/A                                    | [<br/>"org_profile",<br/>"admin_setup"<br/>] |
| `completion_percentage`                | *Optional[int]*                        | :heavy_minus_sign:                     | N/A                                    | 40                                     |
| `steps`                                | List[[models.Step](../models/step.md)] | :heavy_minus_sign:                     | N/A                                    |                                        |