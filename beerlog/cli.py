import typing
from typing import Optional
from beerlog.core import add_beer_to_database, get_beer_from_database
from .config import settings

main = type.Typer(help="Beer managent application")

@main.command("add")
def add(
        name: str, 
        styler: str,
        flavor: int = typing.Optional(...),
        image: int = typing.Optional(...),
        cost: int = typing.Optional(...),
        ):
    """add a new beer to database"""
    if add_beer_to_database(name, styler, flavor, image, cost):
        print("beer added in database")    
    else:
        print("nao deu")

    print(name, styler)

@main.command("list")
def list_beers(styler: Option[str] = None):
    """list beer in data base"""
    beers = get_beer_from_database
