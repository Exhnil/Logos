import json
import os
import sys
from typing import Dict
from pathlib import Path
import logging

logger = logging.getLogger("LogosExecutor")


class Executor:
    def __init__(self, app_path: Path = None):
        if app_path is None:
            app_path = (
                Path(__file__).parent.parent / "executor" / "config" / "apps.json"
            )

        try:
            with open(app_path, "r", encoding="utf-8") as f:
                self.apps: Dict[str, str] = json.load(f)
        except Exception as e:
            logger.exception(f"Failed to load apps.json: {e}")
            self.apps = {}

    def execute(self, command: Dict):
        action = command.get("action")
        target = command.get("target")
        param_name = command.get("param_name")
        param = command.get("param")

        if not action:
            logger.error(f"Invalid command: {command}")
            return

        if target:
            method_name = f"_{action}_{target}"
        else:
            method_name = f"_{action}"

        method = getattr(self, method_name, None)

        if not method:
            logger.error(f"No executor method for '{method_name}'")
            return

        try:
            logger.info(f"Executing {method_name} with {param_name}={param}")
            return method(param)
        except Exception as e:
            logger.exception(f"Execution failed for {method_name}: {e}")

    def _open_browser(self, param):
        # Ex: param = "chrome"
        app_path = self.apps.get(param)
        if not app_path:
            logger.error(f"Unknown app '{param}'")
            return

        logger.info(f"Opening browser: {param} -> {app_path}")
        if sys.platform.startswith("win"):
            os.startfile(app_path)

    def _play_music(self, param):
        # param_name = "track", param = "song name"
        logger.info(f"Playing music track: {param}")
        # Ici ça pourrait appeler Spotify API plus tard

    def _get_weather_weather(self, param):
        logger.info(f"Fetching weather for {param}")

    def _set_alarm(self, param):
        logger.info(f"Setting alarm at {param}")

    def _set_timer(self, param):
        logger.info(f"Setting timer for {param} minutes")

    def _search(self, param):
        logger.info(f"Searching for query: {param}")
        # Exemple: ouvrir une recherche Google
        if sys.platform.startswith("win"):
            os.startfile(f"https://www.google.com/search?q={param}")

    def _stop(self, param):
        logger.info("Stopping last active media app")

    def _volume_up(self, param):
        logger.info("Increasing system volume")

    def _volume_down(self, param):
        logger.info("Decreasing system volume")