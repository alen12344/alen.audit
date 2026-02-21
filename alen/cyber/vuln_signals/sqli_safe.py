import urllib.parse
from alen.core.http import HTTPClient

class SQLiChecker:
    def __init__(self):
        self.http = HTTPClient()

    def check(self, target_url: str) -> bool:
        # Very basic SQLi quote check
        payload = "'"
        encoded = urllib.parse.quote(payload)
        
        test_url = f"{target_url}?id={encoded}"
        try:
            resp = self.http.get(test_url)
            if resp and any(err in resp.text.lower() for err in ["sql syntax", "mysql", "ora-"]):
                return True
            return False
        except Exception:
            return False
