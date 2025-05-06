from pydantic import BaseModel
from uuid import UUID


class BusBase(BaseModel):
    plate_number: str
    capacity: int
    route_id: str

class BusCreate(BusBase):
    pass

class BusRead(BusBase):
    id: str

class config:
    orm_mode = True    