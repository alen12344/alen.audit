from alen.config.settings import settings
import ipaddress

class PolicyEnforcer:
    @staticmethod
    def is_in_scope(target: str) -> bool:
        if settings.POLICY_MODE == "relaxed":
            return True
        # In strict mode, only allow configured scopes
        allowed = settings.ALLOWED_SCOPES
        if target in allowed:
            return True
        try:
            target_ip = ipaddress.ip_address(target)
            for scope in allowed:
                try:
                    net = ipaddress.ip_network(scope)
                    if target_ip in net:
                        return True
                except ValueError:
                    pass
        except ValueError:
            pass
        return False

    @staticmethod
    def enforce_rate_limit(target: str):
        # Placeholder for rate limiting logic
        pass
