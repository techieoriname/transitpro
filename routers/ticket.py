from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import ticket as ticket_model
from models import bus as bus_model
from schemas import ticket as ticket_schema
from typing import List

router = APIRouter()

@router.post("/", response_model=ticket_schema.TicketRead)
def book_ticket(ticket: ticket_schema.TicketCreate, db: Session = Depends(get_db)):
    bus = db.query(bus_model.Bus).filter(bus_model.Bus.id == ticket.bus_id).first()
    if not bus:
        raise HTTPException(status_code=404, detail="Bus not Found")
    
    tickets_on_bus = db.query(ticket_model.Ticket).filter(ticket_model.Ticket.bus_id == ticket.bus_id).all()

    if any(t.seat_number == ticket.seat_number for t in tickets_on_bus):
        raise HTTPException(status_code=400, detail="Seat already booked")
    
    if len(tickets_on_bus) >= bus.capacity:
        raise HTTPException(Status_code=400, detail="Bus is fully booked")
    
    new_ticket = ticket_model.Ticket(**ticket.dict())
    db.add((new_ticket))
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

@router.get("/", response_model=List[ticket_schema.TicketRead])
def list_tickets(db: Session = Depends(get_db)):
    return db.query(ticket_model.Ticket).all()
