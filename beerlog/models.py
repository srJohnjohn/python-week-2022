import re
from statistics import mean
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel import select
from pydantic import validator
from datetime import datetime

class Beer(SQLModel, table= True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str 
    styler: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date : datetime = Field(default_factory=datetime.now)


    @validator("flavor", "image", "cost")
    def validate_rating(cls, v, field):
        if v < 1 or v> 10:
            raise RuntimeError(f"{field.name} must between 1 and 10")
        return v


    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)

brewdog = Beer( name="bewdog", style="NEIPA", flavor=6, image=8, cost=8)
