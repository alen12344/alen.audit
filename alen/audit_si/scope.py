class AuditScope:
    def __init__(self, target_systems: list[str]):
        self.systems = target_systems

    def is_in_scope(self, system: str) -> bool:
        return system in self.systems
