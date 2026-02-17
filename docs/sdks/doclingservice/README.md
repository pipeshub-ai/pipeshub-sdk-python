# DoclingService

## Overview

### Available Operations

* [get_health](#get_health) - [Docling Service] Health check
* [process_pdf](#process_pdf) - [Docling Service] Process PDF document
* [parse_pdf](#parse_pdf) - [Docling Service] Parse PDF (Phase 1)

## get_health

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Health check endpoint for the Docling Service (Python FastAPI).<br><br>

<b>Service:</b> Docling Service<br>
<b>Port:</b> 8081<br>
<b>Base URL:</b> <code>http://localhost:8081</code><br><br>

<b>Authentication:</b> None required for health check<br><br>

<b>Note:</b> This is an internal service used by the Indexing Service
for advanced document parsing. No user-facing endpoints.


### Example Usage

<!-- UsageSnippet language="python" operationID="doclingServiceHealth" method="get" path="/docling/health" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.docling_service.get_health()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.DoclingServiceHealthResponse](../../models/doclingservicehealthresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## process_pdf

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Full PDF processing endpoint - parses PDF and creates content blocks.<br><br>

<b>Service:</b> Docling Service<br>
<b>Port:</b> 8081<br>
<b>Base URL:</b> <code>http://localhost:8081</code><br><br>

<b>Authentication:</b> Internal only - called by Indexing Service<br><br>

<b>Processing Steps:</b>
<ol>
<li>Decode base64 PDF binary</li>
<li>Parse document structure using Docling library</li>
<li>Extract text, tables, and images</li>
<li>Create content blocks for indexing</li>
</ol>

<b>Timeout:</b> 40 minutes (for large documents)


### Example Usage

<!-- UsageSnippet language="python" operationID="doclingProcessPdf" method="post" path="/docling/process-pdf" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.docling_service.process_pdf(record_name="<value>", pdf_binary="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `record_name`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Name/identifier of the document                                     |
| `pdf_binary`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Base64 encoded PDF binary data                                      |
| `org_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Organization ID (optional)                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.DoclingProcessPdfResponse](../../models/doclingprocesspdfresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## parse_pdf

⚠️ <b>INTERNAL SERVICE ENDPOINT</b><br><br>

Phase 1 of two-phase PDF processing - parse PDF without block creation.<br><br>

<b>Service:</b> Docling Service<br>
<b>Port:</b> 8081<br>
<b>Base URL:</b> <code>http://localhost:8081</code><br><br>

<b>Authentication:</b> Internal only - called by Indexing Service<br><br>

<b>Note:</b> This endpoint only parses the PDF structure without making
LLM calls for table processing. Use <code>/create-blocks</code> for Phase 2.


### Example Usage

<!-- UsageSnippet language="python" operationID="doclingParsePdf" method="post" path="/docling/parse-pdf" -->
```python
from pipeshub import Pipeshub


with Pipeshub(
    server_url="https://api.example.com",
) as p_client:

    res = p_client.docling_service.parse_pdf(record_name="<value>", pdf_binary="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `record_name`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Name/identifier of the document                                     |
| `pdf_binary`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Base64 encoded PDF binary data                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |
| `server_url`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional server URL to use.                                      |

### Response

**[models.DoclingParsePdfResponse](../../models/doclingparsepdfresponse.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |