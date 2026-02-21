import nmap
import json
from alen.core.policy import PolicyEnforcer

class PortScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()

    def scan(self, target: str, ports: str = 'top100') -> str:
        if not PolicyEnforcer.is_in_scope(target):
            return f"Error: Target {target} is out of authorized scope."
            
        args = '-sV -sC' if ports == 'top100' else f'-p {ports} -sV'
        try:
            self.nm.scan(target, arguments=args)
            
            # Simple wrapper to return scan data as JSON-ish string
            scan_data = {}
            for host in self.nm.all_hosts():
                scan_data[host] = {'state': self.nm[host].state()}
                for proto in self.nm[host].all_protocols():
                    scan_data[host][proto] = {}
                    lport = self.nm[host][proto].keys()
                    for port in lport:
                        scan_data[host][proto][port] = self.nm[host][proto][port]
            
            return json.dumps(scan_data, indent=2)
        except Exception as e:
            return f"Scan failed: {str(e)}"
