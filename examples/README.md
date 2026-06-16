# Examples

Runnable scripts that call a live PipesHub instance through `pipeshub-sdk`. These are integration demos, not unit tests.

## Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
- A running PipesHub backend (local or remote)

## Setup

From the `examples/` directory:

```bash
uv sync
cp .env.example .env
```

Edit `.env` with your credentials. **Do not commit real secrets.**

| Variable | Required | Default / notes |
| --- | --- | --- |
| `PIPESHUB_TEST_USER_EMAIL` | yes | Workspace user email |
| `PIPESHUB_TEST_USER_PASSWORD` | yes | Password for that user |
| `PIPESHUB_BASE_URL` | no | `http://localhost:3000` |
| `PIPESHUB_AGENT_KEY` | no | Falls back to default in `agent_conversation/helpers.py` |
| `CONNECTOR_ID` | no | Falls back to default in `agent_conversation/helpers.py` |

Verify authentication from `examples/`:

```bash
uv run python client.py .env
```

Expected output: `login ok`

The `examples` project installs the published `pipeshub-sdk` package from PyPI. Streaming examples call the SDK stream methods and parse raw SSE lines from `stream.response` in `helpers.py` (workaround for a known SSE parser issue in PyPI `1.2.0`).

## Shared utilities

### `client.py`

- `load_env(path)` — alias for `python-dotenv`'s `load_dotenv`; loads a `.env` file into `os.environ`
- `client()` — performs email/password auth and returns an authenticated `Pipeshub` client

Convention in example scripts:

```python
from client import client, load_env

load_env(sys.argv[1])
with client() as pipeshub_client:
    pipeshub_client.agents.some_method(...)
```

Each script under `agent_conversation/` adds `examples/` to `sys.path`, so `client` imports work when run from the repo root or from inside the example directory.

## Example groups

| Directory | Description |
| --- | --- |
| [`agent_conversation/`](agent_conversation/README.md) | Agent chat streaming, conversation CRUD, archives, feedback, regeneration |

## How to run

From `examples/`:

```bash
uv run python agent_conversation/<script>.py .env
```

Replace `<script>.py` with any script listed in [`agent_conversation/README.md`](agent_conversation/README.md).

From the repository root, you can also run examples through the `examples` project:

```bash
uv run --project examples python examples/agent_conversation/<script>.py examples/.env
```
