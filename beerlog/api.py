
from typing import List, Optional
from urllib import response
from fastapi import FastAPI, Response, status
from beerlog.core import get_beers_from_database
from beerlog.models import Beer
from beerlog.serializers import BeerOut, BeerIn
from beerlog.database import get_session

api = FastAPI(title="beerlog")

@api.get("/beer", response_model=List[BeerOut])
def list_beers(styler: Optional[str] = None):
    beers = get_beers_from_database(styler)
    return beers

@api.post("/beers", response_model=BeerOut)
def add_beer(beer_in : BeerIn, response: Response):
    beer = Beer(**beer_in.dict())
    with get_session() as session:
        session.add(beer)
        session.commit()
        session.refresh(beer)

    response.status_code = status.HTTP_201_CREATED
    return beer