from pydantic import BaseModel
from datetime import datetime

class BeerOut(BaseModel):
    id: int
    name: str 
    styler: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date : datetime
