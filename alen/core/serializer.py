import json
from datetime import datetime
from uuid import UUID

class CustomEncoder(json.JSONEncoder):
    """JSON Encoder for safely serializing complex types."""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, UUID):
            return str(obj)
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)

def to_json(data):
    """Convert dict to safely formatted JSON string."""
    return json.dumps(data, cls=CustomEncoder, indent=2)
