# SemanticSearchGraphRecord

Graph record vertex returned in `records` and as values of `virtual_to_record_map`.
All listed fields are optional in the schema so partial or evolving documents validate; typical Arango documents
usually include `_key`, `_id`, `_rev`, `orgId`, `recordName`, `externalRecordId`, `recordType`, `origin`,
`createdAtTimestamp`, and `connectorId`. Extend this schema when new stable fields appear on Record vertices.



## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `key`                            | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `id`                             | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `rev`                            | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `record_name`                    | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `external_record_id`             | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `record_type`                    | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `origin`                         | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `created_at_timestamp`           | *OptionalNullable[float]*        | :heavy_minus_sign:               | N/A                              |
| `connector_id`                   | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `org_id`                         | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `updated_at_timestamp`           | *OptionalNullable[float]*        | :heavy_minus_sign:               | N/A                              |
| `external_group_id`              | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `external_parent_id`             | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `external_revision_id`           | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `external_root_group_id`         | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `record_group_id`                | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `version`                        | *OptionalNullable[float]*        | :heavy_minus_sign:               | N/A                              |
| `connector_name`                 | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `mime_type`                      | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `web_url`                        | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `last_sync_timestamp`            | *OptionalNullable[float]*        | :heavy_minus_sign:               | N/A                              |
| `source_created_at_timestamp`    | *OptionalNullable[float]*        | :heavy_minus_sign:               | N/A                              |
| `source_last_modified_timestamp` | *OptionalNullable[float]*        | :heavy_minus_sign:               | N/A                              |
| `is_deleted`                     | *OptionalNullable[bool]*         | :heavy_minus_sign:               | N/A                              |
| `is_archived`                    | *OptionalNullable[bool]*         | :heavy_minus_sign:               | N/A                              |
| `is_vlm_ocr_processed`           | *OptionalNullable[bool]*         | :heavy_minus_sign:               | N/A                              |
| `deleted_by_user_id`             | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `processing_started_at`          | *OptionalNullable[float]*        | :heavy_minus_sign:               | N/A                              |
| `parsing_status`                 | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `indexing_status`                | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `extraction_status`              | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `is_latest_version`              | *OptionalNullable[bool]*         | :heavy_minus_sign:               | N/A                              |
| `is_dirty`                       | *OptionalNullable[bool]*         | :heavy_minus_sign:               | N/A                              |
| `reason`                         | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `last_index_timestamp`           | *OptionalNullable[float]*        | :heavy_minus_sign:               | N/A                              |
| `last_extraction_timestamp`      | *OptionalNullable[float]*        | :heavy_minus_sign:               | N/A                              |
| `summary_document_id`            | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `storage_document_id`            | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `virtual_record_id`              | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `preview_renderable`             | *OptionalNullable[bool]*         | :heavy_minus_sign:               | N/A                              |
| `is_shared`                      | *OptionalNullable[bool]*         | :heavy_minus_sign:               | N/A                              |
| `is_dependent_node`              | *OptionalNullable[bool]*         | :heavy_minus_sign:               | N/A                              |
| `parent_node_id`                 | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `hide_weburl`                    | *OptionalNullable[bool]*         | :heavy_minus_sign:               | N/A                              |
| `is_internal`                    | *OptionalNullable[bool]*         | :heavy_minus_sign:               | N/A                              |
| `md5_checksum`                   | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `size_in_bytes`                  | *OptionalNullable[float]*        | :heavy_minus_sign:               | N/A                              |
| `definition`                     | *OptionalNullable[str]*          | :heavy_minus_sign:               | N/A                              |
| `source_tables`                  | List[*str*]                      | :heavy_minus_sign:               | N/A                              |
| `row_count`                      | *OptionalNullable[float]*        | :heavy_minus_sign:               | N/A                              |