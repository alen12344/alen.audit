import click
import time
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from alen import __version__

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
    # Animated banner
    console.clear()
    title = Text("ALEN ENTERPRISE", justify="center", style="bold cyan")
    subtitle = Text(f"Version {__version__} - AI Information Audit", justify="center", style="dim")
    
    # Eye intro effect
    console.print(Align.center(Text(EYE_ASCII, style="bold bright_green")))
    console.print(Panel(title + Text("\n") + subtitle, border_style="cyan"))
    time.sleep(0.5)

@click.group(invoke_without_command=True)
@click.pass_context
@click.version_option(version=__version__)
def cli(ctx):
    """Alen Enterprise: AI-Powered Information Systems Audit Tool."""
    if ctx.invoked_subcommand is None:
        show_banner()
        click.echo(ctx.get_help())

@cli.group()
def cyber():
    """Cybersecurity scanning and analysis tools."""
    pass

@cyber.command()
@click.option('--target', required=True, help='Target IP, domain, or range (e.g., 127.0.0.1)')
@click.option('--ports', default='top100', help='Ports to scan (e.g., top100, custom range 80,443)')
def scan(target, ports):
    """Run a security scan against a target."""
    show_banner()
    with console.status(f"[bold bright_green]Initiating intelligence gathering on target {target}...", spinner="aesthetic"):
        time.sleep(2) # simulate loading
        # TODO: Integration with alen.cyber.scanner
        console.print(f"[bold cyan]>[/bold cyan] Cyber scan completed for target: [yellow]{target}[/yellow] (Ports: {ports})")
    console.print(Panel("No major vulnerabilities found during quick scan. Proceed to full evaluation.", style="bright_green"))

@cli.group()
def audit():
    """Information systems audit management lifecycle."""
    pass

@audit.command()
@click.option('--name', required=True, help='Name of the audit project.')
def init(name):
    """Initialize a new IS Audit planning and scope."""
    show_banner()
    with console.status("[bold blue]Provisioning audit workspace...", spinner="dots"):
        time.sleep(1.5)
        # TODO: Integration with alen.audit_si.planning
        console.print(f"[bold cyan]>[/bold cyan] Audit project created: [bold white]{name}[/bold white]")
    console.print(Panel("Workspace is ready and policies have been attached.", style="blue"))

if __name__ == '__main__':
    cli()
