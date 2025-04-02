from pydantic import BaseModel, ConfigDict  # Add ConfigDict import
from datetime import datetime

class PropertyBase(BaseModel):
    title: str
    description: str
    price: float
    location: str
    host_id: int

class PropertyCreate(PropertyBase):
    pass

class Property(PropertyBase):
    id: int
    model_config = ConfigDict(from_attributes=True)  # Updated: Use ConfigDict and from_attributes

class BookingBase(BaseModel):
    property_id: int
    user_id: int
    start_date: datetime
    end_date: datetime
    total_cost: float

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int
    model_config = ConfigDict(from_attributes=True)  # Updated

class ReviewBase(BaseModel):
    property_id: int
    user_id: int
    rating: int
    comment: str

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    model_config = ConfigDict(from_attributes=True)  # Updated

class MessageBase(BaseModel):
    booking_id: int
    sender_id: int
    content: str
    timestamp: datetime

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int
    model_config = ConfigDict(from_attributes=True)  # Updated