from pydantic import BaseModel
from uuid import UUID

class TicketBase(BaseModel):
    bus_id: str
    passenger_name: str
    seat_number: str

class TicketCreate(TicketBase):
    pass

class TicketRead(TicketBase):
    id: str

class Config:
    orm_mode = True
    
