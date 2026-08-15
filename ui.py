"""Handles UI using the textual framework"""

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Static
from rich.table import Table

from uptime import uptime
from memory import memory
from processes import get_processes

class ProcViewerApp(App):

    BINDINGS = [('d', 'toggle_dark', 'Toggle dark mode')]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app"""
        yield Header()
        yield ProccessWidget()
        yield Footer()

    def action_toggle_dark(self):
        """Toggles darkmode"""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

class ProccessWidget(Static):
    def on_mount(self) -> None:
        processes = get_processes()

        table = Table("PID", "Name", "State", "PPID", "Threads")

        for process in processes:
            table.add_row(str(process.pid), process.name, process.state, str(process.ppid), str(process.threads))

        self.update(table)

