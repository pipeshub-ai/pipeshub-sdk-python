# UpdateOnboardingStatusResponse

Onboarding status updated successfully


## Fields

| Field                                  | Type                                   | Required                               | Description                            | Example                                |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `success`                              | *Optional[bool]*                       | :heavy_minus_sign:                     | N/A                                    | true                                   |
| `message`                              | *Optional[str]*                        | :heavy_minus_sign:                     | N/A                                    | Step 'invite_team' marked as complete  |
| `is_onboarding_complete`               | *Optional[bool]*                       | :heavy_minus_sign:                     | Whether all onboarding is now complete | false                                  |
| `next_step`                            | *Optional[str]*                        | :heavy_minus_sign:                     | Next step to complete (null if done)   | connect_integrations                   |