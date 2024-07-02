from fastapi import FastAPI,HTTPException,APIRouter,Depends,Header
from database.database import SessionLocal
from src.models.evendetail import EventDetail
from src.schemas.userschemas import EventDetails,EventDetailsUpdate
import uuid
from datetime import datetime,timedelta


event = APIRouter()
db = SessionLocal()



