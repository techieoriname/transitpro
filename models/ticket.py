from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
import uuid

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4))
    bus_id = Column(String, ForeignKey("buses.id"), nullable=False)
    passenger_name = Column(String, nullable=False)
    seat_number = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)


