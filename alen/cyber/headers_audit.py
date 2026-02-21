from alen.core.http import HTTPClient
from alen.core.policy import PolicyEnforcer
import json

class HeaderAuditor:
    def __init__(self):
        self.http = HTTPClient()

    def audit(self, target_url: str) -> str:
        # Very basic extraction of domain from URL for policy check
        domain = target_url.split('//')[-1].split('/')[0]
        if ":" in domain:
            domain = domain.split(":")[0]

        if not PolicyEnforcer.is_in_scope(domain):
            return f"Error: Target {domain} is out of authorized scope."

        try:
            response = self.http.get(target_url)
            headers = dict(response.headers)
            
            # Simple check for missing security headers
            missing = []
            expected = ['Strict-Transport-Security', 'X-Content-Type-Options', 'X-Frame-Options', 'Content-Security-Policy']
            for header in expected:
                if header not in headers:
                    missing.append(header)
                    
            result = {
                "target": target_url,
                "status_code": response.status_code,
                "missing_headers": missing,
                "raw_headers": headers
            }
            return json.dumps(result, indent=2)
        except Exception as e:
            return f"Audit failed: {str(e)}"
