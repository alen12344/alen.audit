from alen.ai.gemini_client import GeminiClient
from alen.ai.prompts import CYBER_AUDIT_PROMPT, IS_AUDIT_PROMPT
from alen.core.fp_killer import FalsePositiveKiller
from typing import Dict, Any, List

class AIOrchestrator:
    def __init__(self):
        self.gemini = GeminiClient()
        self.fp_killer = FalsePositiveKiller()

    def process_cyber_scan(self, raw_scan_data: str) -> str:
        """Process Raw Nmap/Cyber scan data and return AI explanation."""
        ai_analysis = self.gemini.analyze(CYBER_AUDIT_PROMPT, raw_scan_data)
        return ai_analysis

    def process_is_evidence(self, evidence_data: str) -> str:
        """Process IS Audit evidence against frameworks."""
        ai_analysis = self.gemini.analyze(IS_AUDIT_PROMPT, evidence_data)
        return ai_analysis
