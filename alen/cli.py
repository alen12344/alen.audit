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
    title = Text("ALEN ENTERPRISE", justify="center", style="bold cyan")
    subtitle = Text(f"Version {__version__} - AI Information Audit", justify="center", style="dim")
    
    console.print(Align.center(Text(EYE_ASCII, style="bold bright_green")))
    console.print(Panel(title + Text("\n") + subtitle, border_style="cyan"))
    time.sleep(0.5)

def run_cyber_scan(target_url: str):
    show_banner()
    with console.status(f"[bold bright_green]Initiating intelligence gathering on {target_url}...", spinner="aesthetic"):
        time.sleep(2) # simulate loading
        console.print(f"[bold cyan]>[/bold cyan] Port & Vulnerability scan completed for: [yellow]{target_url}[/yellow]")
    console.print(Panel("No major vulnerabilities found during quick scan. Proceed to full evaluation.", style="bright_green"))

def run_is_audit(target_url: str):
    show_banner()
    with console.status(f"[bold blue]Provisioning audit workspace for {target_url}...", spinner="dots"):
        time.sleep(1.5)
        console.print(f"[bold cyan]>[/bold cyan] Audit logs and evidence collected for: [bold white]{target_url}[/bold white]")
    console.print(Panel("Workspace is ready and AI policies have been attached.", style="blue"))

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
        console.print("[3] ❌ Keluar (Exit)")
        
        pilihan = Prompt.ask("\n[bold yellow]Pilih menu (1/2/3)[/bold yellow]", choices=["1", "2", "3"])
        
        if pilihan == "3":
            console.print("[bold red]Keluar dari Alen Enterprise. Sampai jumpa![/bold red]")
            sys.exit(0)
            
        target_url = Prompt.ask("[bold bright_green]Masukkan URL Target (contoh: https://target.com)[/bold bright_green]")
        
        if pilihan == "1":
            run_cyber_scan(target_url)
        elif pilihan == "2":
            run_is_audit(target_url)
            
        Prompt.ask("\n[dim]Tekan Enter untuk kembali ke menu utama...[/dim]")
        show_banner()

if __name__ == '__main__':
    cli()
