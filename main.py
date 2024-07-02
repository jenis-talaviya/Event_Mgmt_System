from fastapi import FastAPI,APIRouter
from src.routers.userrouter import user_log
from src.routers.userrouter import otp_gen
from src.routers.userdetail import event
from src.routers.userdetail import manager
from src.routers.userdetail import venue
from src.routers.userdetail import status
from src.routers.userdetail import vendors
from src.routers.userdetail import payment

app = FastAPI()

app.include_router(user_log)
app.include_router(otp_gen)
app.include_router(event)
app.include_router(manager)
app.include_router(venue)
app.include_router(status)
app.include_router(vendors)
app.include_router(payment)