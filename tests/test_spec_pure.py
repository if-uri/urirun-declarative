# Author: Tom Sapletta · Part of the ifURI solution.
"""Pure unit tests of the spec→bindings mapping — no urirun runtime needed, so they run in the
isolated package-test env (where the integration tests skip)."""
from __future__ import annotations

import pytest

from urirun_declarative.declarative import bindings_from_spec


def test_bindings_from_spec_builds_fetch_binding():
    spec = {
        "connector": "demo",
        "routes": [
            {"uri": "demo://api/thing/query/get", "url": "https://api.example.test/thing"},
        ],
    }
    out = bindings_from_spec(spec)
    b = out["bindings"]
    assert "demo://api/thing/query/get" in b
    cfg = b["demo://api/thing/query/get"]["config"]
    assert cfg["method"] == "GET"          # /query/ defaults to GET
    assert cfg["inputSchema"]["type"] == "object"


def test_bindings_from_spec_env_expansion():
    spec = {
        "environments": {"dev": {"base": "https://dev.test"}, "prod": {"base": "https://prod.test"}},
        "routes": [{"uri": "demo://{env}/thing/command/make", "url": "{base}/make"}],
    }
    out = bindings_from_spec(spec)
    b = out["bindings"]
    assert "demo://dev/thing/command/make" in b
    assert "demo://prod/thing/command/make" in b
    assert b["demo://dev/thing/command/make"]["config"]["method"] == "POST"  # /command/ → POST


def test_route_without_uri_is_rejected():
    with pytest.raises(ValueError):
        bindings_from_spec({"routes": [{"url": "https://x.test"}]})
