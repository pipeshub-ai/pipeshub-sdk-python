# AuthConfig

Organization authentication configuration. Supports 1-3 authentication steps for multi-factor authentication.
**Validation Rules:**
- Minimum 1 step, maximum 3 steps
- Each step must have unique order
- No duplicate methods within the same step
- No method can appear in multiple steps



## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `auth_methods`                                 | List[[models.AuthStep](../models/authstep.md)] | :heavy_check_mark:                             | List of authentication steps in order          |