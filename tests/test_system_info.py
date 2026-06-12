"""Tests for runtime identity strings exposed to LLM tool descriptions."""

from open_terminal.env import runtime_username


def test_runtime_username_from_user_env(monkeypatch):
    monkeypatch.setenv("USER", "alice")
    monkeypatch.delenv("HOME", raising=False)
    assert runtime_username() == "alice"


def test_runtime_username_from_home_when_user_unset(monkeypatch):
    monkeypatch.delenv("USER", raising=False)
    monkeypatch.setenv("HOME", "/home/user")
    assert runtime_username() == "user"


def test_runtime_username_not_unknown_when_user_unset(monkeypatch):
    monkeypatch.delenv("USER", raising=False)
    monkeypatch.setenv("HOME", "/home/user")
    assert runtime_username() != "unknown"
