# CreateAIModelsConfigRequest

AI models configuration. At least one model type array must contain entries.



## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `ocr`                                                                  | List[[models.AIModelConfiguration](../models/aimodelconfiguration.md)] | :heavy_minus_sign:                                                     | N/A                                                                    |
| `embedding`                                                            | List[[models.AIModelConfiguration](../models/aimodelconfiguration.md)] | :heavy_minus_sign:                                                     | N/A                                                                    |
| `llm`                                                                  | List[[models.AIModelConfiguration](../models/aimodelconfiguration.md)] | :heavy_minus_sign:                                                     | N/A                                                                    |
| `slm`                                                                  | List[[models.AIModelConfiguration](../models/aimodelconfiguration.md)] | :heavy_minus_sign:                                                     | N/A                                                                    |
| `reasoning`                                                            | List[[models.AIModelConfiguration](../models/aimodelconfiguration.md)] | :heavy_minus_sign:                                                     | N/A                                                                    |
| `multi_modal`                                                          | List[[models.AIModelConfiguration](../models/aimodelconfiguration.md)] | :heavy_minus_sign:                                                     | N/A                                                                    |
| `custom_system_prompt`                                                 | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | N/A                                                                    |