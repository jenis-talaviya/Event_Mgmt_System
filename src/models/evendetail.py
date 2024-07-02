from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Time,Date
from datetime import datetime,timedelta,date
import uuid
from database.database import Base



class EventDetail(Base):
    __tablename__ = 'event'
    id = Column(String(50), primary_key=True, default=str(uuid.uuid4()))
    E_manager_id= Column(String(50),ForeignKey('manager.id'))
    E_venue_id = Column(String(50),ForeignKey('venue.id'),nullable=True)
    E_catering_id = Column(String(50),ForeignKey('catering.id'),nullable=True)
    E_decoandfloral_id = Column(String(50),ForeignKey('decoandfloral.id'),nullable=True)
    E_audiovisual_id = Column(String(50),ForeignKey('audio_visual.id'),nullable=True)
    E_entertainment_id = Column(String(50),ForeignKey('entertainment.id'),nullable=True)
    E_photoandvideography_id = Column(String(50),ForeignKey('photo_video_graphy.id'),nullable=True)
    E_transportation_id = Column(String(50),ForeignKey('transportation.id'),nullable=True)
    E_name = Column(String(50),nullable=False)
    E_venue = Column(String(50),nullable=False)
    E_date = Column(Date,nullable=False)
    E_time = Column(Time,nullable=False)
    E_location = Column(String(250),nullable=False)
    E_description = Column(String(250),nullable=False)
    E_guest_size = Column(Integer,nullable=False)
    E_price = Column(Integer,nullable=False)
    is_deleted = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,default=datetime.now)
    modified_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)