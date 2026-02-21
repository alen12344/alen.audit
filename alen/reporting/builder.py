from jinja2 import Environment, FileSystemLoader
import os
from datetime import datetime

class ReportBuilder:
    def __init__(self, template_dir="templates"):
        # Resolve to actual directory where this file resides
        base_dir = os.path.dirname(os.path.abspath(__file__))
        template_path = os.path.join(base_dir, template_dir)
        self.env = Environment(loader=FileSystemLoader(template_path))

    def build_html(self, project_name: str, findings: list, ai_summary: str) -> str:
        template = self.env.get_template("report.html")
        return template.render(
            project_name=project_name,
            date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            findings=findings,
            ai_summary=ai_summary
        )
