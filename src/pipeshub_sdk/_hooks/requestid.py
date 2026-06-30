"""
Stamp an x-request-id trace header onto every outbound SDK request.
"""

import base64
import binascii
import json
import uuid
from typing import Optional

import httpx

from .types import BeforeRequestContext, BeforeRequestHook

REQUEST_ID_HEADER = "x-request-id"


def _user_id_from_token(request: httpx.Request) -> Optional[str]:

    auth = request.headers.get("authorization", "")

    if not auth.lower().startswith("bearer "):
        return None

    parts = auth[7:].strip().split(".")

    base64url = parts[1] if len(parts) > 1 else ""

    if not base64url:
        return None
    payload = base64url + "=" * (-len(base64url) % 4)  # restore base64url padding
    try:
        claims = json.loads(base64.urlsafe_b64decode(payload))
    except (binascii.Error, ValueError):
        return None
    return claims.get("userId") or None if isinstance(claims, dict) else None


class RequestIDHook(BeforeRequestHook):
    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> httpx.Request:
        if request.headers.get(REQUEST_ID_HEADER):
            return request
        user_id = _user_id_from_token(request)
        random = uuid.uuid4().hex
        request.headers[REQUEST_ID_HEADER] = (
            f"sdk-py-{user_id}-{random}" if user_id else f"sdk-py-{random}"
        )
        return request
