from fastapi import FastAPI
from database import engine, Base
from routers import route, bus, ticket
from auth import routes as auth_routes


app = FastAPI(title="Bus Ticketing API",
    version="1.0.0",
    description="API for managing buses, routes, and ticket bookings")

# Create all tables in the database
# This needs to happen before the app starts handling requests
Base.metadata.create_all(bind=engine)

app.include_router(route.router, prefix="/api/v1/routes", tags=["Routes"])
app.include_router(bus.router, prefix="/api/v1/buses", tags=["Buses"])
app.include_router(ticket.router, prefix="/api/v1/tickets", tags=["Tickets"])
app.include_router(auth_routes.router, prefix="/api/v1/auth", tags=["Authentication"])

# If you need an endpoint to check if API is running
@app.get("/")
def read_root():
    return {"message": "Welcome to Bus Ticketing API"}