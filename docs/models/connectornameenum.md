# ConnectorNameEnum

Name of the source connector. Mirrors the values of the backend
`Connectors` enum (`backend/python/app/config/constants/arangodb.py`);
records store the enum value (e.g. Google Drive is `DRIVE`,
SharePoint Online is `SHAREPOINT ONLINE`), not the enum member name.


## Example Usage

```python
from pipeshub_sdk.models import ConnectorNameEnum

# Open enum: unrecognized values are captured as UnrecognizedStr
value: ConnectorNameEnum = "DRIVE"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"DRIVE"`
- `"DRIVE WORKSPACE"`
- `"GMAIL"`
- `"GMAIL WORKSPACE"`
- `"CALENDAR"`
- `"ONEDRIVE"`
- `"SHAREPOINT ONLINE"`
- `"OUTLOOK"`
- `"OUTLOOK PERSONAL"`
- `"OUTLOOK CALENDAR"`
- `"MICROSOFT TEAMS"`
- `"NOTION"`
- `"NOTION PERSONAL"`
- `"SLACK"`
- `"SLACK WORKSPACE"`
- `"KB"`
- `"CONFLUENCE"`
- `"CONFLUENCE DATA CENTER"`
- `"CONFLUENCE DATA CENTER PERSONAL"`
- `"JIRA"`
- `"JIRA PERSONAL"`
- `"JIRA DATA CENTER"`
- `"JIRA DATA CENTER PERSONAL"`
- `"BOX"`
- `"NEXTCLOUD"`
- `"DROPBOX"`
- `"DROPBOX PERSONAL"`
- `"WEB"`
- `"BOOKSTACK"`
- `"DRUPAL WIKI"`
- `"GITHUB"`
- `"GITHUB TEAMS"`
- `"SERVICENOW"`
- `"SALESFORCE"`
- `"S3"`
- `"MINIO"`
- `"GCS"`
- `"AZURE BLOB"`
- `"AZURE FILES"`
- `"LINEAR"`
- `"ZAMMAD"`
- `"ZOOM"`
- `"GITLAB"`
- `"GITLAB PERSONAL"`
- `"SNOWFLAKE"`
- `"POSTGRESQL"`
- `"MARIADB"`
- `"UNKNOWN"`
- `"RSS"`
- `"LOCAL_FS"`
- `"CODING_SANDBOX"`
- `"DATABASE_SANDBOX"`
- `"IMAGE_GENERATION"`
- `"ATTACHMENTS"`
