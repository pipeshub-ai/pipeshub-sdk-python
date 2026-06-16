import json
from typing import Iterable


def iter_sse_events(lines: Iterable[str | bytes]) -> Iterable[dict[str, str]]:
    """Parse raw SSE lines (event:/data:) from the SDK stream response."""
    event_name: str | None = None
    data_lines: list[str] = []

    for raw in lines:
        line = raw.decode() if isinstance(raw, bytes) else raw
        if line == "":
            if event_name is not None or data_lines:
                yield {"event": event_name or "message", "data": "\n".join(data_lines)}
            event_name = None
            data_lines = []
            continue
        if line.startswith(":"):
            continue
        field, _, value = line.partition(":")
        if value.startswith(" "):
            value = value[1:]
        if field == "event":
            event_name = value
        elif field == "data":
            data_lines.append(value)


def stream_bot_reply(
    stream,
    *,
    print_output: bool = True,
) -> tuple[str, str, str, str | None]:
    """Read SSE from the SDK stream response and print the bot reply."""
    printed_any_chunk = False
    for ev in iter_sse_events(stream.response.iter_lines()):
        name = ev["event"]
        data = ev["data"]
        if name == "answer_chunk" and data:
            chunk = json.loads(data)
            token = chunk.get("chunk") or chunk.get("delta")
            if print_output and token:
                printed_any_chunk = True
                print(token, end="", flush=True)
        elif name == "complete" and data:
            payload = json.loads(data)
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
        elif name == "error":
            raise RuntimeError(f"stream error: {data}")
    raise RuntimeError("stream ended without complete event")
