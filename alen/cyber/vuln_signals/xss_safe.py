import urllib.parse
from alen.core.http import HTTPClient

class XSSChecker:
    def __init__(self):
        self.http = HTTPClient()

    def check(self, target_url: str) -> bool:
        # Very basic Reflected XSS check signal
        payload = "<script>alert('XSS')</script>"
        encoded = urllib.parse.quote(payload)
        
        test_url = f"{target_url}?q={encoded}"
        try:
            resp = self.http.get(test_url)
            if resp and payload in resp.text:
                return True
            return False
        except Exception:
            return False
