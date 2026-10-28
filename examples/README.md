## Setup

Install the dependencies, then run any example script with `python`.

```bash
pip install "pipeshub-sdk>=1.7.0" python-dotenv
```

## Connectors

`connectors/` has one program per connector operation, new in SDK 2.0.0. They sign in with
a **personal access token** in `PIPESHUB_BEARER_AUTH`. Use one of an admin with the `connector:*` scopes:
creating team connectors and OAuth configurations is admin-only, and an OAuth app's client-credentials
token acts as a service account, which is never an admin.

Each script loads `examples/.env`; variables already set in the environment take precedence.

```bash
pip install "pipeshub-sdk>=2.0.0" python-dotenv
python connectors/create_connector_instance.py
```

`create_connector_instance` creates a team RSS connector and prints its id. Put it in
`PIPESHUB_CONNECTOR_ID` for the programs that act on one connector, and delete it with
`delete_connector_instance` when you are done.

| Variable | Used by |
| --- | --- |
| `PIPESHUB_CONNECTOR_ID` | the programs that act on one connector instance |
| `PIPESHUB_CONNECTOR_TYPE` | the registry, schema, connection check and OAuth configuration programs (`RSS`, `Jira`, ...) |
| `PIPESHUB_FILTER_KEY` | `get_filter_field_options`: a filter of the connector's type whose options are fetched from the source |
| `PIPESHUB_OAUTH_CONFIG_ID` | the get, update and delete OAuth configuration programs |
| `PIPESHUB_OAUTH_CODE`, `PIPESHUB_OAUTH_STATE` | `handle_oauth_callback`: the `code` and `state` of the provider's redirect |

- `get_oauth_authorization_url` needs a connector created with an OAuth auth type; an RSS connector is refused.
- `test_connector_connection` works only for types with a connection check (PostgreSQL, SMB, OneDrive).
