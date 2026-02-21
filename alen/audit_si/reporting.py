from alen.core.models import AuditReport

class ReportGenerator:
    def generate(self, report_data: AuditReport) -> str:
        # Generate basic SI Audit internal report structure
        return f"Audit Report for {report_data.project_name} generated."
