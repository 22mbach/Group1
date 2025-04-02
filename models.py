from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from database import Base

class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, index = True)
    description = Column(String)
    price = Column(Float)
    location = Column(String)
    host_id = Column(Integer)  # Simplified, no full user table for brevity

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key = True, index = True)
    property_id = Column(Integer, ForeignKey("properties.id"))
    user_id = Column(Integer)  # Simplified
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    total_cost = Column(Float)

class Review(Base):  # For optional feature
    __tablename__ = "reviews"
    id = Column(Integer, primary_key = True, index = True)
    property_id = Column(Integer, ForeignKey("properties.id"))
    user_id = Column(Integer)
    rating = Column(Integer)
    comment = Column(String)

class Message(Base):  # For optional chat feature
    __tablename__ = "messages"
    id = Column(Integer, primary_key = True, index = True)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    sender_id = Column(Integer)
    content = Column(String)
    timestamp = Column(DateTime)