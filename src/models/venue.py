from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime,timedelta,date,time
import uuid
from database.database import Base


#event_id
class VenueManagement(Base):
    __tablename__ = 'venue'
    id = Column(String(50), primary_key=True,default=str(uuid.uuid4()))
    name = Column(String(50),nullable=False)
    address = Column(String(250),nullable=False)
    capacity = Column(String(99999),nullable=False)
    contact_number = Column(String(10),nullable=False)
    availability = Column(Boolean)
    cost = Column(String(999999),nullable=False)
    facility = Column(String(999),nullable=False)
    is_deleted = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,default=datetime.now)
    modified_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)