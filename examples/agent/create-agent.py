# To run the example:
# pip install -e .
# python create-agent.py
from pipeshub_sdk import Pipeshub, errors, models

# Load env and require bearer token
load_dotenv()
token = (os.getenv("PIPESHUB_BEARER_AUTH") or "").strip()
if not token:
    sys.exit(1)

# Create an agent with available LLM/reasoning models
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
        response = pipeshub.agents.create_agent(
            name="Sample Agent - Python Demo",
            description="Demo agent created by pipeshub-sdk agent example",
            system_prompt="You are a helpful assistant.",
            start_message="Hello! How can I help you today?",
            models=entries,
            toolsets=[],
            knowledge=[],
        )
        logger.json("Created agent", response.model_dump())
        logger.info("Agent key:", response.agent_key)
    except errors.PipeshubError as e:
        logger.error("PipeshubError: %s", e)
