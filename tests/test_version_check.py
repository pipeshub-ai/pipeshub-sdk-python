"""The PipesHub release check against a mocked ``GET /api/v1/health``."""

import logging
from types import SimpleNamespace

import httpx
import pytest

from pipeshub_sdk._hooks import versioncheck
from pipeshub_sdk._hooks.versioncheck import VersionCheckHook, mismatch_warning

INSTANCE = "https://pipeshub.example"


@pytest.fixture(autouse=True)
def fresh_state(monkeypatch):
    monkeypatch.setattr(versioncheck, "_checked", set())


def run_hook(health, status=200, url=f"{INSTANCE}/api/v1/knowledgeBase"):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(str(request.url))
        return httpx.Response(status, json=health)

    client = httpx.Client(transport=httpx.MockTransport(handler))
    ctx = SimpleNamespace(config=SimpleNamespace(client=client, sdk_version="2.0.0"))
    request = httpx.Request("GET", url)
    assert VersionCheckHook().before_request(ctx, request) is request
    return calls


@pytest.mark.parametrize(
    "health",
    [
        {"status": "healthy", "build": {"version": "1.0.0", "commitId": "abc"}},
        {"status": "healthy", "build": {"version": "1.0.7", "commitId": "abc"}},
        {"status": "healthy", "build": {"version": None, "commitId": None}},
        {"status": "healthy", "build": {"version": "dev", "commitId": None}},
        {"not": "pipeshub"},
        ["not", "a", "dict"],
    ],
)
def test_no_warning(health):
    assert mismatch_warning("2.0.0", INSTANCE, health) is None


def test_warns_on_another_minor_release():
    health = {"status": "healthy", "build": {"version": "1.1.0", "commitId": "abc"}}
    assert mismatch_warning("2.0.0", INSTANCE, health) == (
        "pipeshub-sdk 2.0.0 is built for PipesHub 1.0.0, but https://pipeshub.example "
        "runs PipesHub 1.1.0. Some calls may not work as expected."
    )


def test_warns_on_a_release_without_build_info():
    warning = mismatch_warning("2.0.0", INSTANCE, {"status": "healthy"})
    assert warning is not None and "a PipesHub release older than 1.0.0" in warning


def test_hook_logs_the_warning_once_per_instance(caplog):
    health = {"status": "healthy", "build": {"version": "0.10.0", "commitId": "abc"}}
    with caplog.at_level(logging.WARNING, logger="pipeshub_sdk"):
        assert run_hook(health) == [f"{INSTANCE}/api/v1/health"]
        assert run_hook(health) == []
    assert [r.message for r in caplog.records] == [
        "pipeshub-sdk 2.0.0 is built for PipesHub 1.0.0, but https://pipeshub.example "
        "runs PipesHub 0.10.0. Some calls may not work as expected."
    ]


def test_hook_is_quiet_when_health_fails(caplog):
    with caplog.at_level(logging.WARNING, logger="pipeshub_sdk"):
        run_hook({"error": "boom"}, status=500)
    assert caplog.records == []


def test_hook_skips_requests_outside_the_api():
    assert run_hook({"status": "healthy"}, url=f"{INSTANCE}/mcp") == []
