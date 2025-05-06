from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import route as route_model
from schemas import route as route_schema
from typing import List, Optional 

router = APIRouter()

@router.post("/", response_model=route_schema.RouteRead)
def create_route(route: route_schema.RouteCreate, db: Session = Depends(get_db)):
    new_route = route_model.Route(**route.dict())
    db.add(new_route)
    db.commit()
    db.refresh(new_route)
    return new_route

@router.get("/", response_model=List[route_schema.RouteRead])
def list_routes(db: Session = Depends(get_db)):
    routes = db.query(route_model.Route).all()
    return routes
