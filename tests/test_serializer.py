import json
from datetime import datetime
from uuid import uuid4
from alen.core.serializer import to_json

def test_json_encoder():
    dt = datetime(2024, 1, 1, 12, 0, 0)
    uId = uuid4()
    
    data = {
        "timestamp": dt,
        "session_id": uId,
        "name": "Audit_Result"
    }
    
    result = to_json(data)
    parsed = json.loads(result)
    
    assert parsed["timestamp"] == "2024-01-01T12:00:00"
    assert parsed["session_id"] == str(uId)
    assert parsed["name"] == "Audit_Result"
