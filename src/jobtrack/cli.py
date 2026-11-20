import typer
from typing import Annotated
from jobtrack import __version__

app = typer.Typer()


def version_callback(value: bool) -> None:
    if value:
        print(f"jobtrack {__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option("--version", callback=version_callback, is_eager=True, help="Show the version and exit."),
    ] = False,
) -> None:
    """Track job postings from Greenhouse, Lever and Ashby."""

@app.command()
def save(url: str):
    """
    Not yet implemented
    """
    print("save")

@app.command("list")
def list_postings():
    """
    Not yet implemented
    """
    print("list postings")

@app.command()
def check():
    """
    Not yet implemented
    """
    print("check")
