from typing import Optional, Dict


class LLMLayer:
    def parse(self, text: str) -> Optional[Dict]:
        # Ici, on branchera un LLM (local ou API)
        # Pour l’instant on renvoie None pour simuler le fallback
        return None
