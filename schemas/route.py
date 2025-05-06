from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class RouteBase(BaseModel):
    origin: str
    destination: str
    departure_time: datetime
    arrival_time: datetime

class RouteCreate(RouteBase):
    pass

class RouteRead(RouteBase):
    id: str

class Config:
    orm_mode = True    


