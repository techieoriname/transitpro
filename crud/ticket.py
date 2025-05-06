from sqlalchemy.orm import Session
from models.ticket import Ticket
from models.bus import Bus
from schemas.ticket import TicketCreate
from fastapi import HTTPException


def book_ticket(db: Session, ticket_data: TicketCreate) -> Ticket:
    bus = db.query(Bus).filter(Bus.id == ticket_data.bus_id).first()
    if not bus:
        raise HTTPException(status_code=404, detail="Bus not found")

    existing_tickets = db.query(Ticket).filter(Ticket.bus_id == ticket_data.bus_id).all()

    if any(t.seat_number == ticket_data.seat_number for t in existing_tickets):
        raise HTTPException(status_code=400, detail="Seat already taken")

    if len(existing_tickets) >= bus.capacity:
        raise HTTPException(status_code=400, detail="Bus is full")

    ticket = Ticket(**ticket_data.dict())
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def get_tickets(db: Session):
    return db.query(Ticket).all()