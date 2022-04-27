from curses import beep
from typing import List
from fastapi import FastAPI
from beerlog.core import get_beer_from_database
from beerlog.models import Beer
api = FastAPI(title="beerlog")

@api.get("/beer/", response_model=List[Beer])
def list_beers():
    beers = get_beer_from_database()
    return beers
