from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime,timedelta,date,time
import uuid
from database.database import Base


class Catering(Base):
    __tablename__ = 'catering'
    id = Column(String(50), primary_key=True,default=str(uuid.uuid4()))
    name = Column(String(50),nullable=False)
    address = Column(String(250),nullable=False)
    email = Column(String(50),nullable=False)
    contact_number = Column(String(10),nullable=False)
    availability = Column(Boolean)
    cost = Column(String(50),nullable=False)
    is_deleted = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,default=datetime.now)
    modified_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    
    
class DecorationandFloralarrangment(Base):
    __tablename__ = 'decoandfloral'
    id = Column(String(50), primary_key=True,default=str(uuid.uuid4()))
    name = Column(String(50),nullable=False)
    address = Column(String(250),nullable=False)
    email = Column(String(50),nullable=False)
    contact_number = Column(String(10),nullable=False)
    availability = Column(Boolean)
    cost = Column(String(50),nullable=False)
    is_deleted = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,default=datetime.now)
    modified_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    
    
class Audio_visualEquipment(Base):
    __tablename__ = 'audio_visual'
    id = Column(String(50), primary_key=True,default=str(uuid.uuid4()))
    name = Column(String(50),nullable=False)
    address = Column(String(250),nullable=False)
    email = Column(String(50),nullable=False)
    contact_number = Column(String(10),nullable=False)
    availability = Column(Boolean)
    cost = Column(String(50),nullable=False)
    is_deleted = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,default=datetime.now)
    modified_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)



class Entertainment(Base):
    __tablename__ = 'entertainment'
    id = Column(String(50), primary_key=True,default=str(uuid.uuid4()))
    name = Column(String(50),nullable=False)
    address = Column(String(250),nullable=False)
    email = Column(String(50),nullable=False)
    contact_number = Column(String(10),nullable=False)
    availability = Column(Boolean)
    cost = Column(String(50),nullable=False)
    is_deleted = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,default=datetime.now)
    modified_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    
    
class Photo_video_graphy(Base):
    __tablename__ = 'photo_video_graphy'
    id = Column(String(50), primary_key=True,default=str(uuid.uuid4()))
    name = Column(String(50),nullable=False)
    address = Column(String(250),nullable=False)
    email = Column(String(50),nullable=False)
    contact_number = Column(String(10),nullable=False)
    availability = Column(Boolean)
    cost = Column(String(50),nullable=False)
    is_deleted = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,default=datetime.now)
    modified_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    
    
class Transportation(Base):
    __tablename__ = 'transportation'
    id = Column(String(50), primary_key=True,default=str(uuid.uuid4()))
    name = Column(String(50),nullable=False)
    address = Column(String(250),nullable=False)
    email = Column(String(50),nullable=False)
    contact_number = Column(String(10),nullable=False)
    availability = Column(Boolean)
    cost = Column(String(50),nullable=False)
    is_deleted = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,default=datetime.now)
    modified_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)