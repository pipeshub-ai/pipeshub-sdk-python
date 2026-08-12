# MessageReasoningTurn

One model turn's chain-of-thought. Persisted only when reasoning
persistence is enabled; the array is empty otherwise.



## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `message_id`       | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `turn_index`       | *Optional[float]*  | :heavy_minus_sign: | N/A                |
| `content`          | *str*              | :heavy_check_mark: | N/A                |