import json
import logging
import re
from typing import Optional, Dict
from pathlib import Path

logger = logging.getLogger("LogosRules")


class RulesLayer:
    def __init__(self, language: str = "en"):
        self.commands = self.load_commands()
        self.language = language

    def _load_commands(self):
        config_path = Path(__file__).parent.parent / "config" / "commands.json"
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def set_language(self, lang: str):
        if lang in ["fr", "en", "ja"]:
            self.language = lang
        else:
            raise ValueError("Language not supported : {lang}")

    def parse(self, text: str) -> Optional[Dict]:
        logger.info(f"Language : {self.language}")
        logger.info("Starting rules parsing process")

        text = text.lower().strip()
        print(text)

        for cmd in self.commands:
            action = cmd.get("action")
            target = cmd.get("target")
            param_name = cmd.get("param_name")

            keywords = cmd.get("keywords", {}).get(self.language, [])
            print(keywords)

            for kw in keywords:
                if kw.lower() in text:
                    return {
                        "action": action,
                        "target": target,
                        "param_name": None,
                        "param": None,
                    }

            patterns = cmd.get("patterns", {}).get(self.language, [])
            for pattern in patterns:
                match = re.search(pattern, text)
                if match:
                    param = match.group(1) if match.groups() else None
                    return {
                        "action": action,
                        "target": target,
                        "param_name": param_name,
                        "param": param,
                    }
                
        return None
