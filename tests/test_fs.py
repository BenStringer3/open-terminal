"""Tests for UserFS path resolution."""

from open_terminal.utils.fs import UserFS


def test_resolve_path_tilde_home():
    fs = UserFS(home="/home/user")
    assert fs.resolve_path("~") == "/home/user"


def test_resolve_path_tilde_slash():
    fs = UserFS(home="/home/user")
    assert (
        fs.resolve_path("~/repos/homelab-dashboards/grafana/provisioning/dashboards/solar.json")
        == "/home/user/repos/homelab-dashboards/grafana/provisioning/dashboards/solar.json"
    )


def test_resolve_path_relative():
    fs = UserFS(home="/home/user")
    assert fs.resolve_path("repos/foo") == "/home/user/repos/foo"


def test_resolve_path_absolute_unchanged():
    fs = UserFS(home="/home/user")
    assert fs.resolve_path("/home/user/repos/foo") == "/home/user/repos/foo"


def test_resolve_path_tilde_with_session_cwd():
    fs = UserFS(home="/home/user")
    assert fs.resolve_path("solar.json", cwd="/home/user/repos/homelab-dashboards") == (
        "/home/user/repos/homelab-dashboards/solar.json"
    )


def test_resolve_path_multi_user_rewrites_home_user_after_tilde():
    fs = UserFS(username="alice", home="/home/alice")
    assert fs.resolve_path("~/repos/foo") == "/home/alice/repos/foo"


def test_resolve_path_multi_user_rewrites_literal_home_user_path():
    fs = UserFS(username="alice", home="/home/alice")
    assert fs.resolve_path("/home/user/repos/foo") == "/home/alice/repos/foo"
