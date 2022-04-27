from typing import Optional, List
from sqlmodel import select
from beerlog.config import settings
from beerlog.models import Beer
from beerlog.database import get_session

def add_beer_to_database(
    name: str,
    style: str,
    flavor: int,
    image: int,
    cost: int
) -> bool:
    with get_session() as session:
        beer = Beer(
            name=name,
            style=style,
            flavor=flavor,
            image=image,
            cost=cost
        )
        session.add(beer)
        session.commit()
    return True

def get_beers_from_database(styler: Optional[str] = None) -> List[Beer]:
    with get_session() as session:
        sql = select(Beer)
        if styler:
            sql = sql.where(Beer.styler == styler)
        return list(session.exec(sql))