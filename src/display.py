from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box
from models import PaletteResult

console = Console()

def render_swatch(hex_code: str) -> Text:
    text = Text()
    text.append(f"  {hex_code}  ", style=f"bold on {hex_code}")
    return text

def display_palette(result: PaletteResult):
    console.print()
    console.rule("[bold magenta]🎨 COLORISTA[/bold magenta]")
    console.print(f"[dim]  {result.image_path}[/dim]\n")

    table = Table(box=box.SIMPLE, show_header=False, padding=(0, 1))

    for i, color in enumerate(result.colors):
        label = "[bold]PRIMARY[/bold]" if i == 0 else f"COLOR {i+1}"
        swatch = render_swatch(color.hex_code)
        emotions = ", ".join(color.emotions)
        vibe = " · ".join(color.vibe)
        table.add_row(
            label,
            swatch,
            f"[cyan]{emotions}[/cyan]",
            f"[yellow]{vibe}[/yellow]"
        )

    console.print(table)

    if result.description:
        console.print(Panel(
            result.description,
            title="[bold]El Colorista Says[/bold]",
            border_style="cyan"
        ))

    console.print()