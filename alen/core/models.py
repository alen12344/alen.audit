from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class Evidence(BaseModel):
    source: str
    data: Any
    timestamp: str

class Finding(BaseModel):
    id: str
    title: str
    description: str
    severity: str
    remediation: Optional[str] = None
    evidence: List[Evidence] = []
    metadata: Dict[str, Any] = {}

class AuditReport(BaseModel):
    project_name: str
    findings: List[Finding]
    summary: Dict[str, Any]
