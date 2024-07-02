from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime,timedelta,date,time
import uuid
from database.database import Base

#event_id and id

class EvenStatus(Base):
    __tablename__ = 'status'
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    event_id = Column(String(50),ForeignKey ('event.id'))
    name = Column(String(50),nullable=False)
    status = Column(String(50),nullable=False)
    is_deleted = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,default=datetime.now)
    modified_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)