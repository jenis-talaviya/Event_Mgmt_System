from fastapi import FastAPI,HTTPException,APIRouter,Depends,Header
from database.database import SessionLocal
from src.models.evendetail import EventDetail
from src.models.even_manager import EventManager
from src.models.vendors_supplier import Catering,DecorationandFloralarrangment,Audio_visualEquipment,Entertainment,Photo_video_graphy,Transportation
from src.models.logistics_operation import Logistic_operation
from src.models.venue import VenueManagement
from src.models.event_status import EvenStatus
from src.models.payment_system import Payment
from src.models.userdetail import UserDetail
from src.utils.otp import send_email
from src.schemas.userschemas import EventDetails,EventDetailsUpdate,EventManagers,ManagerUpdate,Caterings,Decorations,Audio_visuals,Entertainments,PhotoVideoGraphys,Transportations,Logistic_operations,Payments,VenueManagements,EvenStatuss,EventStatusUpdates,UpdateDetails,VendorsUpdateDetails,Logistic_operationsUpdates,PaymentResponse
import uuid
from datetime import datetime,timedelta
from src.utils.usertoken import get_event_token,decode_token_em_email,decode_token_em_id
from logs.log_config import logger


event = APIRouter()
db = SessionLocal()

@event.post("/event_detail",response_model=EventDetails)
def add_event(use:EventDetails):
    # breakpoint()
    logger.info("check manager id")
    manger = db.query(EventManager).filter(EventManager.id == use.E_manager_id).first()
    
    if manger is None:
        logger.error("manager detail is not found")
        raise HTTPException(status_code=404, detail='manager is not found')
    
    logger.info("toggle the condition")
    manger.is_active = True
    manger.is_deleted = False
    
    venues = db.query(VenueManagement).filter(VenueManagement.id == use.E_venue_id,VenueManagement.is_active == True).first()
    if venues is None:
        raise HTTPException(status_code=404, detail="venue id not available")
    
    venues.availability = False
    
    caters = db.query(Catering).filter(Catering.id == use.E_catering_id,Catering.is_active == True).first()
    if caters is None:
        raise HTTPException(status_code=404, detail="caters id not available")
    
    caters.availability = False
    
    Decor = db.query(DecorationandFloralarrangment).filter(DecorationandFloralarrangment.id == use.E_catering_id,DecorationandFloralarrangment.is_active == True).first()
    if Decor is None:
        raise HTTPException(status_code=404, detail="DecorationandFloralarrangment id not available")
    
    DecorationandFloralarrangment.availability = False
    
    audio_visual = db.query(Audio_visualEquipment).filter(Audio_visualEquipment.id == use.E_catering_id,Audio_visualEquipment.is_active == True).first()
    if audio_visual is None:
        raise HTTPException(status_code=404, detail="Audio_visualEquipment id not available")
    
    Audio_visualEquipment.availability = False
    
    entertain = db.query(Entertainment).filter(Entertainment.id == use.E_catering_id,Entertainment.is_active == True).first()
    if entertain is None:
        raise HTTPException(status_code=404, detail="Entertainment id not available")
    
    Entertainment.availability = False
    
    Photo_videography = db.query(Photo_video_graphy).filter(Photo_video_graphy.id == use.E_catering_id,Photo_video_graphy.is_active == True).first()
    if Photo_videography is None:
        raise HTTPException(status_code=404, detail="Photo_video_graphy id not available")
    
    Photo_video_graphy.availability = False
    
    transport = db.query(Transportation).filter(Transportation.id == use.E_catering_id,Transportation.is_active == True).first()
    if transport is None:
        raise HTTPException(status_code=404, detail="Transportation id not available")
    
    Transportation.availability = False
    
    logger.info("add event detail")
    new_event = EventDetail(
    E_manager_id = use.E_manager_id,
    E_venue_id = use.E_venue_id,
    E_catering_id = use.E_catering_id,
    E_decoandfloral_id = use.E_decoandfloral_id,
    E_audiovisual_id = use.E_audiovisual_id,
    E_entertainment_id = use.E_entertainment_id,
    E_photoandvideography_id = use.E_photoandvideography_id,
    E_transportation_id = use.E_transportation_id,
    E_name = use.E_name,
    E_venue = use.E_venue,
    E_date = use.E_date,
    E_time = use.E_time,
    E_location = use.E_location,
    E_description = use.E_description,
    E_guest_size = use.E__guest_size,
    E_price = use.E_price
    )
    logger.info("add event detail")
    db.add(new_event)
    logger.info("commit the event detail")
    db.commit()
    logger.success("event detail add successfully")
    return new_event



@event.get("/all_event",response_model=list[EventDetails])
def show_event():
    logger.info("get the data")
    db_event = db.query(EventDetail).filter(EventDetail.is_active == True,EventDetail.is_deleted == False).all()
    if db_event is None:
        logger.error("event detail not found")
        raise HTTPException(status_code=404, detail="user not found")
    logger.success("data get successfully")
    return db_event



@event.get("/get_event",response_model=EventDetails)
def read_event(token : str):
    logger.info("decode the token")
    event_id = decode_token_em_id(token)
    db_event = db.query(EventDetail).filter(EventDetail.id == event_id,EventDetail.is_active == True,EventDetail.is_deleted == False).first()
    
    if db_event is None:
        logger.error("event detail is not found")
        raise HTTPException(status_code=404, detail="user not found")
    logger.success("data get successfully")
    return db_event



@event.put("/update_event")
def change_event_detail(user:EventDetails,token : str):
    logger.info("decode the token")
    event_id = decode_token_em_id(token)
    db_event = db.query(EventDetail).filter(EventDetail.id == event_id,EventDetail.is_active == True,EventDetail.is_deleted == False).first()
    
    if db_event is None:
        logger.error("event detail is not found")
        raise HTTPException(status_code=404, detail="user not found")
    
    logger.info("change the detail")
    db_event.E_name = user.E_name,
    db_event.E_venue = user.E_venue,
    db_event.E_date = user.E_date,
    db_event.E_time = user.E_time,
    db_event.E_location = user.E_location,
    db_event.E_description = user.E_description,
    db_event.E_guest_size = user.E__guest_size,
    db_event.E_price = user.E_price
    
    logger.info("data commit")
    db.commit()
    logger.success("detail change the successfully")
    return "your detail changes successfully"



@event.patch("/update_event_detail")
def update_data(token : str,updateevent:EventDetailsUpdate):
    logger.info("decode the token")
    user_id = decode_token_em_id(token)
    
    db_event = db.query(EventDetail).filter(EventDetail.id == user_id,EventDetail.is_active == True,EventDetail.is_deleted == False).first()
    if db_event is None:
        logger.error("event detail is not found")
        raise HTTPException(status_code=404, detail="user not found")
    update_data = updateevent.dict(exclude_unset = True)
    for key,value in update_data.items():
        logger.info("change the specific detail")
        setattr(db_event, key, value)
    logger.info("after update the detail commit")
    db.commit()
    db.refresh(db_event)
    logger.success("detail change the successfully")
    return{"message":"details changes successfully","User": db_event}


@event.delete("/delete_event")
def delete_event(token:str):
    logger.info("decode event token")
    event_id = decode_token_em_id(token)
    db_event = db.query(EventDetail).filter(EventDetail.id == event_id,EventDetail.is_active == True).first()
    if db_event is None:
        logger.error("event detail is not found")
        raise HTTPException(status_code=404, detail="users is not found")
    logger.info("sweep the values")
    db_event.is_active = False
    db_event.is_deleted = True
    
    logger.info("after the change commit ")
    db.commit()
    logger.success("event detail successfully")
    return "your event detail deleted successfully"



#-----------------------------venuemanagement-----------------------------------

venue = APIRouter()
db = SessionLocal()

@venue.post("/add_place",response_model=VenueManagements)
def add_event(place:VenueManagements):
    
    logger.info("adding venuedetails")
    new_venues = VenueManagement(
    name  = place.name,
    address  = place.address,
    capacity  = place.capacity,
    contact_number  = place.contact_number,
    availability  = place.availability,
    cost = place.cost,
    facility  = place.facility,
    )
    logger.info("add detail in database")
    db.add(new_venues)
    logger.info("commit the detail")
    db.commit()
    logger.success("venue detail added successfully")
    return new_venues



@venue.get("/all_places",response_model=list[VenueManagements])
def all_detail():
    logger.info("getting the venuedetail")
    db_event = db.query(VenueManagement).filter(VenueManagement.is_active == True,VenueManagement.is_deleted == False).all()
    if db_event is None:
        logger.error("vunue detail is found")
        raise HTTPException(status_code=404, detail="any venues is  not found")
    logger.success("detail fetch successfully")
    return db_event



@venue.get("/get_places_by_id",response_model=VenueManagements)
def get_by_id(token: str):
    logger.info("decode the token")
    venue_id = decode_token_em_id(token)
    db_place = db.query(VenueManagement).filter(VenueManagement.id == venue_id,VenueManagement.is_active == True,VenueManagement.is_deleted == False).first()
    if db_place is None:
        logger.error("venue id is not found")
        raise HTTPException(status_code=404, detail="venue id is  not found")
    logger.success("venue detail found successfully")
    return db_place



@venue.put("/update_venues")
def update_decoratore(venues:VenueManagements,token:str):
    logger.info("decode the token")
    venue_id = decode_token_em_id(token)
    db_place = db.query(VenueManagement).filter(VenueManagement.id == venue_id,VenueManagement.is_active == True,VenueManagement.is_deleted == False,VenueManagement.availability == True).first()

    if db_place is None:
        logger.error("venue detail is not found")
        raise HTTPException(status_code=404, detail="venue is not found")
    
    logger.info("update the detail")
    db_place.event_id  = venues.event_id,
    db_place.name  = venues.name,
    db_place.address  = venues.address,
    db_place.capacity  = venues.capacity,
    db_place.contact_number  = venues.contact_number,
    db_place.cost = venues.cost,
    db_place.facility  = venues.facility,
    
    logger.info("after update commit detail")
    db.commit()
    logger.success("your venue detail change the successfully")
    return "your detail changes successfully"



@venue.delete("/delete_venues")
def delete_event(token:str):
    logger.info("decode the token")
    venue_id = decode_token_em_id(token)
    db_event = db.query(VenueManagement).filter(VenueManagement.id == venue_id,VenueManagement.is_active == True).first()
    if db_event is None:
        logger.error("venue is not found")
        raise HTTPException(status_code=404, detail="venues is not found")
    
    logger.info("sweep the bool value")
    db_event.is_active = False
    db_event.is_deleted = True
    
    db.commit()
    logger.success("your venue detail deleted")
    return "your venue detail deleted successfully"



#-----------------------------------event manager-------------------------------


manager = APIRouter()
db = SessionLocal()

@manager.post("/event_manager",response_model=EventManagers)
def add_event(use:EventManagers):
    logger.info("add event manager detail")
    new_manager = EventManager(
    name = use.name,
    contact_no = use.contact_no
    )
    logger.info("add manger detail in database")
    db.add(new_manager)
    logger.info("commit the detail")
    db.commit()
    logger.success("adding detail successfully")
    return new_manager



@manager.get("/all_manager",response_model=list[EventManagers])
def all_manager():
    logger.info("fetching data")
    db_event = db.query(EventManager).filter(EventManager.is_active == True,EventManager.is_deleted == False).all()
    if db_event is None:
        logger.error("manager is not found")
        raise HTTPException(status_code=404, detail="manager not found")
    logger.success("all manager detail get successfully")
    return db_event



@manager.get("/get_manager",response_model=EventManagers)
def get_manager(token : str):
    logger.info("decode the token")
    manager_id = decode_token_em_id(token)
    db_event = db.query(EventManager).filter(EventManager.id == manager_id,EventManager.is_active == True,EventManager.is_deleted == False).first()
    
    if db_event is None:
        logger.error("manger is not found")
        raise HTTPException(status_code=404, detail="manager not found")
    logger.success("manger detail get by the id")
    return db_event



@manager.put("/update_manager")
def update_manager(manager:ManagerUpdate,token:str):
    logger.info("decode the token")
    manager_id = decode_token_em_id(token)
    db_event = db.query(EventManager).filter(EventManager.id == manager_id,EventManager.is_active == True,EventManager.is_deleted == False).first()

    if db_event is None:
        logger.error("manager is not found")
        raise HTTPException(status_code=404, detail="manager not found")
    
    logger.info("update manger detail")
    db_event.name = manager.name,
    db_event.contact_no = manager.contact_no
    
    db.commit()
    logger.success("detail change the successfully")
    return "your detail changes successfully"



@manager.patch("/update_manger_detail")
def update_data(token : str,updatemanager:ManagerUpdate):
    logger.info("decode the token")
    manager_id = decode_token_em_id(token)
    db_event = db.query(EventManager).filter(EventManager.id == manager_id,EventManager.is_active == True,EventManager.is_deleted == False).first()
    if db_event is None:
        logger.error("manager is not found")
        raise HTTPException(status_code=404, detail="manager not found")
    update_data = updatemanager.dict(exclude_unset = True)
    for key,value in update_data.items():
        logger.info("update the specific detail")
        setattr(db_event, key, value)
    db.commit()
    db.refresh(db_event)
    logger.success("detail updated!!!")
    return{"message":"details changes successfully","User": db_event}



@manager.delete("/delete_manager")
def delete_event(token:str):
    logger.info("decode the token")
    manager_id = decode_token_em_id(token)
    db_event = db.query(EventManager).filter(EventManager.id == manager_id,EventManager.is_active == True).first()
    if db_event is None:
        logger.error("manager is not found")
        raise HTTPException(status_code=404, detail="manager is not found")
    
    logger.info("change the bool value")
    db_event.is_active = False
    db_event.is_deleted = True
    
    db.commit()
    logger.success("manager detail deleted successfully")
    return "your manager detail deleted successfully"



#-------------------------------EventStatus-------------------------------------

status = APIRouter()
db = SessionLocal()

@status.post("/add_status",response_model=EvenStatuss)
def add_status(status:EvenStatuss):
    logger.info("add event status detail")
    new_eventstatus = EvenStatus(
    event_id = status.event_id,
    name = status.name,
    status = status.status,
    )
    logger.info("addind detail")
    db.add(new_eventstatus)
    db.commit()
    logger.success("status adding successfully")
    return new_eventstatus



@status.get("/all_event_status",response_model=list[EvenStatuss])
def all_satus():
    logger.info("fetching event status detail")
    db_status = db.query(EvenStatus).filter(EvenStatus.is_active == True,EvenStatus.is_deleted == False).all()
    if db_status is None:
        logger.error("event status not found")
        raise HTTPException(status_code=404, detail="event status not found")
    logger.success("status get successfully")
    return db_status



@status.get("/get_status_id",response_model=EvenStatuss)
def get_manager(token : str):
    logger.info("decode the token")
    status_id = decode_token_em_id(token)
    logger.info("fetching event status detail")
    db_status = db.query(EvenStatus).filter(EvenStatus.id == status_id,EvenStatus.is_active == True,EvenStatus.is_deleted == False).first()
    
    if db_status is None:
        logger.error("event status not found")
        raise HTTPException(status_code=404, detail="event status not found")
    logger.success("status get successfully")
    return db_status



@status.put("/update_eventstatus")
def update_manager(status:EvenStatuss,token:str):
    logger.info("decode the token")
    status_id = decode_token_em_id(token)
    db_status = db.query(EvenStatus).filter(EvenStatus.id == status_id,EvenStatus.is_active == True,EvenStatus.is_deleted == False).first()

    if db_status is None:
        logger.error("event status not found")
        raise HTTPException(status_code=404, detail="event status not found")
    
    logger.info("update the status detail")
    db_status.event_id  = status.event_id,
    db_status.name  = status.name,
    db_status.status  = status.status,
    
    db.commit()
    logger.success("detail updated successfully")
    return "your detail changes successfully"



@status.patch("/update_eventstatus_detail")
def update_data(token : str,updatestatus:EventStatusUpdates):
    logger.info("decode the token")
    status_id = decode_token_em_id(token)
    db_status = db.query(EvenStatus).filter(EvenStatus.id == status_id,EvenStatus.is_active == True,EvenStatus.is_deleted == False).first()
    if db_status is None:
        logger.error("event status not found")
        raise HTTPException(status_code=404, detail="status is  not found")
    update_data = updatestatus.dict(exclude_unset = True)
    for key,value in update_data.items():
        logger.info("change the any specific detail")
        setattr(db_status, key, value)
    db.commit()
    db.refresh(db_status)
    logger.success("your detail change the successfully")
    return{"message":"details changes successfully","User": db_status}



@status.delete("/delete_status")
def delete_eventstatus(token:str):
    logger.info("decode the token")
    status_id = decode_token_em_id(token)
    db_status = db.query(EvenStatus).filter(EvenStatus.id == status_id,EvenStatus.is_active == True).first()
    if db_status is None:
        logger.error("event status not found")
        raise HTTPException(status_code=404, detail="manager is not found")
    logger.info("change the bool value")
    db_status.is_active = False
    db_status.is_deleted = True
    
    db.commit()
    logger.success("status deleted successfully")
    return "your event status detail deleted successfully"






#--------------------------------vendor_suppliers-------------------------------

vendors = APIRouter()
db = SessionLocal()



@vendors.post("/add_catering",response_model=Caterings)
def add_catering(caters:Caterings):
    
    db_user = db.query(Catering).filter(Catering.name == caters.name).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="caters name already available")
    
    db_user = db.query(Catering).filter(Catering.email == caters.email).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="email id already available")
    
    db_user = db.query(Catering).filter(Catering.contact_number == caters.contact_number).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="contact_number already available")
    
    
    logger.info("create new catering ")
    new_caters = Catering(
    name = caters.name,
    address = caters.address,
    email = caters.email,
    contact_number = caters.contact_number,
    availability = caters.availability,
    cost = caters.cost
    )
    logger.info("add the catering detail")
    db.add(new_caters)
    db.commit()
    logger.success("catering detail add successfully")
    return new_caters



@vendors.get("/all_caters",response_model=list[Caterings])
def all_detail():
    logger.info("fetch the caters detail")
    db_event = db.query(Catering).filter(Catering.is_active == True,Catering.is_deleted == False).all()
    if db_event is None:
        logger.error("caterning detail not found")
        raise HTTPException(status_code=404, detail="catering detail not found")
    logger.success("getting the detail successfully")
    return db_event



@vendors.get("/get_catering_by_id",response_model=Caterings)
def get_by_id(token: str):
    logger.info("decode the token")
    caters_id = decode_token_em_id(token)
    logger.info("fetch the caters detail")
    db_event = db.query(Catering).filter(Catering.id == caters_id,Catering.is_active == True,Catering.is_deleted == False).first()
    if db_event is None:
        logger.error("caterning detail not found")
        raise HTTPException(status_code=404, detail="catering detail not found")
    logger.success("detail get successfully")
    return db_event



@vendors.put("/update_catering")
def update_catering(caters:UpdateDetails,token:str):
    caters_id = decode_token_em_id(token)
    logger.info("decode the token")
    db_event = db.query(Catering).filter(Catering.id == caters_id,EventManager.is_active == True,EventManager.is_deleted == False).first()

    if db_event is None:
        logger.error("caterning detail not found")
        raise HTTPException(status_code=404, detail="manager not found")
    
    logger.info("update the catering detail")
    db_event.name = caters.name,
    db_event.address = caters.address,
    db_event.email = caters.email,
    db_event.contact_number = caters.contact_number,
    db_event.cost = caters.cost
    
    logger.info("commit the detail")
    db.commit()
    logger.success("catering detail change the successfully")
    return "your detail changes successfully"




@event.patch("/update_caters")
def update_catering(token : str,updateevent:VendorsUpdateDetails):
    logger.info("decode the token")
    caters_id = decode_token_em_id(token)
    db_event = db.query(Catering).filter(Catering.id == caters_id,Catering.is_active == True,Catering.is_deleted == False,Catering.availability == True).first()
    if db_event is None:
        logger.error("caterning detail not found")
        raise HTTPException(status_code=404, detail="caters not found")
    update_data = updateevent.dict(exclude_unset = True)
    for key,value in update_data.items():
        logger.info("change the specific detail")
        setattr(db_event, key, value)
        
    logger.info("commit the detail")
    db.commit()
    db.refresh(db_event)
    logger.success("detail add successfully")
    return{"message":"details changes successfully","User": db_event}



@vendors.delete("/delete_catering")
def delete_catering(token:str):
    logger.info("decode the token")
    caters_id = decode_token_em_id(token)
    db_event = db.query(Catering).filter(Catering.id == caters_id,Catering.is_active == True).first()
    if db_event is None:
        logger.error("caterning detail not found")
        raise HTTPException(status_code=404, detail="catering is not found")
    
    logger.info("change the bool value")
    db_event.is_active = False
    db_event.is_deleted = True
    
    db.commit()
    logger.success("catering detail deleted successfully")
    return "your catering detail deleted successfully"


#--------------------------------Decorations------------------------------------



@vendors.post("/add_decorater",response_model=Decorations)
def add_event(decos:Decorations):
    
    db_user = db.query(DecorationandFloralarrangment).filter(DecorationandFloralarrangment.name == decos.name).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="decor name already available")
    
    db_user = db.query(DecorationandFloralarrangment).filter(DecorationandFloralarrangment.email == decos.email).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="email id already available")
    
    db_user = db.query(DecorationandFloralarrangment).filter(DecorationandFloralarrangment.contact_number == decos.contact_number).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="contact_number already available")
    
    logger.info("create a new decoration detail")
    new_manager = DecorationandFloralarrangment(
    name = decos.name,
    address = decos.address,
    email = decos.email,
    contact_number = decos.contact_number,
    availability = decos.availability,
    cost = decos.cost
    )
    logger.info("add the decoration detail")
    db.add(new_manager)
    db.commit()
    logger.success("decoration detail add successfully")
    return new_manager



@vendors.get("/all_decorater",response_model=list[Decorations])
def all_detail():
    logger.info("fetching the detail")
    db_event = db.query(DecorationandFloralarrangment).filter(DecorationandFloralarrangment.is_active == True,DecorationandFloralarrangment.is_deleted == False).all()
    if db_event is None:
        logger.error("decorator detail not found")
        raise HTTPException(status_code=404, detail="decorator not found")
    logger.success("getting all the detail")
    return db_event



@vendors.get("/get_decoratore_by_id",response_model=Decorations)
def get_by_id(token: str):
    logger.info("decode the token")
    id = decode_token_em_id(token)
    db_event = db.query(DecorationandFloralarrangment).filter(DecorationandFloralarrangment.id == id,DecorationandFloralarrangment.is_active == True,DecorationandFloralarrangment.is_deleted == False,DecorationandFloralarrangment.availability == True).first()
    if db_event is None:
        logger.error("decorator detail not found")
        raise HTTPException(status_code=404, detail="manager not found")
    logger.success("getting all the detail")
    return db_event



@vendors.put("/update_decoratore")
def update_decoratore(deco:UpdateDetails,token:str):
    # breakpoint()
    logger.info("decode the token")
    decoratore_id = decode_token_em_id(token)
    db_event = db.query(DecorationandFloralarrangment).filter(DecorationandFloralarrangment.id == decoratore_id,DecorationandFloralarrangment.is_active == True,DecorationandFloralarrangment.is_deleted == False,DecorationandFloralarrangment.availability == True).first()

    if db_event is None:
        logger.error("decorator detail not found")
        raise HTTPException(status_code=404, detail="manager not found")
    
    logger.info("update decorator detail")
    db_event.name = deco.name,
    db_event.address = deco.address,
    db_event.email = deco.email,
    db_event.contact_number = deco.contact_number,
    db_event.cost = deco.cost
    
    db.commit()
    logger.success("detail update successfully")
    return "your detail changes successfully"



@event.patch("/update_decoratorefloral")
def update_decoratore(token : str,updateevent:VendorsUpdateDetails):
    logger.info("decode the token")
    decoratore_id = decode_token_em_id(token)
    db_deco = db.query(DecorationandFloralarrangment).filter(DecorationandFloralarrangment.id == decoratore_id,DecorationandFloralarrangment.is_active == True,DecorationandFloralarrangment.is_deleted == False,DecorationandFloralarrangment.availability == True).first()
    if db_deco is None:
        logger.error("decorator detail not found")
        raise HTTPException(status_code=404, detail="decorators not found")
    update_data = updateevent.dict(exclude_unset = True)
    for key,value in update_data.items():
        logger.info("change specific detail")
        setattr(db_deco, key, value)
    db.commit()
    db.refresh(db_deco)
    logger.success("detail change successfully")
    return{"message":"details changes successfully","User": db_deco}



@vendors.delete("/delete_decoratore")
def delete_event(token:str):
    logger.info("decode the token")
    decoratore_id = decode_token_em_id(token)
    db_event = db.query(DecorationandFloralarrangment).filter(DecorationandFloralarrangment.id == decoratore_id,DecorationandFloralarrangment.is_active == True).first()
    if db_event is None:
        logger.error("decorator detail not found")
        raise HTTPException(status_code=404, detail="decoratore is not found")
    
    logger.info("change bool value")
    db_event.is_active = False
    db_event.is_deleted = True
    
    db.commit()
    logger.success("decorator deleted successfully")
    return "your decoratore detail deleted successfully"



#---------------------------audio_visual----------------------------------------


@vendors.post("/add_audiovisual",response_model=Audio_visuals)
def add_event(audio:Audio_visuals):
    
    db_user = db.query(Audio_visualEquipment).filter(Audio_visualEquipment.name == audio.name).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="caters name already available")
    
    db_user = db.query(Audio_visualEquipment).filter(Audio_visualEquipment.email == audio.email).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="email id already available")
    
    db_user = db.query(Audio_visualEquipment).filter(Audio_visualEquipment.contact_number == audio.contact_number).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="contact_number already available")
    
    logger.info("create a new audiovisual")
    new_audiovisuals = Audio_visualEquipment(
    name = audio.name,
    address = audio.address,
    email = audio.email,
    contact_number = audio.contact_number,
    availability = audio.availability,
    cost = audio.cost
    )
    logger.info("adding detail in database")
    db.add(new_audiovisuals)
    db.commit()
    logger.success("detail adding successfully")
    return new_audiovisuals



@vendors.get("/all_audiovisual",response_model=list[Audio_visuals])
def all_detail():
    logger.info("fetching detail")
    db_event = db.query(Audio_visualEquipment).filter(Audio_visualEquipment.is_active == True,Audio_visualEquipment.is_deleted == False).all()
    if db_event is None:
        logger.error("audiocisual detail not found")
        raise HTTPException(status_code=404, detail="audio or visualgrapher not found")
    logger.success("getting detail successfully")
    return db_event



@vendors.get("/get_audiovisuals_by_id",response_model=Audio_visuals)
def get_by_id(token: str):
    logger.info("decode the token")
    audio_id = decode_token_em_id(token)
    db_event = db.query(Audio_visualEquipment).filter(Audio_visualEquipment.id == audio_id,Audio_visualEquipment.is_active == True,Audio_visualEquipment.is_deleted == False).first()
    if db_event is None:
        logger.error("audio or videographer detail not found")
        raise HTTPException(status_code=404, detail="audio or visualgrapher not found")
    logger.success("getting detail successfully")
    return db_event



@vendors.put("/update_audiovisual")
def update_decoratore(audio:UpdateDetails,token:str):
    logger.info("decode the token")
    audio_id = decode_token_em_id(token)
    db_event = db.query(Audio_visualEquipment).filter(Audio_visualEquipment.id == audio_id,Audio_visualEquipment.is_active == True,Audio_visualEquipment.is_deleted == False,Audio_visualEquipment.availability == True).first()

    if db_event is None:
        logger.error("audio or visual detail not found")
        raise HTTPException(status_code=404, detail="audio or visualgrapher not found")
    
    logger.info("update the audiovisual detail")
    db_event.name = audio.name,
    db_event.address = audio.address,
    db_event.email = audio.email,
    db_event.contact_number = audio.contact_number,
    db_event.cost = audio.cost
    
    db.commit()
    logger.success("detail updated successfully")
    return "your detail changes successfully"



@event.patch("/update_audiovisuals")
def update_audiovisuals(token : str,updateevent:VendorsUpdateDetails):
    logger.info("decode the token")
    audio_id = decode_token_em_id(token)
    db_audio = db.query(Audio_visualEquipment).filter(Audio_visualEquipment.id == audio_id,Audio_visualEquipment.is_active == True,Audio_visualEquipment.is_deleted == False,Audio_visualEquipment.availability == True).first()
    if db_audio is None:
        logger.error("audiovisual detail not found")
        raise HTTPException(status_code=404, detail="audiovisuals is not found")
    update_data = updateevent.dict(exclude_unset = True)
    for key,value in update_data.items():
        logger.info("change the specific detail")
        setattr(db_audio, key, value)
    db.commit()
    db.refresh(db_audio)
    logger.success("detail change the successfully")
    return{"message":"details changes successfully","User": db_audio}



@vendors.delete("/delete_audiovisual")
def delete_event(token:str):
    logger.info("decode the token")
    audio_id = decode_token_em_id(token)
    db_event = db.query(Audio_visualEquipment).filter(Audio_visualEquipment.id == audio_id,Audio_visualEquipment.is_active == True).first()
    if db_event is None:
        logger.error("audiovisual detail not found")
        raise HTTPException(status_code=404, detail="audiovisual is not found")
    
    logger.info("change bool value")
    db_event.is_active = False
    db_event.is_deleted = True
    
    db.commit()
    logger.success("videovisual deleted successfully")
    return "your video or visual detail deleted successfully"



#------------------------entertainments-----------------------------------------

@vendors.post("/add_entertaiment",response_model=Entertainments)
def add_event(event:Entertainments):
    
    db_user = db.query(Entertainment).filter(Entertainment.name == event.name).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="caters name already available")
    
    db_user = db.query(Entertainment).filter(Entertainment.email == event.email).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="email id already available")
    
    db_user = db.query(Entertainment).filter(Entertainment.contact_number == event.contact_number).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="contact_number already available")
    
    logger.info("add new entertainment")
    new_entertainment = Entertainment(
    name = event.name,
    address = event.address,
    email = event.email,
    contact_number = event.contact_number,
    availability = event.availability,
    cost = event.cost
    )
    logger.info("adding detail in database")
    db.add(new_entertainment)
    db.commit()
    logger.success("detail adding successfully")
    return new_entertainment



@vendors.get("/all_entertainment",response_model=list[Entertainments])
def all_detail():
    logger.info("fethching detail")
    db_event = db.query(Entertainment).filter(Entertainment.is_active == True,Entertainment.is_deleted == False).all()
    if db_event is None:
        logger.error("entertainment id detail not found")
        raise HTTPException(status_code=404, detail="your id is not found")
    logger.success("all detail get it")
    return db_event



@vendors.get("/get_entertainment_by_id",response_model=Entertainments)
def get_by_id(token: str):
    logger.info("decode the token")
    enter_id = decode_token_em_id(token)
    db_event = db.query(Entertainment).filter(Entertainment.id == enter_id,Entertainment.is_active == True,Entertainment.is_deleted == False,Entertainment.availability == True).first()
    if db_event is None:
        logger.error("entertainment id detail not found")
        raise HTTPException(status_code=404, detail="your id or detail not found")
    logger.success("detail getting it")
    return db_event



@vendors.put("/update_entertainment")
def update_decoratore(entertainment:UpdateDetails,token:str):
    logger.info("decode the token")
    entertainment_id = decode_token_em_id(token)
    db_event = db.query(Entertainment).filter(Entertainment.id == entertainment_id,Entertainment.is_active == True,Entertainment.is_deleted == False,Entertainment.availability == True).first()

    if db_event is None:
        logger.error("entertainment id detail not found")
        raise HTTPException(status_code=404, detail="your id is not found")
    
    logger.info("update entertainment detail")
    db_event.name = entertainment.name,
    db_event.address = entertainment.address,
    db_event.email = entertainment.email,
    db_event.contact_number = entertainment.contact_number,
    db_event.cost = entertainment.cost
    
    db.commit()
    logger.success("detail change successfully")
    return "your detail changes successfully"



@event.patch("/update_entertaimnet_detail")
def update_catering(token : str,updateevent:VendorsUpdateDetails):
    logger.info("decode the token")
    entertainment_id = decode_token_em_id(token)
    db_entertainment = db.query(Entertainments).filter(Entertainments.id == entertainment_id,Entertainments.is_active == True,Entertainments.is_deleted == False,Entertainments.availability == True).first()
    if db_entertainment is None:
        logger.error("entertainment id detail not found")
        raise HTTPException(status_code=404, detail="entetainment detail not found")
    update_data = updateevent.dict(exclude_unset = True)
    for key,value in update_data.items():
        logger.info("change specific detail")
        setattr(db_entertainment, key, value)
    db.commit()
    db.refresh(db_entertainment)
    logger.success("change detail successfully")
    return{"message":"details changes successfully","User": db_entertainment}



@vendors.delete("/delete_entertainment")
def delete_event(token:str):
    logger.info("decode the token")
    enter_id = decode_token_em_id(token)
    db_event = db.query(Entertainment).filter(Entertainment.id == enter_id,Entertainment.is_active == True).first()
    if db_event is None:
        logger.error("entertainment id detail not found")
        raise HTTPException(status_code=404, detail="your id is not found")
    
    logger.info("change bool values")
    db_event.is_active = False
    db_event.is_deleted = True
    
    db.commit()
    logger.success("entertainment deleted successfully")
    return "your entertainment detail deleted successfully"



#---------------------------------photovideography------------------------------


@vendors.post("/add_photographer",response_model=PhotoVideoGraphys)
def add_event(videography:PhotoVideoGraphys):
    
    db_user = db.query(Photo_video_graphy).filter(Photo_video_graphy.name == videography.name).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="caters name already available")
    
    db_user = db.query(Photo_video_graphy).filter(Photo_video_graphy.email == videography.email).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="email id already available")
    
    db_user = db.query(Photo_video_graphy).filter(Photo_video_graphy.contact_number == videography.contact_number).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="contact_number already available")
    
    logger.info("add new photographer detail")
    new_photovideography = Photo_video_graphy(
    name = videography.name,
    address = videography.address,
    email = videography.email,
    contact_number = videography.contact_number,
    availability = videography.availability,
    cost = videography.cost
    )
    logger.info("detail add successfully")
    db.add(new_photovideography)
    db.commit()
    logger.success("detail add successfully")
    return new_photovideography



@vendors.get("/all_photovideo",response_model=list[PhotoVideoGraphys])
def all_detail():
    logger.info("fetching all detil")
    db_event = db.query(Photo_video_graphy).filter(Photo_video_graphy.is_active == True,Photo_video_graphy.is_deleted == False).all()
    if db_event is None:
        logger.error("photovideo id detail not found")
        raise HTTPException(status_code=404, detail="your id is not found")
    logger.success("photovideo data got successfully")
    return db_event



@vendors.get("/get_photovideo_by_id",response_model=PhotoVideoGraphys)
def get_by_id(token: str):
    logger.info("decode the token")
    photo_id = decode_token_em_id(token)
    db_event = db.query(Photo_video_graphy).filter(Photo_video_graphy.id == photo_id,Photo_video_graphy.is_active == True,Photo_video_graphy.is_deleted == False,Photo_video_graphy.availability == True).first()
    if db_event is None:
        logger.error("photovideo id detail not found")
        raise HTTPException(status_code=404, detail="yours id is not found")
    logger.success("detail get successfully")
    return db_event



@vendors.put("/update_photovideo")
def update_decoratore(photovideo:UpdateDetails,token:str):
    logger.info("decode the token")
    photo_id = decode_token_em_id(token)
    db_event = db.query(Photo_video_graphy).filter(Photo_video_graphy.id == photo_id,Photo_video_graphy.is_active == True,Photo_video_graphy.is_deleted == False,Photo_video_graphy.availability == True).first()

    if db_event is None:
        logger.error("photovideo detail not found")
        raise HTTPException(status_code=404, detail="your id is not found")
    
    logger.info("update photovideos details")
    db_event.name = photovideo.name,
    db_event.address = photovideo.address,
    db_event.email = photovideo.email,
    db_event.contact_number = photovideo.contact_number,
    db_event.cost = photovideo.cost
    
    db.commit()
    logger.success("update the detail successfully")
    return "your detail changes successfully"



@event.patch("/update_photovideography")
def update_catering(token : str,updateevent:VendorsUpdateDetails):
    logger.info("decode the token")
    photos_id = decode_token_em_id(token)
    db_pvgraphy = db.query(Photo_video_graphy).filter(Photo_video_graphy.id == photos_id,Photo_video_graphy.is_active == True,Photo_video_graphy.is_deleted == False,Photo_video_graphy.availability == True).first()
    if db_pvgraphy is None:
        logger.error("photographer detail not found")
        raise HTTPException(status_code=404, detail="photographer is  not found")
    update_data = updateevent.dict(exclude_unset = True)
    for key,value in update_data.items():
        logger.info("change specific detail")
        setattr(db_pvgraphy, key, value)
    db.commit()
    db.refresh(db_pvgraphy)
    logger.success("detail update successfully")
    return{"message":"details changes successfully","User": db_pvgraphy}



@vendors.delete("/delete_photovideo")
def delete_event(token:str):
    logger.info("decode the token")
    photo_id = decode_token_em_id(token)
    db_event = db.query(Photo_video_graphy).filter(Photo_video_graphy.id == photo_id,Photo_video_graphy.is_active == True).first()
    if db_event is None:
        logger.error("photovideographer detail not found")
        raise HTTPException(status_code=404, detail="photovideographer is not found")
    
    logger.info("chabge bool value")
    db_event.is_active = False
    db_event.is_deleted = True
    
    db.commit()
    logger.success("photovideographer deleted successfully")
    return "your photovideographer detail deleted successfully"


#---------------------------------Transportations-------------------------------

@vendors.post("/add_transportation",response_model=Transportations)
def add_event(travel:Transportations):
    
    db_user = db.query(Transportation).filter(Transportation.name == travel.name).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="caters name already available")
    
    db_user = db.query(Transportation).filter(Transportation.email == travel.email).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="email id already available")
    
    db_user = db.query(Transportation).filter(Transportation.contact_number == travel.contact_number).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="contact_number already available")
    
    logger.info("add new data")
    new_transport = Transportation(
    name = travel.name,
    address = travel.address,
    email = travel.email,
    contact_number = travel.contact_number,
    availability = travel.availability,
    cost = travel.cost
    )
    logger.info("add detail")
    db.add(new_transport)
    db.commit()
    logger.success("transport detail add successfully")
    return new_transport



@vendors.get("/all_transportation",response_model=list[Transportations])
def all_detail():
    logger.info("fetch transportation detal")
    db_event = db.query(Transportation).filter(Transportation.is_active == True,Transportation.is_deleted == False).all()
    if db_event is None:
        logger.error("transportation detail not found")
        raise HTTPException(status_code=404, detail="transportation detail not found")
    logger.success("all transportations get")
    return db_event



@vendors.get("/get_transportation_by_id",response_model=Transportations)
def get_by_id(token: str):
    logger.info("decode id token")
    transport_id = decode_token_em_id(token)
    db_event = db.query(Transportation).filter(Transportation.id == transport_id,Transportation.is_active == True,Transportation.is_deleted == False).first()
    if db_event is None:
        logger.error("transportation id not found")
        raise HTTPException(status_code=404, detail="transportation details not found")
    logger.success("tansportation detail get")
    return db_event



@vendors.put("/update_transportation")
def update_decoratore(tranport:UpdateDetails,token:str):
    logger.info("decode id token")
    transport_id = decode_token_em_id(token)
    db_event = db.query(Transportation).filter(Transportation.id == transport_id,Transportation.is_active == True,Transportation.is_deleted == False,Transportation.availability == True).first()

    if db_event is None:
        logger.error("transportation id not found")
        raise HTTPException(status_code=404, detail="transportation not found")
    
    logger.info("update details")
    db_event.name = tranport.name,
    db_event.address = tranport.address,
    db_event.email = tranport.email,
    db_event.contact_number = tranport.contact_number,
    db_event.cost = tranport.cost
    
    db.commit()
    logger.success("detail change successfully")
    return "your detail changes successfully"



@event.patch("/update_transportations")
def update_catering(token : str,updateevent:VendorsUpdateDetails):
    logger.info("decode id token")
    transport_id = decode_token_em_id(token)
    db_transpot = db.query(Transportations).filter(Transportations.id == transport_id,Transportations.is_active == True,Transportations.is_deleted == False,Transportations.availability == True).first()
    if db_transpot is None:
        logger.error("transportation id not found")
        raise HTTPException(status_code=404, detail="transport not found")
    update_data = updateevent.dict(exclude_unset = True)
    for key,value in update_data.items():
        logger.info("update specific detail")
        setattr(db_transpot, key, value)
    db.commit()
    db.refresh(db_transpot)
    logger.success("update detail successfully")
    return{"message":"details changes successfully","User": db_transpot}



@vendors.delete("/delete_transportation")
def delete_event(token:str):
    logger.info("decode id token")
    transport_id = decode_token_em_id(token)
    db_event = db.query(Transportation).filter(Transportation.id == transport_id,Transportation.is_active == True).first()
    if db_event is None:
        logger.error("transportation id not found")
        raise HTTPException(status_code=404, detail="transportation is not found")
    
    logger.info("change bool value")
    db_event.is_active = False
    db_event.is_deleted = True
    
    db.commit()
    logger.info("transportation detail successfully")
    return "transportation detail deleted successfully"


#------------------------------------logistic_operation-------------------------


@vendors.post("/add_logistics",response_model=Logistic_operations)
def add_event(logistics:Logistic_operations):
    logger.info("adding new logistics detail")
    new_logistics = Logistic_operation(
    setup_breakdown = logistics.setup_breakdown,
    staffing_volunteers = logistics.staffing_volunteers,
    security_safety = logistics.security_safety,
    transportation_parking = logistics.transportation_parking,
    signage_directions = logistics.signage_directions,
    )
    logger.info("add deetail in database")
    db.add(new_logistics)
    db.commit()
    logger.success("new transportation detail added")
    return new_logistics



@vendors.get("/all_logistics",response_model=list[Logistic_operations])
def all_detail():
    logger.info("fetching detail")
    db_event = db.query(Logistic_operation).filter(Logistic_operation.is_active == True,Logistic_operation.is_deleted == False).all()
    if db_event is None:
        logger.error("logistics id not found")
        raise HTTPException(status_code=404, detail="logistics id not found")
    logger.success("all detail get")
    return db_event



@vendors.get("/get_logistics_by_id",response_model=Logistic_operations)
def get_by_id(token: str):
    logger.info("decode id token")
    logist_id = decode_token_em_id(token)
    db_event = db.query(Logistic_operation).filter(Logistic_operation.id == logist_id,Logistic_operation.is_active == True,Logistic_operation.is_deleted == False).first()
    if db_event is None:
        logger.error("transportation id not found")
        raise HTTPException(status_code=404, detail="logistics is not found")
    logger.success("transportation detail successfully get")
    return db_event



@vendors.put("/update_logistics")
def update_decoratore(logistic:Logistic_operations,token:str):
    logger.info("decode id token")
    logist_id = decode_token_em_id(token)
    db_event = db.query(Logistic_operation).filter(Logistic_operation.id == logist_id,Logistic_operation.is_active == True,Logistic_operation.is_deleted == False).first()

    if db_event is None:
        logger.error("transportation id not found")
        raise HTTPException(status_code=404, detail="logistics not found")
    
    logger.info("update logistics detail")
    db_event.setup_breakdown = logistic.setup_breakdown,
    db_event.staffing_volunteers = logistic.staffing_volunteers,
    db_event.security_safety = logistic.security_safety,
    db_event.transportation_parking = logistic.transportation_parking,
    db_event.signage_directions = logistic.signage_directions,
    
    
    db.commit()
    logger.success("detail change successfully")
    return "your detail changes successfully"



@event.patch("/update_logistics_detail")
def update_catering(token : str,updateevent:Logistic_operationsUpdates):
    logger.info("decode id token")
    logist_id = decode_token_em_id(token)
    db_logist = db.query(Logistic_operation).filter(Logistic_operation.id == logist_id,Logistic_operation.is_active == True,Logistic_operation.is_deleted == False,Logistic_operation.availability == True).first()
    if db_logist is None:
        logger.error("logistic id not found")
        raise HTTPException(status_code=404, detail="logistic id is not found")
    update_data = updateevent.dict(exclude_unset = True)
    for key,value in update_data.items():
        logger.info("change specific detail")
        setattr(db_logist, key, value)
    db.commit()
    db.refresh(db_logist)
    logger.success("detail change successfully")
    return{"message":"details changes successfully","User": db_logist}



@vendors.delete("/delete_logistics")
def delete_event(token:str):
    logger.info("decode id token")
    logist_id = decode_token_em_id(token)
    db_event = db.query(Logistic_operation).filter(Logistic_operation.id == logist_id,Logistic_operation.is_active == True).first()
    if db_event is None:
        logger.error("logistics id not found")
        raise HTTPException(status_code=404, detail="logistics is not found")
    logger.info("change bool value")
    db_event.is_active = False
    db_event.is_deleted = True
    
    db.commit()
    logger.success("logistic deleted successfully")
    return "your logistics detail deleted successfully"



#----------------------------------------payment_system-------------------------

from validate_email_address import validate_email

payment = APIRouter()
db = SessionLocal()


@payment.post("/make_payment")
def make_payment(payment_request: Payments):
    logger.info("make payment system")
    # breakpoint()
    
    logger.info("check verified and id detail")
    user = db.query(UserDetail).filter(UserDetail.id == payment_request.user_id,UserDetail.is_verified == True,UserDetail.is_active == True).first()
    if user is None:
        logger.error("user not found")
        raise HTTPException(status_code=404, detail="User is not available or not verified or deleted")
    
    logger.info("check event id")
    event = db.query(EventDetail).filter(EventDetail.id == payment_request.event_id,EventDetail.E_price == payment_request.amount).first()
    if not event:
        logger.error("event is not found")
        raise HTTPException(status_code=404, detail="Event or price is not match")
    
    logger.info("check valid email")
    if not validate_email(user.email):
        logger.error("email id invalid or not given")
        raise HTTPException(status_code=400, detail="Invalid email address")
    
    logger.info("enter the detail")
    payment = Payment(
        user_id=payment_request.user_id,
        event_id=payment_request.event_id,
        amount=payment_request.amount,
        payment_status="Completed"
    )
    
    logger.info("add in databse system")
    db.add(payment)
    db.commit()


    logger.info("sent message through mail")
    success, message = send_email(
        sender_email="jenistalaviya404@gmail.com",
        receiver_email=user.email,
        password="zghoimvlnpzerzkv",
        transaction_id=payment.transaction_id
    )

    if not success:
        logger.error("message is not sent")
        raise HTTPException(status_code=500, detail=message)

    logger.success("payment done successfully and transaction id sent")
    return {"message": "Payment successful, transaction ID sent to email", "transaction_id": payment.transaction_id}



@event.get("/get_token_event")
def encode_token(id: str,email: str):
    access_token = get_event_token(id)
    return access_token
