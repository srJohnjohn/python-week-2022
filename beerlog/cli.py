from tomlkit import table
import typer
from typing import Optional
from beerlog.core import add_beer_to_database, get_beers_from_database
import sys
from .config import settings
from rich.table import Table
from rich.console import Console

main = typer.Typer(help="Beer managent application")
console = Console()


@main.command("add")
def add(
        name: str, 
        styler: str,
        flavor: int = typer.Option(...),
        image: int = typer.Option(...),
        cost: int = typer.Option(...),
        ):
    """add a new beer to database"""
    if add_beer_to_database(name, styler, flavor, image, cost):
        print("beer added in database")    
    else:
        print("nao deu")

    print(name, styler)

@main.command("list")
def list_beers(styler: Optional[str] = None):
    """list beer in data base"""
    beers = get_beers_from_database()
    table = Table(title="beerlog")
    headers = ["id", "name", "styler", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)


