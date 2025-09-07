import pytest
from src.parser.layers import regex_parser


parser = regex_parser.RegexLayer(language="en")


@pytest.mark.parametrize(
    "text, expected",
    [
        (
            "open chrome",
            {
                "action": "open",
                "target": "browser",
                "param_name": "app",
                "param": "chrome",
            },
        ),
        ("stop", {"action": "stop", "target": None, "param_name": None, "param": None}),
        (
            "play Look to Windward",
            {
                "action": "play",
                "target": "music",
                "param_name": "track",
                "param": "look to windward",
            },
        ),
        (
            "set timer for 12 minutes",
            {
                "action": "set",
                "target": "timer",
                "param_name": "duration",
                "param": "12",
            },
        ),
    ],
)
def test_parser(text, expected):
    result = parser.parse(text)
    assert result == expected
