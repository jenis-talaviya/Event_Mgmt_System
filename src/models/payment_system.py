from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime,timedelta,date,time
import uuid
from database.database import Base



class Payment(Base):
    __tablename__ = 'payment'
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    user_id = Column(String(50), ForeignKey('users.id'), nullable=False)
    event_id = Column(String(50), ForeignKey('event.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    payment_status = Column(String(50), nullable=False)
    transaction_id = Column(String(100), default=str(uuid.uuid4()),nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)