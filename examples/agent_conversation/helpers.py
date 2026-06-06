import json
import os
import time
from datetime import datetime, timezone

from pipeshub_sdk import Pipeshub
from pipeshub_sdk.models import (
    AgentConversationListItem,
    AgentCreateWebSearchTypedDict,
    FiltersTypedDict,
)

DEFAULT_AGENT_KEY = "52b7e901-f3e9-4009-bcd7-c0274c58f296"
DEFAULT_CONNECTOR_ID = "270d4bac-234a-4c0d-963f-84f152cd21f0"


def agent_key() -> str:
    return os.getenv("PIPESHUB_AGENT_KEY", DEFAULT_AGENT_KEY)


def connector_id() -> str:
    return os.getenv("CONNECTOR_ID", DEFAULT_CONNECTOR_ID)


def default_filters() -> FiltersTypedDict:
    return {"apps": [connector_id()]}


def first_llm_model_key(sdk: Pipeshub) -> str:
    if key := os.getenv("PIPESHUB_AGENT_MODEL_KEY"):
        return key
    res = sdk.ai_models_providers.get_available_models_by_type(model_type="llm")
    for model in res.models:
        if model.is_reasoning and model.model_key:
            return model.model_key
    if res.models and res.models[0].model_key:
        return res.models[0].model_key
    raise RuntimeError("no LLM model configured; set PIPESHUB_AGENT_MODEL_KEY in .env")


def decode_complete(data: str) -> tuple[str, str, str, str | None]:
    conv = json.loads(data).get("conversation", {})
    conv_id = conv.get("_id", "")
    title = conv.get("title") or ""
    answer = ""
    bot_response_message_id = None
    for msg in reversed(conv.get("messages", [])):
        if not title and msg.get("messageType") == "user_query":
            title = msg.get("content", "")
        if msg.get("messageType") == "bot_response":
            answer = msg.get("content", "")
            bot_response_message_id = msg.get("_id")
            break
    return answer, conv_id, title, bot_response_message_id


def stream_create(
    sdk: Pipeshub,
    query: str,
    filters: FiltersTypedDict | None = None,
    *,
    key: str | None = None,
    print_bot: bool = True,
) -> tuple[str, str, str, str | None]:
    with sdk.agents.stream_agent_conversation(
        agent_key=key or agent_key(),
        query=query,
        filters=filters,
        chat_mode="auto",
    ) as stream:
        if print_bot:
            print(f"You: {query}\n\nBot: ", end="", flush=True)
        for ev in stream:
            if not ev.event or not ev.data:
                continue
            if ev.event == "complete":
                answer, conv_id, title, bot_response_message_id = decode_complete(ev.data)
                if print_bot and answer:
                    print(answer)
                if not conv_id:
                    raise RuntimeError("complete event missing conversation id")
                return conv_id, title, answer, bot_response_message_id
            if ev.event == "error":
                raise RuntimeError(f"stream error: {ev.data}")
    raise RuntimeError("stream ended without complete event")


async def stream_create_async(
    sdk: Pipeshub,
    query: str,
    filters: FiltersTypedDict | None = None,
    *,
    key: str | None = None,
    print_bot: bool = True,
) -> tuple[str, str, str, str | None]:
    stream = await sdk.agents.stream_agent_conversation_async(
        agent_key=key or agent_key(),
        query=query,
        filters=filters,
        chat_mode="auto",
    )
    async with stream:
        if print_bot:
            print(f"You: {query}\n\nBot: ", end="", flush=True)
        async for ev in stream:
            if not ev.event or not ev.data:
                continue
            if ev.event == "complete":
                answer, conv_id, title, bot_response_message_id = decode_complete(ev.data)
                if print_bot and answer:
                    print(answer)
                if not conv_id:
                    raise RuntimeError("complete event missing conversation id")
                return conv_id, title, answer, bot_response_message_id
            if ev.event == "error":
                raise RuntimeError(f"stream error: {ev.data}")
    raise RuntimeError("stream ended without complete event")


def stream_add_message(
    sdk: Pipeshub,
    conv_id: str,
    query: str,
    filters: FiltersTypedDict | None = None,
    *,
    key: str | None = None,
    print_bot: bool = True,
) -> str:
    with sdk.agents.stream_agent_conversation_message(
        agent_key=key or agent_key(),
        conversation_id=conv_id,
        query=query,
        filters=filters,
        chat_mode="auto",
    ) as stream:
        if print_bot:
            print(f"\nYou: {query}\n\nBot: ", end="", flush=True)
        for ev in stream:
            if not ev.event or not ev.data:
                continue
            if ev.event == "complete":
                answer, _, _, _ = decode_complete(ev.data)
                if print_bot and answer:
                    print(answer)
                return answer
            if ev.event == "error":
                raise RuntimeError(f"stream error: {ev.data}")
    raise RuntimeError("stream ended without complete event")


def stream_regenerate(
    sdk: Pipeshub,
    conv_id: str,
    message_id: str,
    filters: FiltersTypedDict | None = None,
    *,
    key: str | None = None,
) -> str:
    accumulated = ""
    with sdk.agents.regenerate_agent_conversation_message(
        agent_key=key or agent_key(),
        conversation_id=conv_id,
        message_id=message_id,
        filters=filters,
    ) as stream:
        print(f"\nRegenerating message {message_id} ...\n\nBot: ", end="", flush=True)
        for ev in stream:
            if not ev.event or not ev.data:
                continue
            if ev.event == "answer_chunk":
                chunk = json.loads(ev.data)
                accumulated = chunk.get("accumulated") or accumulated
            elif ev.event == "complete":
                answer, _, _, _ = decode_complete(ev.data)
                answer = answer or accumulated
                print(answer)
                return answer
            elif ev.event == "error":
                raise RuntimeError(f"stream error: {ev.data}")
    raise RuntimeError("stream ended without complete event")


def update_title(sdk: Pipeshub, conv_id: str, title: str, *, key: str | None = None) -> str:
    res = sdk.agents.update_agent_conversation_title(
        agent_key=key or agent_key(),
        conversation_id=conv_id,
        title=title,
    )
    updated = res.conversation.title
    if not updated:
        raise RuntimeError("response missing conversation title")
    return updated


async def update_title_async(sdk: Pipeshub, conv_id: str, title: str, *, key: str | None = None) -> str:
    res = await sdk.agents.update_agent_conversation_title_async(
        agent_key=key or agent_key(),
        conversation_id=conv_id,
        title=title,
    )
    updated = res.conversation.title
    if not updated:
        raise RuntimeError("response missing conversation title")
    return updated


def print_conversation(sdk: Pipeshub, conv_id: str, *, key: str | None = None, verbose: bool = False) -> None:
    res = sdk.agents.get_agent_conversation_by_id(
        agent_key=key or agent_key(),
        conversation_id=conv_id,
    )
    conv = res.conversation
    print(f"  id: {conv.id}")
    if conv.title:
        print(f"  title: {conv.title!r}")
    messages = conv.messages or []
    print(f"  messages: {len(messages)}")
    for i, msg in enumerate(messages, 1):
        content = msg.content or ""
        msg_type = msg.message_type or ""
        if verbose:
            print(f"\n--- message {i} [{msg_type}] ---\n{content}")
        else:
            print(f"  - message {i} [{msg_type}]: {content}")


def format_activity(conv) -> str:
    if conv.last_activity_at:
        dt = datetime.fromtimestamp(conv.last_activity_at / 1000, tz=timezone.utc)
        return dt.strftime("%Y-%m-%d %H:%M:%S UTC")
    if conv.updated_at:
        return conv.updated_at.strftime("%Y-%m-%d %H:%M:%S %Z")
    return "—"


def archive_conversation(sdk: Pipeshub, conv_id: str, *, key: str | None = None) -> None:
    sdk.agents.archive_agent_conversation(
        agent_key=key or agent_key(),
        conversation_id=conv_id,
    )


def delete_conversation(sdk: Pipeshub, conv_id: str, *, key: str | None = None) -> None:
    sdk.agents.delete_agent_conversation_by_id(
        agent_key=key or agent_key(),
        conversation_id=conv_id,
    )


def list_archived(
    sdk: Pipeshub, *, key: str | None = None, page_limit: int = 20
) -> list[AgentConversationListItem]:
    key = key or agent_key()
    archived = []
    page = 1
    while True:
        res = sdk.agents.list_agent_conversation_archives(
            agent_key=key,
            page=page,
            limit=page_limit,
            sort_by="lastActivityAt",
            sort_order="desc",
        )
        archived.extend(res.conversations)
        p = res.pagination
        if not p.has_next_page or page >= p.total_pages:
            break
        page += 1
    return archived


def create_agent_with_web_search(sdk: Pipeshub) -> str:
    ws: AgentCreateWebSearchTypedDict = {"provider": "duckduckgo"}
    for p in sdk.web_search.get_web_search_providers().providers:
        if p.provider == "duckduckgo" and p.provider_key:
            ws["provider_key"] = p.provider_key
            break
    model_key = first_llm_model_key(sdk)
    res = sdk.agents.create_agent(
        name=f"SDK example {int(time.time())}",
        models=[{"model_key": model_key, "is_reasoning": True}],
        web_search=ws,
    )
    if not res.agent.key:
        raise RuntimeError("create agent: response missing agent key")
    return res.agent.key
