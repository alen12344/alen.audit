import click
import time
import sys
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.prompt import Prompt
from alen import __version__
from alen.config.settings import settings
import urllib.parse
import json
from alen.cyber.scanner import PortScanner
from alen.cyber.api_surface import APISurfaceAnalyzer
from alen.cyber.vuln_signals.sqli_safe import SQLiChecker
from alen.cyber.vuln_signals.xss_safe import XSSChecker
from alen.ai.orchestrator import AIOrchestrator
from alen.reporting.builder import ReportBuilder
from alen.audit_si.evidence_collect import EvidenceCollector
import os
console = Console()

EYE_ASCII = """
      .:::.          .:::.      
     :::::::.      .:::::::     
     :::::::::    :::::::::     
    :::::::::::  :::::::::::    
     :::::::::    :::::::::     
      ':::::'      ':::::'      
           ..::::::..
         .::::::::::::.
        ::::::::::::::::
        ::::::::::::::::
         '::::::::::::'
           ''::::::''
"""

def show_banner():
    console.clear()
    sys.stdout.write('\a') # System beep sound for cyber feel
    title = Text("ALEN ENTERPRISE", justify="center", style="bold cyan")
    subtitle = Text(f"Version {__version__} - AI Information Audit", justify="center", style="dim")
    
    console.print(Align.center(Text(EYE_ASCII, style="bold bright_green")))
    console.print(Panel(title + Text("\n") + subtitle, border_style="cyan"))
    time.sleep(0.5)

def run_cyber_scan(target_url: str):
    show_banner()
    domain = urllib.parse.urlparse(target_url).hostname or target_url
    
    scanner = PortScanner()
    api_analyzer = APISurfaceAnalyzer()
    sqli_checker = SQLiChecker()
    xss_checker = XSSChecker()
    ai_orch = AIOrchestrator()
    report_builder = ReportBuilder()

    with console.status(f"[bold bright_green]Initiating intelligence gathering on {target_url}...", spinner="aesthetic"):
        scan_results = scanner.scan(domain)
        api_results = api_analyzer.discover(target_url)
        sqli_result = sqli_checker.check(target_url)
        xss_result = xss_checker.check(target_url)
        
        raw_data = f"Port Scan:\n{scan_results}\n\nAPI Surface:\n{json.dumps(api_results)}\n\nSQLi Signal:\n{sqli_result}\n\nXSS Signal:\n{xss_result}"
        console.print(f"[bold cyan]>[/bold cyan] Port & Vulnerability scan completed for: [yellow]{target_url}[/yellow]")

    with console.status("[bold bright_green]Processing findings with Gemini AI...", spinner="aesthetic"):
        ai_analysis = ai_orch.process_cyber_scan(raw_data)
        
    findings = [
        {"title": "Open Ports & Services", "description": "Raw data analyzed by AI", "severity": "Info"},
        {"title": "API Surface", "description": f"Found {len(api_results)} possible endpoints.", "severity": "Info"},
        {"title": "SQLi Signal", "description": f"Potential SQLi: {sqli_result}", "severity": "High" if sqli_result else "Low"},
        {"title": "XSS Signal", "description": f"Potential Reflected XSS: {xss_result}", "severity": "High" if xss_result else "Low"}
    ]

    html_report = report_builder.build_html(f"Cyber Scan: {target_url}", findings, ai_analysis)
    with open("output_report.html", "w", encoding="utf-8") as f:
        f.write(html_report)
        
    console.print(Panel("Scan complete! Report saved to [bold]output_report.html[/bold]", style="bright_green"))

def run_is_audit(target_url: str):
    show_banner()
    evidence_collector = EvidenceCollector()
    ai_orch = AIOrchestrator()
    report_builder = ReportBuilder()

    with console.status(f"[bold blue]Provisioning audit workspace for {target_url}...", spinner="dots"):
        time.sleep(1)
        console.print(f"[bold cyan]>[/bold cyan] Workspace is ready.")
        
    evidence_text = Prompt.ask("\n[bold yellow]Masukkan data/bukti audit untuk dianalisis (misal: 'Password policy minimal 8 karakter')[/bold yellow]")

    with console.status("[bold blue]Analyzing evidence with Gemini AI...", spinner="dots"):
        evidence_collector.collect(target_url, evidence_text)
        ai_analysis = ai_orch.process_is_evidence(evidence_text)

    findings = [
        {"title": "Evidence Analisa", "description": evidence_text, "severity": "Info"}
    ]

    html_report = report_builder.build_html(f"IS Audit: {target_url}", findings, ai_analysis)
    with open("output_report.html", "w", encoding="utf-8") as f:
        f.write(html_report)

    console.print(Panel("Audit complete! Report saved to [bold]output_report.html[/bold]", style="blue"))

@click.command()
@click.version_option(version=__version__)
def cli():
    """Alen Enterprise: AI-Powered Information Systems Audit Tool."""
    show_banner()
    
    if not settings.GEMINI_API_KEY:
        console.print("[bold yellow]⚠️  API Key Gemini belum dikonfigurasi![/bold yellow]")
        console.print("Dapatkan API Key gratis di: [cyan]https://aistudio.google.com/[/cyan]")
        api_key = Prompt.ask("\n[bold bright_green]Masukkan API Key Gemini Anda[/bold bright_green]", password=True)
        if api_key:
            settings.save_api_key(api_key.strip())
            console.print("[bold green]✅ API Key berhasil disimpan untuk sesi selanjutnya![/bold green]")
            time.sleep(1)
            show_banner()
        else:
            console.print("[bold red]API Key wajib diisi untuk menggunakan fitur AI. Keluar...[/bold red]")
            sys.exit(1)
            
    while True:
        console.print("\n[bold cyan]=== MENU UTAMA ALEN ===[/bold cyan]")
        console.print("[1] 🔍 Lakukan Cyber Security Scan")
        console.print("[2] 📋 Mulai Information System Audit")
        console.print("[3] 📄 Ekspor Laporan Terakhir ke PDF")
        console.print("[4] ❌ Keluar (Exit)")
        
        pilihan = Prompt.ask("\n[bold yellow]Pilih menu (1/2/3/4)[/bold yellow]", choices=["1", "2", "3", "4"])
        
        if pilihan == "4":
            console.print("[bold red]Keluar dari Alen Enterprise. Sampai jumpa![/bold red]")
            sys.exit(0)
            
        elif pilihan == "3":
            if not os.path.exists("output_report.html"):
                console.print("[bold red]Belum ada laporan HTML yang dibuat. Lakukan scan terlebih dahulu.[/bold red]")
            else:
                try:
                    import weasyprint
                    with console.status("[bold cyan]Generating PDF Report...", spinner="dots"):
                        weasyprint.HTML('output_report.html').write_pdf('output_report.pdf')
                        console.print(Panel("Export Success! Report saved to [bold]output_report.pdf[/bold]", style="bright_green"))
                except ImportError:
                    console.print("[bold red]Library weasyprint belum terinstall, tidak dapat membuat PDF.[/bold red]")
                except Exception as e:
                    console.print(f"[bold red]PDF Generation failed: {str(e)}[/bold red]")
            Prompt.ask("\n[dim]Tekan Enter untuk kembali ke menu utama...[/dim]")
            show_banner()
            continue
            
        target_url = Prompt.ask("[bold bright_green]Masukkan URL Target (contoh: https://target.com)[/bold bright_green]")
        
        if pilihan == "1":
            run_cyber_scan(target_url)
        elif pilihan == "2":
            run_is_audit(target_url)
            
        Prompt.ask("\n[dim]Tekan Enter untuk kembali ke menu utama...[/dim]")
        show_banner()

if __name__ == '__main__':
    cli()
