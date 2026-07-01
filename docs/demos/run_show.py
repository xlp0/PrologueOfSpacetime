import sys
import os
import time
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()

DEMOS = {
    "1": {"title": "Slide 3: Arithmetic (CLM Scripting)", "script": "demos/slide3_arithmetic_demo.py", "type": "python"},
    "2": {"title": "Slide 5: Music (Observability)", "script": "demos/slide5_music_demo.json", "type": "text"},
    "3": {"title": "Slide 6: Astrobiology (Macro/Micro)", "script": "cat demos/slide6_astrobiology_manifest.md", "type": "shell"},
    "4": {"title": "Slide 10: The Engine (Titan Quorum)", "script": "demos/titan_dashboard.py", "type": "python"},
}

def print_menu():
    console.clear()
    console.print(Panel.fit("[bold cyan]PROLOGUE OF SPACETIME: DEMO ORCHESTRATOR[/bold cyan]", border_style="cyan"))
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=4)
    table.add_column("Demo Title")
    table.add_column("Type", justify="right")
    
    for key, demo in DEMOS.items():
        table.add_row(key, demo["title"], demo["type"])
    
    console.print(table)
    console.print("\n[dim]Press 'q' to quit.[/dim]")

def run_python_demo(script_path):
    console.print(f"\n[green]Running {script_path}...[/green]")
    try:
        subprocess.run([sys.executable, script_path], check=True)
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Error running demo:[/bold red] {e}")
    console.print("\n[dim]Press Enter to return to menu...[/dim]")
    input()

def show_text_demo(file_path):
    console.print(f"\n[green]Displaying {file_path}...[/green]")
    try:
        with open(file_path, "r") as f:
            content = f.read()
        console.print(Panel(content, title=file_path, border_style="blue"))
    except FileNotFoundError:
        console.print(f"[bold red]File not found:[/bold red] {file_path}")
    console.print("\n[dim]Press Enter to return to menu...[/dim]")
    input()

def run_shell_demo(command):
    console.print(f"\n[green]Executing: {command}...[/green]")
    os.system(command)
    console.print("\n[dim]Press Enter to return to menu...[/dim]")
    input()

def main():
    while True:
        print_menu()
        choice = Prompt.ask("Select a demo", choices=list(DEMOS.keys()) + ["q"], default="q")
        
        if choice == "q":
            console.print("[bold green]Exiting Demo Orchestrator. Good luck with the presentation![/bold green]")
            break
            
        demo = DEMOS[choice]
        if demo["type"] == "python":
            run_python_demo(demo["script"])
        elif demo["type"] == "text":
            show_text_demo(demo["script"])
        elif demo["type"] == "shell":
            run_shell_demo(demo["script"])

if __name__ == "__main__":
    try:
        import rich
        main()
    except ImportError:
        print("Please install requirements: pip install -r requirements.txt")
