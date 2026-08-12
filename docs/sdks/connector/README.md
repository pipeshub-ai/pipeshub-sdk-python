# Connector

## Overview

Connector-related operations

### Available Operations

* [get_record_content](#get_record_content) - Get a record's full parsed content and metadata
* [navigate_knowledge_graph](#navigate_knowledge_graph) - Browse the knowledge graph from a node
* [lookup_record_by_identifier](#lookup_record_by_identifier) - Resolve a URL, issue key or external ID to a Record ID

## get_record_content

Retrieve the full parsed content and metadata of a single record —
the same content PipesHub's own RAG/chat pipeline uses to answer
questions, returned directly instead of via chat.

**When to use this vs. the other record endpoints:**
- `GET /knowledgeBase/record/{recordId}` returns metadata only
  (name, type, indexing status, size) — no content.
- `GET /knowledgeBase/stream/record/{recordId}` returns the original,
  unparsed file bytes — use it to download/open the source file.
- **This endpoint** returns the record's full parsed content as a
  single plain-text `content` string (a metadata header, then the
  block/table text in reading order, then any foreign-key related
  tables) — use it when you need the record's actual textual/tabular
  content without downloading and re-parsing the original file yourself.

**Typical flow:** obtain a `recordId` from a `pipeshub_search` hit or
a chat citation's `recordId`, then call this endpoint to read the
full content when the search snippet or citation excerpt isn't
enough to answer the question.

**Permission scoping:**

The requesting user/token must have access to the record; access is
verified via the knowledge graph before content is returned — a
caller with a valid scope but no access to this specific record gets
a `403`.


### Example Usage

<!-- UsageSnippet language="python" operationID="getRecordContent" method="get" path="/connectors/record/{recordId}/content" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector.get_record_content(record_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `record_id`                                                                                                                      | *str*                                                                                                                            | :heavy_check_mark:                                                                                                               | Record ID to fetch. Obtain it from a `pipeshub_search` result (`hits[*].recordId`) or a chat citation (`citations[*].recordId`). |
| `retries`                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to override the default retry behavior of the client.                                                              |

### Response

**[models.GetRecordContentResponseSchema](../../models/getrecordcontentresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 401, 403                    | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## navigate_knowledge_graph

Open a node in the knowledge graph and see what is inside it — a file
explorer across every connected source.

Call it with no `nodeId` for a flat listing of every record group and
record the caller can reach, newest first. This is a starting point to
pick a node from, not a roster of connected apps — app nodes are never
returned in a listing, though an app's `id` is accepted as a `nodeId`
and lists that app's record groups. Pass a node's `id` to descend:
record groups contain records and folders, and a record contains its
own children — comments, attachments, sub-tasks — plus a `related`
section of cross-referenced records, such as the Confluence page linked
from a Jira ticket. `nodeId` is tolerant: a URL or an issue key such as
`PA-1787` is resolved to its record before navigating, so a link can be
pasted straight in without a separate lookup call.

The response carries a rendered `text` view — breadcrumbs, the current
node, the children listing, `Related:`, and a closing `Next:` line
naming a follow-up call. The structured fields carry the same
information for programmatic use.

**When to use this vs. the other record endpoints:**
- **This endpoint** is for structural exploration — "what is in this
  project", "what is attached to this ticket", "what else links to this
  page". It returns names, types and IDs; it never returns document
  text.
- `GET /connectors/record/{recordId}/content` returns one record's
  actual parsed text. Use it once navigation has identified the record
  you want to read.
- `GET /connectors/record/lookup` is the way in when you hold a URL or
  an issue key rather than a position in the tree.

**Typical flow:** call with no `nodeId` to see what is reachable → pass
a record group's `id` to list its records → take a row whose
`is_record` is true and call
`GET /connectors/record/{recordId}/content` to read it.

**Paging and depth:** results are paginated; `pagination.has_next`
tells you whether to request the next `page`. `depth` above 1 returns
all descendants down to that level as one flat list, each row carrying
its own `level`, instead of only direct children.

**Scope:** everything the caller can read, across both connectors and
Knowledge Base collections. No connector-level filter is applied — the
listing is bounded by per-node permissions alone.

**Permission scoping:**

`rows` and `related` carry only nodes the caller can see, and the
opened node itself is access-checked before any of its details are
returned. A node that does not exist and a node the caller cannot
access are deliberately indistinguishable — both return an empty view
rather than an error.

`breadcrumbs` is the exception: the ancestor trail is resolved by id
alone, without a permission check. For a record shared directly with
the caller, it can therefore name ancestors the caller cannot open.
Treat breadcrumb entries as labels, not as nodes guaranteed to be
navigable.


### Example Usage

<!-- UsageSnippet language="python" operationID="navigateKnowledgeGraph" method="get" path="/connectors/navigate" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector.navigate_knowledge_graph(page=1, limit=50, depth=1)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `node_id`                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | The node to open. Take it from an `id` in a previous navigate or lookup response. Omit it entirely for the flat listing of everything reachable — the usual starting point. A URL or an issue key such as `PA-1787` also works: it is resolved to its record automatically. |
| `page`                                                                                                                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Page number, 1-indexed.                                                                                                                                                                                                                                                     |
| `limit`                                                                                                                                                                                                                                                                     | *Optional[int]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Children per page. The minimum is 50 — smaller values are rejected rather than silently raised.                                                                                                                                                                             |
| `depth`                                                                                                                                                                                                                                                                     | *Optional[int]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Levels of descendants to return in one call. Above 1, `rows` is a flat list of all descendants down to that level rather than only direct children, and each row carries its own `level`.                                                                                   |
| `node_types`                                                                                                                                                                                                                                                                | List[*str*]                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Restrict children to these node types. Repeat the parameter for multiple types: `?nodeTypes=record&nodeTypes=folder`.                                                                                                                                                       |
| `created_after`                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Filter children by source creation time. ISO 8601 `YYYY-MM-DD`, or a full datetime that MUST carry a timezone offset — a naive datetime is rejected rather than assumed to be UTC.                                                                                          |
| `created_before`                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Filter children by source creation time. `YYYY-MM-DD` is inclusive of the whole day.                                                                                                                                                                                        |
| `modified_after`                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Filter children by source modification time.                                                                                                                                                                                                                                |
| `modified_before`                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Filter children by source modification time.                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                         |

### Response

**[models.NavigateKnowledgeGraphResponseSchema](../../models/navigateknowledgegraphresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |

## lookup_record_by_identifier

Turn an external reference into the matching PipesHub record. Accepts a
pasted link, a Jira-style issue key, or a bare external system ID from
any connected source. Repeat `identifiers` to batch-resolve up to ten
in one call.

The response carries a rendered `text` view — each match's metadata
block followed by a `Next:` line naming a follow-up call. The structured
fields carry the same information for programmatic use.

**Accepted identifiers**
- Jira issue URL — `https://acme.atlassian.net/browse/PA-1787`
- Jira issue key — `PA-1787`
- Confluence page URL —
  `https://acme.atlassian.net/wiki/spaces/SD/pages/450625553/Agent+Loop`
- Google Drive / Docs URL — `https://docs.google.com/document/d/1AbC.../edit`
- Slack message link — `https://acme.slack.com/archives/C0123/p1720000000000100`
- Bare external system ID — `450625553`

**When to use this vs. the other record endpoints:**
- **This endpoint** converts an *external* reference into an internal
  Record ID. Reach for it whenever you meet a link or ticket key and
  need the record behind it.
- `GET /connectors/record/{recordId}/content` reads a record you have
  already identified. It needs an internal Record ID, which is exactly
  what this endpoint returns.
- `GET /connectors/navigate` browses the hierarchy when you have a
  position in the tree rather than a specific identifier.

**Typical flow:** call this with the reference, take a match's `id`
from the response, then call
`GET /connectors/record/{recordId}/content` to read the record.

**Multiple matches:** one identifier can legitimately match more than
one record — the same external ID may exist in several connected
instances. In that case the response sets `ambiguous: true` and
`matches` holds every candidate. Present the choice rather than taking
the first; `connectorName` narrows a retry.

**Misses are not errors.**

Only records the caller can see are returned, and a miss is a `200`
with an empty `matches` array and the input echoed in
`not_found_identifiers` — not a `404`. The identifier resolved to
nothing *or* to something the caller may not access; the two are
deliberately indistinguishable, because an identifier is
caller-supplied and guessable, and confirming existence would leak
records across organizations. `searched_connectors` names what was
covered, so a retry with `connectorName` is often the right next move.

**Scope:** resolution searches every connector the caller can access,
regardless of any source filter used elsewhere.


### Example Usage

<!-- UsageSnippet language="python" operationID="lookupRecordByIdentifier" method="get" path="/connectors/record/lookup" -->
```python
import os
from pipeshub_sdk import Pipeshub, models


with Pipeshub(
    security=models.Security(
        bearer_auth=os.getenv("PIPESHUB_BEARER_AUTH", ""),
    ),
) as pipeshub:

    res = pipeshub.connector.lookup_record_by_identifier(identifiers=[
        "<value 1>",
    ], connector_name="DRIVE")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `identifiers`                                                                                                                                                                                                                                                                     | List[*str*]                                                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                                                                | The reference(s) to resolve: a URL, an issue key such as `PA-1787`, or a bare external system ID. Repeat the parameter to batch: `?identifiers=PA-1787&identifiers=PA-1788`. Maximum 10.                                                                                          |                                                                                                                                                                                                                                                                                   |
| `connector_name`                                                                                                                                                                                                                                                                  | [Optional[models.ConnectorNameEnum]](../../models/connectornameenum.md)                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                | Optional hint that prioritises resolution order, e.g. `JIRA`, `CONFLUENCE`, `DRIVE`, `SLACK`. Allowed values are the `ConnectorNameEnum` values. It cannot widen the search beyond the connectors the caller can already access. Useful on a retry when a lookup came back empty. | DRIVE                                                                                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                   |

### Response

**[models.LookupRecordResponseSchema](../../models/lookuprecordresponseschema.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorResponse        | 400, 401, 403, 404          | application/json            |
| errors.ErrorResponse        | 500, 503                    | application/json            |
| errors.PipeshubDefaultError | 4XX, 5XX                    | \*/\*                       |