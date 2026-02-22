from alen.reporting.builder import ReportBuilder

rb = ReportBuilder()
findings = [
    {"title": "Cross Site Scripting", "severity": "High", "description": "Reflected XSS on /search", "remediation": "Escape input."}
]
html = rb.build_html('Full Test', findings, 'AI Analysis: Advanced testing completed.')

with open('test_report_advanced.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("SUCCESS")
