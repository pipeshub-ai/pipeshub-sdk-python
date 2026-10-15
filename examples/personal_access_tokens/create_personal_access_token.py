"""Create a personal access token.

Creates a token with two scopes and a 30-day expiry, then revokes it so the
example leaves nothing behind. `expiry_days` accepts 30, 90, 365 or "never".

The personal access token endpoints need an interactive user session and
reject PATs and OAuth tokens, so this example signs in with
PIPESHUB_TEST_USER_EMAIL and PIPESHUB_TEST_USER_PASSWORD.
"""

import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv

from pipeshub_sdk import Pipeshub as SDK, models

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

server_url = f'{os.environ["PIPESHUB_BASE_URL"].rstrip("/")}/api/v1'
email = os.environ["PIPESHUB_TEST_USER_EMAIL"]
password = os.environ["PIPESHUB_TEST_USER_PASSWORD"]


async def login() -> str:
    """Sign in with email and password and return the session's access token."""
    async with SDK(server_url=server_url) as anonymous:
        init = await anonymous.user_account.init_auth_async(request={"email": email})
        session_token = init.headers["x-session-token"][0]
        auth = await anonymous.user_account.authenticate_async(
            x_session_token=session_token,
            method="password",
            credentials={"password": password},
            email=email,
        )
    if not isinstance(auth, models.AuthenticateFinalResponse):
        raise RuntimeError("sign-in needs another step (MFA); use an account without MFA")
    return auth.access_token


async def main() -> None:
    async with SDK(
        server_url=server_url,
        security=models.Security(bearer_auth=await login()),
    ) as client:
        created = await client.personal_access_tokens.create_personal_access_token_async(
            name="SDK example token",
            scopes=["conversation:read", "conversation:chat"],
            expiry_days=30,
        )
        token = created.token
        try:
            # token.access_token holds the secret. It is returned only in this
            # response, so store it now. This example doesn't print it.
            print(f"id: {token.id}")
            print(f"name: {token.name}")
            print(f"scopes: {token.scopes}")
            print(f"expires at: {token.expires_at}")
        finally:
            await client.personal_access_tokens.revoke_personal_access_token_async(
                token_id=token.id,
            )


if __name__ == "__main__":
    asyncio.run(main())
