from sqlalchemy.orm import Session
from models import Property, Booking, Review, Message
from schemas import PropertyCreate, BookingCreate, ReviewCreate, MessageCreate
from datetime import datetime

# Property CRUD
def create_property(db: Session, property: PropertyCreate):
    db_property = Property(**property.model_dump())  # Updated: dict() to model_dump()
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

def get_property(db: Session, property_id: int):
    return db.query(Property).filter(Property.id == property_id).first()

def get_properties(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Property).offset(skip).limit(limit).all()

def update_property(db: Session, property_id: int, property_data: dict):
    db_property = get_property(db, property_id)
    if db_property:
        for key, value in property_data.items():
            setattr(db_property, key, value)
        db.commit()
        db.refresh(db_property)
    return db_property

def delete_property(db: Session, property_id: int):
    db_property = get_property(db, property_id)
    if db_property:
        db.delete(db_property)
        db.commit()
    return db_property

# Search
def search_properties(db: Session, location: str = None, min_price: float = None, max_price: float = None):
    query = db.query(Property)
    if location:
        query = query.filter(Property.location.ilike(f"%{location}%"))
    if min_price:
        query = query.filter(Property.price >= min_price)
    if max_price:
        query = query.filter(Property.price <= max_price)
    return query.all()

# Booking
def create_booking(db: Session, booking: BookingCreate):
    # Simple availability check (no overlapping bookings)
    existing = db.query(Booking).filter(
        Booking.property_id == booking.property_id,
        Booking.start_date < booking.end_date,
        Booking.end_date > booking.start_date
    ).first()
    if existing:
        raise ValueError("Property is already booked for these dates")
    db_booking = Booking(**booking.model_dump())  # Updated: dict() to model_dump()
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

# Review (Optional)
def create_review(db: Session, review: ReviewCreate):
    db_review = Review(**review.model_dump())  # Updated: dict() to model_dump()
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_reviews(db: Session, property_id: int):
    return db.query(Review).filter(Review.property_id == property_id).all()

# Chat (Optional)
def create_message(db: Session, message: MessageCreate):
    db_message = Message(**message.model_dump())  # Updated: dict() to model_dump()
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_messages(db: Session, booking_id: int):
    return db.query(Message).filter(Message.booking_id == booking_id).order_by(Message.timestamp).all()