# ConnectorSyncCustomField

A connector-specific sync setting. Send its value in `config.sync` under `name`.


## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `name`             | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `display_name`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `description`      | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `field_type`       | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `required`         | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `default_value`    | *Optional[Any]*    | :heavy_minus_sign: | N/A                |
| `validation`       | Dict[str, *Any*]   | :heavy_minus_sign: | N/A                |
| `is_secret`        | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `non_editable`     | *Optional[bool]*   | :heavy_minus_sign: | N/A                |
| `options`          | List[*str*]        | :heavy_minus_sign: | N/A                |