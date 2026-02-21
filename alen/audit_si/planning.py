class AuditPlanning:
    """IS Audit Planning Phase."""
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.status = "Initiated"

    def define_objectives(self, objectives: list[str]):
        self.objectives = objectives
        return f"Objectives defined for {self.project_name}"
