import os
import sys
from pathlib import Path

from pipeshub_sdk import Pipeshub, models
from pipeshub_sdk.models import AuthenticateFinalResponse


def load_env(path: str | os.PathLike[str]) -> None:
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ[key.strip()] = value.strip()


def client(
    email: str | None = None,
    password: str | None = None,
    *,
    base_url: str | None = None,
) -> Pipeshub:
    email = email or os.getenv("PIPESHUB_TEST_USER_EMAIL")
    password = password or os.getenv("PIPESHUB_TEST_USER_PASSWORD")
    if not email or not password:
        raise ValueError("set PIPESHUB_TEST_USER_EMAIL and PIPESHUB_TEST_USER_PASSWORD")

    root = (base_url or os.getenv("PIPESHUB_BASE_URL") or "http://localhost:3000").rstrip("/")
    api_url = f"{root}/api/v1"

    with Pipeshub(server_url=api_url) as sdk:
        init = sdk.user_account.init_auth(request={"email": email})
        token = (init.headers.get("x-session-token") or [None])[0]
        if not token:
            raise RuntimeError("missing x-session-token")
        auth = sdk.user_account.authenticate(
            x_session_token=token,
            method="password",
            credentials={"password": password},
        )

    if not isinstance(auth, AuthenticateFinalResponse):
        raise RuntimeError("multi-step auth not supported in this example")

    return Pipeshub(
        server_url=api_url,
        security=models.Security(bearer_auth=auth.access_token),
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(f"usage: python {Path(__file__).name} <.env>")
    load_env(sys.argv[1])
    with client():
        print("login ok")
