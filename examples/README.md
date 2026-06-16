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

| Variable | Required | Notes |
| --- | --- | --- |
| `PIPESHUB_BEARER_AUTH` | yes | JWT access token (raw token only — no `Bearer` prefix) |
| `PIPESHUB_BASE_URL` | yes | API root without `/api/v1` (e.g. `http://localhost:3000`) |

The `examples` project installs the published `pipeshub-sdk` package from PyPI. Streaming examples call the SDK stream methods and parse raw SSE lines from `stream.response` in `helpers.py` (workaround for a known SSE parser issue in PyPI `1.2.0`).

## Example groups

| Directory | Description |
| --- | --- |
| [`agent_conversation/`](agent_conversation/README.md) | Agent chat streaming, conversation CRUD, archives, feedback, regeneration |

## How to run

From `examples/`:

```bash
uv run python agent_conversation/<script>.py
```

Replace `<script>.py` with any script listed in [`agent_conversation/README.md`](agent_conversation/README.md).

Scripts call `load_dotenv()`, which discovers `examples/.env` when run from `examples/` or `examples/agent_conversation/`.

From the repository root:

```bash
uv run --project examples python examples/agent_conversation/<script>.py
```

Each script builds an authenticated `Pipeshub` client inline using `PIPESHUB_BEARER_AUTH` and `PIPESHUB_BASE_URL` from the environment.
