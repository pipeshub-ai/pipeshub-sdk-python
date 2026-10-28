# RedactedSource

Stands in for a source the viewer of a shared chat or search cannot read:
a citation, reference, filter node or search hit with no id, name, link or
text. Only the owner of a conversation or search sees every source.



## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `redacted`                             | *Literal[True]*                        | :heavy_check_mark:                     | N/A                                    |
| `reason`                               | [models.Reason](../models/reason.md)   | :heavy_check_mark:                     | N/A                                    |
| `name`                                 | *Optional[str]*                        | :heavy_minus_sign:                     | A neutral label (`Restricted source`). |