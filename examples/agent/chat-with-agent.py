# To run the example:
# pip install -e .
# python chat-with-agent.py
from pipeshub_sdk import Pipeshub, errors, models

# Load env and require bearer token
load_dotenv()
token = (os.getenv("PIPESHUB_BEARER_AUTH") or "").strip()
if not token:
    sys.exit(1)

# Create an agent and run an interactive chat loop
with Pipeshub(
    security=models.Security(bearer_auth=token),
    server_url=os.getenv("PIPESHUB_SERVER_URL"),
) as pipeshub:
    try:

        # Resolve available LLM and reasoning models

        r_llm = pipeshub.ai_models_providers.get_available_models_by_type(model_type="llm")
        
        r_reason = pipeshub.ai_models_providers.get_available_models_by_type(model_type="reasoning")
        llms = (r_llm.models or []) if r_llm else []
        reasons = (r_reason.models or []) if r_reason else []
        llm = llms[0] if llms else None
        reason = reasons[0] if reasons else llm
        entries = []
        if llm:
            entries.append(
                models.CreateAgentModel(
                    model_key=llm.model_key,
                    provider=llm.provider,
                    model_name=llm.model,
                    is_reasoning=False,
                )
            )
        if reason and reason is not llm:
            entries.append(
                models.CreateAgentModel(
                    model_key=reason.model_key,
                    provider=reason.provider,
                    model_name=reason.model,
                    is_reasoning=True,
                )
            )
        if entries and not any(getattr(e, "is_reasoning") for e in entries):
            entries[0].is_reasoning = True
        # Create the agent
        agent = pipeshub.agents.create_agent(
            name="Sample Agent - Python Demo",
            description="Demo chat agent",
            system_prompt="You are a helpful assistant.",
            start_message="Hello! How can I help you today?",
            models=entries,
            toolsets=[],
            knowledge=[],
        )
        agent_key = agent.agent_key
        logger.info("Agent created. Chat (type 'quit' or 'exit' to stop).")

        # Interactive loop: first message starts conversation, then add_agent_message
        conversation_id = None
        while True:
            user_input = input("> ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("quit", "exit"):
                break
            if conversation_id is None:
                conv = pipeshub.agent_conversations.create_agent_conversation(agent_key=agent_key, query=user_input)
            else:
                conv = pipeshub.agent_conversations.add_agent_message(
                    agent_key=agent_key, conversation_id=conversation_id, query=user_input
                )
            conversation_id = conv.id
            # Take latest bot_response content, or last message content
            messages = getattr(conv, "messages", None) or []
            text = None
            if messages:
                for m in reversed(messages):
                    msg_type = (getattr(m, "message_type", None) or getattr(m, "messageType", None) or "").lower()
                    if msg_type == "bot_response":
                        text = getattr(m, "content", None)
                        if text:
                            break
                if text is None:
                    text = getattr(messages[-1], "content", None)
            logger.info(text if text else "(No assistant reply)")
    except errors.PipeshubError as e:
        logger.error("PipeshubError: %s", e)
