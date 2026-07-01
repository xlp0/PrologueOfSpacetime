import time
import random
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich import box
from rich.text import Text

# Configuration for the 5 Titans
TITANS = [
    {"name": "Agent A (Llama 3.1 405B)", "role": "Synthesis", "color": "cyan"},
    {"name": "Agent B (DeepSeek-V3)", "role": "Retrieval", "color": "blue"},
    {"name": "Agent C (Nemotron-4 340B)", "role": "Verification", "color": "green"},
    {"name": "Agent D (Qwen-2.5 72B)", "role": "Nuance", "color": "magenta"},
    {"name": "Agent E (Mistral 8x22B)", "role": "Creativity", "color": "yellow"},
]

def generate_log_entry():
    actions = [
        "Analyzing MCard hash...",
        "Cross-referencing with Qdrant...",
        "Validating Type Theory constraints...",
        "Checking logical consistency...",
        "Reviewing pedagogical alignment...",
        "Detecting hallucination patterns...",
        "Synthesizing counter-arguments...",
        "Computing consensus score...",
    ]
    return random.choice(actions)

def make_layout() -> Layout:
    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=3)
    )
    layout["main"].split_row(
        Layout(name="left", ratio=2),
        Layout(name="right", ratio=3)
    )
    return layout

def generate_table(step: int) -> Table:
    table = Table(box=box.SIMPLE_HEAD)
    table.add_column("Titan Agent", style="bold")
    table.add_column("Role")
    table.add_column("Status", justify="center")
    table.add_column("Vote", justify="right")

    for i, titan in enumerate(TITANS):
        # Simulate status based on step
        if step < 2:
            status = "[dim]Waiting[/dim]"
            vote = "-"
        elif step < 5 + i:
            status = f"[{titan['color']}]Processing...[/{titan['color']}]"
            vote = "-"
        else:
            status = "[green]Ready[/green]"
            score = 9.0 + (random.random() * 0.9)
            vote = f"[{titan['color']}]{score:.1f}/10[/{titan['color']}]"

        table.add_row(
            f"[{titan['color']}]{titan['name']}[/{titan['color']}]",
            titan["role"],
            status,
            vote
        )
    return table

def run_dashboard():
    console = Console()
    layout = make_layout()
    
    layout["header"].update(
        Panel(Text("TITAN QUORUM CONSENSUS ENGINE | GIT WORKTREE PARALLEL EXECUTION", justify="center", style="bold white on blue"))
    )
    
    logs = []
    step = 0
    with Live(layout, refresh_per_second=4, screen=True):
        while step < 30:
            step += 1
            
            # Update Table
            layout["left"].update(
                Panel(generate_table(step), title="Agent Status", border_style="blue")
            )
            
            # Update Logs
            if random.random() < 0.4:
                agent = random.choice(TITANS)
                logs.append(f"[{agent['color']}]{agent['name']}: {generate_log_entry()}[/{agent['color']}]")
                if len(logs) > 12:
                    logs.pop(0)
            
            log_text = "\n".join(logs)
            layout["right"].update(
                Panel(log_text, title="Consensus Log Stream", border_style="green")
            )
            
            # Update Footer
            if step < 15:
                footer_text = "Status: [yellow]Negotiating Consensus...[/yellow]"
            elif step < 25:
                footer_text = "Status: [cyan]Finalizing Scores...[/cyan]"
            else:
                footer_text = "Status: [bold green]CONSENSUS REACHED (Avg: 9.4/10)[/bold green]"
                
            layout["footer"].update(
                Panel(footer_text, style="white")
            )
            
            time.sleep(0.3)
        
        time.sleep(2) # Hold final state

if __name__ == "__main__":
    try:
        run_dashboard()
    except ImportError:
        print("Please install 'rich': pip install rich")
