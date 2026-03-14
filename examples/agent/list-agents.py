# To run the example:
# pip install -e .
# python list-agents.py
from pipeshub_sdk import Pipeshub, errors, models

# Load env and require bearer token
load_dotenv()
token = (os.getenv("PIPESHUB_BEARER_AUTH") or "").strip()
if not token:
    sys.exit(1)

# List all agents for the authenticated user
with Pipeshub(
    security=models.Security(bearer_auth=token),
    server_url=os.getenv("PIPESHUB_SERVER_URL"),
) as pipeshub:
    try:
        response = pipeshub.agents.list_agents()
        logger.json("Agents", [a.model_dump() for a in response])
    except errors.PipeshubError as e:
        logger.error("PipeshubError: %s", e)
