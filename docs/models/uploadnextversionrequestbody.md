# UploadNextVersionRequestBody

Request payload


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `current_version_note`                                             | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Note describing the current version being replaced                 | Draft version with initial content                                 |
| `next_version_note`                                                | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Note describing the new version being uploaded                     | Final version with all revisions incorporated                      |
| `file`                                                             | [models.UploadNextVersionFile](../models/uploadnextversionfile.md) | :heavy_check_mark:                                                 | New version file (max 100MB)                                       |                                                                    |