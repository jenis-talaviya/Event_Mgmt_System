from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime,timedelta,date,time
import uuid
from database.database import Base

class EventManager(Base):
    __tablename__ = 'manager'
    id = Column(String(50),primary_key=True,default=str(uuid.uuid4()))
    name = Column(String(50),nullable=False)
    contact_no = Column(String(10),nullable=False)
    is_deleted = Column(Boolean,default=True)
    is_active = Column(Boolean,default=False)
    created_at = Column(DateTime,default=datetime.now)
    modified_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)