from src.executor.actions import Executor

executor = Executor()


def test_execute_open_browser(monkeypatch):
    called = {}

    def fake_open(param):
        called["browser"] = param

    executor._open_browser = fake_open

    cmd = {
        "action": "open",
        "target": "browser",
        "param_name": "app",
        "param": "chrome",
    }
    executor.execute(cmd)

    assert "browser" in called
    assert called["browser"] == ("chrome")


def test_execute_unknown(caplog):
    cmd = {
        "action": "foo",
        "target": None,
        "param_name": None,
        "param": None,
    }
    with caplog.at_level("ERROR"):
        executor.execute(cmd)

    assert "No executor method for '_foo'" in caplog.text
