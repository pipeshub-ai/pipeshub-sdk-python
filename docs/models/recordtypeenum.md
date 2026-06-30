# RecordTypeEnum

Type of content. Mirrors the backend `RecordType` enum
(`backend/python/app/models/entities.py`); connector-sourced records
may use any of the connector-specific types below.
- FILE: Uploaded or synced documents (PDF, DOCX, etc.)
- DRIVE: Drive/folder container (Google Drive, OneDrive, etc.)
- WEBPAGE: Web pages crawled or bookmarked
- DATABASE: Database object (e.g. Notion database)
- DATASOURCE: Data source object
- MESSAGE: Chat/messaging content (Slack, Teams)
- MAIL: Email messages (Gmail, Outlook)
- GROUP_MAIL: Group/shared mailbox email messages
- TICKET: Support/issue tickets (Jira, ServiceNow)
- COMMENT: Comments from collaboration tools
- INLINE_COMMENT: Inline comments anchored to content (e.g. Confluence)
- CONFLUENCE_PAGE: Confluence page
- CONFLUENCE_BLOGPOST: Confluence blog post
- SHAREPOINT_PAGE: SharePoint page
- SHAREPOINT_LIST: SharePoint list
- SHAREPOINT_LIST_ITEM: SharePoint list item
- SHAREPOINT_DOCUMENT_LIBRARY: SharePoint document library
- LINK: Web link / bookmark
- PROJECT: Project entity (e.g. Jira project)
- PULL_REQUEST: Source-control pull request
- MEETING: Meeting record (e.g. Zoom)
- PRODUCT: Product entity (CRM)
- DEAL: Deal/opportunity entity (CRM)
- CASE: Case entity (CRM/support)
- TASK: Task entity
- ARTIFACT: Generated/derived artifact
- CODE_FILE: Source-code file
- SQL_TABLE: SQL table object
- SQL_VIEW: SQL view object
- OTHERS: Miscellaneous content types



## Values

| Name                          | Value                         |
| ----------------------------- | ----------------------------- |
| `FILE`                        | FILE                          |
| `DRIVE`                       | DRIVE                         |
| `WEBPAGE`                     | WEBPAGE                       |
| `DATABASE`                    | DATABASE                      |
| `DATASOURCE`                  | DATASOURCE                    |
| `MESSAGE`                     | MESSAGE                       |
| `MAIL`                        | MAIL                          |
| `GROUP_MAIL`                  | GROUP_MAIL                    |
| `TICKET`                      | TICKET                        |
| `COMMENT`                     | COMMENT                       |
| `INLINE_COMMENT`              | INLINE_COMMENT                |
| `CONFLUENCE_PAGE`             | CONFLUENCE_PAGE               |
| `CONFLUENCE_BLOGPOST`         | CONFLUENCE_BLOGPOST           |
| `SHAREPOINT_PAGE`             | SHAREPOINT_PAGE               |
| `SHAREPOINT_LIST`             | SHAREPOINT_LIST               |
| `SHAREPOINT_LIST_ITEM`        | SHAREPOINT_LIST_ITEM          |
| `SHAREPOINT_DOCUMENT_LIBRARY` | SHAREPOINT_DOCUMENT_LIBRARY   |
| `LINK`                        | LINK                          |
| `PROJECT`                     | PROJECT                       |
| `PULL_REQUEST`                | PULL_REQUEST                  |
| `MEETING`                     | MEETING                       |
| `PRODUCT`                     | PRODUCT                       |
| `DEAL`                        | DEAL                          |
| `CASE`                        | CASE                          |
| `TASK`                        | TASK                          |
| `ARTIFACT`                    | ARTIFACT                      |
| `CODE_FILE`                   | CODE_FILE                     |
| `SQL_TABLE`                   | SQL_TABLE                     |
| `SQL_VIEW`                    | SQL_VIEW                      |
| `OTHERS`                      | OTHERS                        |