from alen.core.http import HTTPClient
from alen.core.policy import PolicyEnforcer

class APISurfaceAnalyzer:
    def __init__(self):
        self.http = HTTPClient()

    def discover(self, base_url: str) -> list[str]:
        # Very basic mock API discovery
        # In a real tool this would fuzz or parse OpenAPI specs
        domain = base_url.split('//')[-1].split('/')[0].split(":")[0]
        if not PolicyEnforcer.is_in_scope(domain):
            return []
            
        common_endpoints = ['/api/v1/health', '/api/v1/users', '/swagger.json', '/graphql']
        discovered = []
        
        for endpoint in common_endpoints:
            try:
                url = f"{base_url.rstrip('/')}{endpoint}"
                resp = self.http.get(url)
                if resp and resp.status_code < 400:
                    discovered.append(url)
            except Exception:
                pass
                
        return discovered
