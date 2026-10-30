"""
Warn once per PipesHub instance when its release differs (major.minor) from the
one this SDK version is built for. The server reports its release on GET /api/v1/health.
"""

import logging
import threading
from typing import Any, Optional, Set, Tuple

import httpx

from ..httpclient import HttpClient
from .types import BeforeRequestContext, BeforeRequestHook

# The PipesHub release this SDK version is built for. Bump it with each SDK release.
SUPPORTED_PIPESHUB_VERSION = "1.0.0"

API_PREFIX = "/api/v1"
HEALTH_TIMEOUT_SECONDS = 2.0

logger = logging.getLogger("pipeshub_sdk")

_checked: Set[str] = set()
_checked_lock = threading.Lock()


def _major_minor(version: str) -> Optional[Tuple[int, int]]:
    parts = version.strip().lstrip("v").split(".")
    if len(parts) < 2:
        return None
    try:
        return int(parts[0]), int(parts[1])
    except ValueError:
        return None


def mismatch_warning(sdk_version: str, instance: str, health: Any) -> Optional[str]:
    """The warning for a /health response body, or None when there is nothing to warn about."""
    if not isinstance(health, dict) or "status" not in health:
        return None
    build = health.get("build")
    if not isinstance(build, dict):
        # PipesHub reports `build` from 1.0.0 on.
        running = "a PipesHub release older than 1.0.0"
    else:
        version = build.get("version")
        if not isinstance(version, str):
            return None  # a local or dev build reports no version
        server = _major_minor(version)
        if server is None or server == _major_minor(SUPPORTED_PIPESHUB_VERSION):
            return None
        running = f"PipesHub {version}"
    return (
        f"pipeshub-sdk {sdk_version} is built for PipesHub {SUPPORTED_PIPESHUB_VERSION}, "
        f"but {instance} runs {running}. Some calls may not work as expected."
    )


def _check(client: HttpClient, sdk_version: str, instance: str) -> None:
    try:
        request = client.build_request(
            "GET", f"{instance}{API_PREFIX}/health", timeout=HEALTH_TIMEOUT_SECONDS
        )
        response = client.send(request)
        if response.status_code != 200:
            return
        warning = mismatch_warning(sdk_version, instance, response.json())
    except Exception:  # pylint: disable=broad-exception-caught
        return  # the check must never affect the caller's requests
    if warning:
        logger.warning(warning)


class VersionCheckHook(BeforeRequestHook):
    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> httpx.Request:
        url = str(request.url)
        index = url.find(API_PREFIX + "/")
        client = hook_ctx.config.client
        if index == -1 or client is None:
            return request
        instance = url[:index]
        with _checked_lock:
            if instance in _checked:
                return request
            _checked.add(instance)
        # Inline, not a thread: `with Pipeshub()` closes the client on exit, which would cut off a background
        # check. Costs one /health round trip (at most HEALTH_TIMEOUT_SECONDS) on the first request per instance.
        _check(client, hook_ctx.config.sdk_version, instance)
        return request
