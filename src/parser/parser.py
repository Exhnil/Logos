import logging
from typing import Optional, Dict, List
from parser.layers.rules import RulesLayer
from parser.layers.interpreter import NLPLayer
from parser.layers.llm import LLMLayer

logger = logging.getLogger("LogosParser")

class ParserPipeline:
    def __init__(self, language: str, layers: Optional[List] = None):
        self.layers = layers or [
            RulesLayer(language),
            NLPLayer(),
            LLMLayer()
        ]

    def parse(self, text)->Optional[Dict]:
        logger.info("Starting parse")
        for layer in self.layers:
            result = layer.parse(text)
            if result is not None:
                logger.info(result)
                return result
        return None
