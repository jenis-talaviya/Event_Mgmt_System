from pydantic import BaseModel
from typing import Optional
from datetime import date,time,datetime

class UserData(BaseModel):
    fname    : str
    lname    : str
    uname    : str
    email    : str
    mobile_no : str
    gender   : str
    password : str
    

class UserPatch(BaseModel):
    fname    : Optional[str]=None
    lname    : Optional[str]=None
    uname    : Optional[str]=None
    email    : Optional[str]=None
    mobile_no : Optional[str]=None
    gender   : Optional[str]=None



class OtpRequest(BaseModel):
    email :str
    
    
class Otpverify(BaseModel):
    email : str
    otp   : str
    
    
#------------------------event management system--------------------------------

class EventDetails(BaseModel):
    E_manager_id : str
    E_venue_id : str
    E_catering_id : str
    E_decoandfloral_id : str
    E_audiovisual_id : str
    E_entertainment_id : str
    E_photoandvideography_id : str
    E_transportation_id : str
    E_name : str
    E_venue : str
    E_date : date
    E_time : time
    E_location : str
    E_description : Optional[str] = None
    E__guest_size : Optional[int] = None
    E_price : Optional[int] = None
    
    
    
class EventDetailsUpdate(BaseModel):
    event_id : Optional[str] = None
    E_name : Optional[str] = None
    E_venue : Optional[str] = None
    E_date : Optional[str] = None
    E_time : Optional[str] = None
    E_location : Optional[str] = None
    E_description : Optional[str] = None
    E__guest_size : Optional[int] = None
    E_price : Optional[str] = None
    

class EventManagers(BaseModel):
    name : str
    contact_no : str


class ManagerUpdate(BaseModel):
    name : Optional[str] = None
    contact_no : Optional[str] = None
    
    

class VenueManagements(BaseModel):
    name : str
    address : str
    capacity : str
    contact_number : str
    availability : bool
    cost :str
    facility : str
    
class EvenStatuss(BaseModel):
    event_id : str
    name : str
    status : str
    
    
class EventStatusUpdates(BaseModel):
    event_id : Optional[str] = None
    name : Optional[str] = None
    status : Optional[str] = None
    
    
#-------------------------------------------
class Caterings(BaseModel):
    name : str
    address : str
    email : str
    contact_number : str
    availability : bool
    cost : str
    
        
class CateringsUpdates(BaseModel):
    name : Optional[str] = None
    address : Optional[str] = None
    email : Optional[str] = None
    contact_number : Optional[int] = None
    availability : Optional[bool] = None
    cost : Optional[str] = None
    
    
    
class Decorations(BaseModel):
    name : str
    address : str
    email : str
    contact_number : str
    availability : bool
    cost : str
    

    
class Audio_visuals(BaseModel):
    name : str
    address : str
    email : str
    contact_number : str
    availability : bool
    cost : str
    

    
class Entertainments(BaseModel):
    name : str
    address : str
    email : str
    contact_number : str
    availability : bool
    cost : str
    

    
class PhotoVideoGraphys(BaseModel):
    name : str
    address : str
    email : str
    contact_number : str
    availability : bool
    cost : str
    

    
class Transportations(BaseModel):
    name : str
    address : str
    email : str
    contact_number : str
    availability : bool
    cost : str
    

class UpdateDetails(BaseModel):
    name : str
    address : str
    email : str
    contact_number : str
    cost : str
    
    
    
class VendorsUpdateDetails(BaseModel):
    name : Optional[str] = None
    address : Optional[str] = None
    email : Optional[str] = None
    contact_number : Optional[str] = None
    cost : Optional[str] = None
    
    
    
class Logistic_operations(BaseModel):
    setup_breakdown : str
    staffing_volunteers : str
    security_safety : str
    transportation_parking : str
    signage_directions : str
    

class Logistic_operationsUpdates(BaseModel):
    setup_breakdown : Optional[str] = None
    staffing_volunteers : Optional[str] = None
    security_safety : Optional[str] = None
    transportation_parking : Optional[str] = None
    signage_directions : Optional[str] = None

    
class Payments(BaseModel):
    user_id : str
    event_id : str
    amount : str
    
    
class PaymentResponse(BaseModel):
    id: str
    user_id: str
    event_id: str
    amount: int
    payment_status: str
    transaction_id: str
    created_at: datetime
    updated_at: datetime
