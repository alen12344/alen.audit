from alen.core.models import Evidence
from datetime import datetime

class EvidenceCollector:
    def __init__(self):
        self.evidence_log = []

    def collect(self, source: str, data: any):
        evidence = Evidence(source=source, data=data, timestamp=datetime.now().isoformat())
        self.evidence_log.append(evidence)
        return evidence
