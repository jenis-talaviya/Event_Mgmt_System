from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime,timedelta,date,time
import uuid
from database.database import Base


class Logistic_operation(Base):
    __tablename__ = 'logistic'
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    setup_breakdown = Column(String(50), nullable=False)
    staffing_volunteers = Column(String(50), nullable=False)
    security_safety = Column(String(50), nullable=False)
    transportation_parking = Column(String(50), nullable=False)
    signage_directions = Column(String(50), nullable=False)
    is_deleted = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,default=datetime.now)
    modified_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    