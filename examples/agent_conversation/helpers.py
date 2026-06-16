import json
import os
from datetime import datetime, timezone
from typing import Any, Iterable

from pipeshub_sdk.models import FiltersTypedDict

DEFAULT_AGENT_KEY = "52b7e901-f3e9-4009-bcd7-c0274c58f296"
DEFAULT_CONNECTOR_ID = "270d4bac-234a-4c0d-963f-84f152cd21f0"


def agent_key() -> str:
    return os.getenv("PIPESHUB_AGENT_KEY", DEFAULT_AGENT_KEY)


def connector_id() -> str:
    return os.getenv("CONNECTOR_ID", DEFAULT_CONNECTOR_ID)


def default_filters() -> FiltersTypedDict:
    return {"apps": [connector_id()]}


def stream_bot_reply(
    stream: Iterable[Any],
    *,
    print_output: bool = True,
) -> tuple[str, str, str, str | None]:
    """Consume an agent SSE stream and return conversation id, title, answer, bot message id."""
    printed_any_chunk = False
    for ev in stream:
        if ev.event == "answer_chunk" and ev.data:
            chunk = json.loads(ev.data)
            token = chunk.get("chunk") or chunk.get("delta")
            if print_output and token:
                printed_any_chunk = True
                print(token, end="", flush=True)
        elif ev.event == "complete" and ev.data is not None:
            payload = json.loads(ev.data)
            conversation = payload["conversation"]
            conv_id = conversation["_id"]
            title = conversation.get("title") or ""
            bot = next(
                msg
                for msg in reversed(conversation["messages"])
                if msg.get("messageType") == "bot_response"
            )
            answer = bot.get("content", "")
            if print_output:
                if not printed_any_chunk and answer:
                    print(answer, end="", flush=True)
                print()
            return conv_id, title, answer, bot.get("_id")
        elif ev.event == "error":
            raise RuntimeError(f"stream error: {ev.data}")
    raise RuntimeError("stream ended without complete event")


def format_activity(conv) -> str:
    if conv.last_activity_at:
        dt = datetime.fromtimestamp(conv.last_activity_at / 1000, tz=timezone.utc)
        return dt.strftime("%Y-%m-%d %H:%M:%S UTC")
    if conv.updated_at:
        return conv.updated_at.strftime("%Y-%m-%d %H:%M:%S %Z")
    return "-"
