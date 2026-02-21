import httpx
from typing import Dict, Any, Optional
import time

class HTTPClient:
    """Wrapper around httpx with retry and timeout logic."""
    def __init__(self, retries: int = 3, timeout: int = 10):
        self.retries = retries
        self.timeout = timeout
        self.client = httpx.Client(timeout=self.timeout)

    def get(self, url: str, headers: Optional[Dict[str, str]] = None) -> Any:
        for attempt in range(self.retries):
            try:
                response = self.client.get(url, headers=headers)
                response.raise_for_status()
                return response
            except httpx.RequestError as exc:
                if attempt == self.retries - 1:
                    raise exc
                time.sleep(2 ** attempt)

    def close(self):
        self.client.close()
