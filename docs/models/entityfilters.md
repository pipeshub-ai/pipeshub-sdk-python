# EntityFilters

**Experimental** named-entity constraints (Labs flag `ENABLE_NAMED_ENTITY_EXTRACTION`, or `HIGH_ACCURACY_MODE`).
Every constraint must hold for the same record: an amount and a date match a record
that mentions both, not one entity that is both. `name`/`entityIds` match entity nodes;
`mentionedDate`, `amount`, `quantity` and `percent` match typed values the record
mentions (any date mentioned, not a role such as "signed on"). A kind of a typed
constraint's own kind narrows it (`currency` with `amount`); other kinds are a
constraint of their own. Only records the caller may read are considered: every empty
result reads the same.

An unusable filter (unknown kind, bad currency, a range whose low end is above its high
end, or a blank name) fails request validation with 400, including on conversation
requests. On `POST /search`, a valid filter matching too many readable records is
refused with 422. Conversation operations apply a valid filter to every search behind
the answer; if retrieval refuses it, the request does not fail and the answer says why
the filter could not be applied.



## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `kinds`                                                                                                | List[[models.NamedEntityKind](../models/namedentitykind.md)]                                           | :heavy_minus_sign:                                                                                     | Lowercase, as listed. The server trims and lowercases each kind before checking it.                    |
| `name`                                                                                                 | *Optional[str]*                                                                                        | :heavy_minus_sign:                                                                                     | Case-insensitive prefix of an entity name; surrounding blanks are trimmed and a blank name is refused. |
| `entity_ids`                                                                                           | List[*str*]                                                                                            | :heavy_minus_sign:                                                                                     | Entity node ids, as returned by entity search. Typed values have no id.                                |
| `mentioned_date`                                                                                       | [Optional[models.MentionedDate]](../models/mentioneddate.md)                                           | :heavy_minus_sign:                                                                                     | Overlap with a date the record mentions; half-open, `from` must not be after `to`.                     |
| `amount`                                                                                               | [Optional[models.Amount]](../models/amount.md)                                                         | :heavy_minus_sign:                                                                                     | `min` must not be after `max`.                                                                         |
| `quantity`                                                                                             | [Optional[models.Quantity]](../models/quantity.md)                                                     | :heavy_minus_sign:                                                                                     | In SI units of the dimension. `min` must not be after `max`.                                           |
| `percent`                                                                                              | [Optional[models.Percent]](../models/percent.md)                                                       | :heavy_minus_sign:                                                                                     | Fractions (0.125 is 12.5%). `min` must not be after `max`.                                             |