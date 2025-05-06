from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import bus as bus_model
from schemas import bus as bus_schema
from models import route as route_model
from typing import List

router = APIRouter()

@router.post("/", response_model=bus_schema.BusRead)
def create_bus(bus: bus_schema.BusCreate, db: Session = Depends(get_db)):
    if not db.query(route_model.Route).filter(route_model.Route.id == bus.route_id).first():
        raise HTTPException(status_code=404, detail="Route not found")
    new_bus = bus_model.Bus(**bus.dict())
    db.add(new_bus)
    db.commit()
    db.refresh(new_bus)
    return new_bus

@router.get("/", response_model=List[bus_schema.BusRead])
def list_buses(db: Session = Depends(get_db)):
    buses = db.query(bus_model.Bus).all()
    return buses


