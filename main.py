from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from schemas import Property, PropertyCreate, Booking, BookingCreate, Review, ReviewCreate, Message, MessageCreate
from crud import (create_property, get_property, get_properties, update_property, delete_property,
                 search_properties, create_booking, create_review, get_reviews, create_message, get_messages)
from typing import List

app = FastAPI()
Base.metadata.create_all(bind=engine)

# Property CRUD
@app.post("/api/properties/", response_model=Property)
def create_property_endpoint(property: PropertyCreate, db: Session = Depends(get_db)):
    return create_property(db, property)

@app.get("/api/properties/{property_id}", response_model=Property)
def read_property(property_id: int, db: Session = Depends(get_db)):
    db_property = get_property(db, property_id)
    if not db_property:
        raise HTTPException(status_code=404, detail="Property not found")
    return db_property

@app.get("/api/properties/", response_model=List[Property])
def read_properties(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_properties(db, skip, limit)

@app.put("/api/properties/{property_id}", response_model=Property)
def update_property_endpoint(property_id: int, property: PropertyCreate, db: Session = Depends(get_db)):
    db_property = update_property(db, property_id, property.model_dump())  # Updated: dict() to model_dump()
    if not db_property:
        raise HTTPException(status_code=404, detail="Property not found")
    return db_property

@app.delete("/api/properties/{property_id}")
def delete_property_endpoint(property_id: int, db: Session = Depends(get_db)):
    db_property = delete_property(db, property_id)
    if not db_property:
        raise HTTPException(status_code=404, detail="Property not found")
    return {"message": "Property deleted"}

# Search
@app.get("/api/properties/search/", response_model=List[Property])
def search_properties_endpoint(location: str = None, min_price: float = None, max_price: float = None, db: Session = Depends(get_db)):
    return search_properties(db, location, min_price, max_price)

# Booking
@app.post("/api/bookings/", response_model=Booking)
def create_booking_endpoint(booking: BookingCreate, db: Session = Depends(get_db)):
    try:
        return create_booking(db, booking)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Review (Optional)
@app.post("/api/properties/{property_id}/reviews/", response_model=Review)
def create_review_endpoint(property_id: int, review: ReviewCreate, db: Session = Depends(get_db)):
    review.property_id = property_id
    return create_review(db, review)

@app.get("/api/properties/{property_id}/reviews/", response_model=List[Review])
def read_reviews(property_id: int, db: Session = Depends(get_db)):
    return get_reviews(db, property_id)

# Chat (Optional - Simplified, no WebSocket)
@app.post("/api/messages/", response_model=Message)
def create_message_endpoint(message: MessageCreate, db: Session = Depends(get_db)):
    return create_message(db, message)

@app.get("/api/messages/{booking_id}", response_model=List[Message])
def read_messages(booking_id: int, db: Session = Depends(get_db)):
    return get_messages(db, booking_id)