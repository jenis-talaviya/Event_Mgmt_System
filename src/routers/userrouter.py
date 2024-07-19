from fastapi import FastAPI,HTTPException,APIRouter,Depends,Header
from database.database import SessionLocal
from src.models.userdetail import UserDetail,OTPDetail
from src.schemas.userschemas import UserData,OtpRequest,Otpverify,UserPatch
import uuid
from datetime import datetime,timedelta
from passlib.context import CryptContext
from src.utils.usertoken import decode_token_password,decode_token_user_email,decode_token_user_id,get_token
from src.utils.otp import generate_otp,send_otp_via_email
from src.utils.usertoken import get_event_token,decode_token_em_email,decode_token_em_id
from config import sender_email,email_password

user_log = APIRouter()
db = SessionLocal()

pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")

@user_log.post("/user_register",response_model=UserData)
def create_user(use:UserData):
    # breakpoint()
    db_user = db.query(UserDetail).filter(UserDetail.uname == use.uname).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="same user name already available")
    
    db_user = db.query(UserDetail).filter(UserDetail.email == use.email).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="same user email already available")
    
    db_user = db.query(UserDetail).filter(UserDetail.mobile_no == use.mobile_no).first()
    if db_user is not None:
        raise HTTPException(status_code=404, detail="same mobileno. already available")
    
    new_user = UserDetail(
        fname = use.fname,
        lname = use.lname,
        uname = use.uname,
        email = use.email,
        mobile_no = use.mobile_no,
        gender = use.gender,
        password = pwd_context.hash(use.password)
    )
    db.add(new_user)
    db.commit()
    return new_user


@user_log.get("/all_users",response_model=list[UserData])
def read_users():
    db_user = db.query(UserDetail).filter(UserDetail.is_active == True,UserDetail.is_deleted == False,UserDetail.is_verified == True).all()
    if db_user is None:
        raise HTTPException(status_code=404, detail="users not found")
    return db_user



@user_log.get("/get_user",response_model=UserData)
def read_single_users(token=Header(...)):
    user_id = decode_token_user_id(token)
    db_user = db.query(UserDetail).filter(UserDetail.id == user_id,UserDetail.is_active == True,UserDetail.is_deleted == False,UserDetail.is_verified == True).first()
    
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return db_user



@user_log.put("/update_user")
def update_user_detail(users: UserData,token=Header(...)):
    user_id = decode_token_user_id(token)
    
    db_user = db.query(UserDetail).filter(UserDetail.uname == users.uname).first()
    if db_user is not None and UserDetail.uname == users.uname:
        raise HTTPException(status_code=404, detail="same user name already available")
    
    db_user = db.query(UserDetail).filter(UserDetail.email == users.email).first()
    if db_user is not None and UserDetail.email == users.email:
        raise HTTPException(status_code=404, detail="same user email already available")
    
    db_user = db.query(UserDetail).filter(UserDetail.mobile_no == users.mobile_no).first()
    if db_user is not None and UserDetail.mobile_no == users.mobile_no:
        raise HTTPException(status_code=404, detail="same user mobileno. already available")
    
    db_user = db.query(UserDetail).filter(UserDetail.id == user_id,UserDetail.is_active == True,UserDetail.is_deleted == False,UserDetail.is_verified == True).first()
    # breakpoint()
    if db_user is None:
        raise HTTPException(status_code=404, detail="users detail not found")
    
    db_user.fname    = users.fname,
    db_user.uname    = users.uname,
    db_user.lname    = users.lname,
    db_user.email    = users.email,
    db_user.mobile_no= users.mobile_no,
    db_user.gender   = users.gender
    
    db.commit()
    return "your detail change succesfully"



@user_log.patch("/update_data")
def update_data(Userdetail: UserPatch,token=Header(...)):
    user_id = decode_token_user_id(token)
    db_user = db.query(UserDetail).filter(UserDetail.id == user_id,UserDetail.is_active == True,UserDetail.is_verified == True).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    update_data = Userdetail.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return {"message": "Details changed successfully", "User": db_user}



@user_log.delete("/delete_user")
def delete_user(token=Header(...)):
    user_id = decode_token_user_id(token)
    db_user = db.query(UserDetail).filter(UserDetail.id == user_id,UserDetail.is_active == True).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="users is not found")
    db_user.is_active  = False
    db_user.is_deleted = True
    db_user.is_verified = False
    
    db.commit()
    return "you deleted successfully"




#-------------------------OTP verification----------------------------------

otp_gen = APIRouter()
db = SessionLocal()


@otp_gen.post("/generate_otp")
def generate_otp_for_user(email: str):
    db_user = db.query(UserDetail).filter(UserDetail.email == email, UserDetail.is_active == True).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="email is not registered")
    
    otp_code = generate_otp()
    expiry_time = datetime.now() + timedelta(minutes=10)  # OTP valid for 10 minutes
    new_otp = OTPDetail(
        email=email,
        otp=otp_code,
        expiry_time=expiry_time
    )
    db.add(new_otp)
    db.commit()

    # Send OTP via email
    
    receiver_email = email
    
    success, message = send_otp_via_email(sender_email, receiver_email, email_password, otp_code)

    if not success:
        raise HTTPException(status_code=500, detail="otp can't sent")

    return {"message": "OTP sent to email", "email": email}



@otp_gen.post("/verify_otp")
def verify_otp(email: str, otp: str):
    db_record = db.query(OTPDetail).filter(OTPDetail.email == email, OTPDetail.otp == otp).first()
    if not db_record:
        raise HTTPException(status_code=400, detail="Invalid Entered OTP")
    
    # Check if the OTP has expired
    if datetime.now() > db_record.expiry_time:
        raise HTTPException(status_code=400, detail="OTP Time expired")
    
    user_record = db.query(UserDetail).filter(UserDetail.email == email).first()
    if not user_record:
        raise HTTPException(status_code=400, detail="Email is not found")
    
    # Update the is_verified field in the USERDetail table
    user_record.is_verified = True
    
    db.delete(db_record)
    db.commit()
    return {"message": "OTP verified successfully"}


# @otp_gen.get("/is_verified/{email}")
# def check_otp_verification(email: str):
#     otp_record = db.query(OTPDetail).filter(OTPDetail.email == email, OTPDetail.is_verified == True).first()
#     if otp_record:
#         return {"is_verified": True}
#     else:
#         return {"is_verified": False}



# @user_log.get("/logging_users")
# def logging_user(token:str):
#     user_id = decode_token_user_id(token)
#     db_user = db.query(UserDetail).filter(UserDetail.id == user_id,UserDetail.is_active == True,UserDetail.is_deleted == False,OTPDetail.is_verified == True).first()
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="user id is not found")
    
    
#     return("logging successfully")



@user_log.get("/logging_users")
def logging_user(email:str, password:str):
    db_user = db.query(UserDetail).filter(UserDetail.email == email,UserDetail.is_active == True,UserDetail.is_deleted == False,UserDetail.is_verified == True).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="user is not found")
    
    if not pwd_context.verify(password,db_user.password):
        raise HTTPException(status_code=404, detail="password is incorrect")
        
    access_token = get_token(db_user.id,email,password)
    return access_token




@user_log.put("/reset_password")
def reset_password(newpass: str,token=Header(...)):
    user_id = decode_token_user_id(token)
    email   = decode_token_user_email(token)
    password= decode_token_password(token)
    db_user = db.query(UserDetail).filter(UserDetail.id == user_id,UserDetail.email == email,UserDetail.is_active == True).first()
    if db_user is None:
        raise HTTPException("user data is not found")
    
    if pwd_context.verify(password,db_user.password):
        db_user.password = pwd_context.hash(newpass)
        db.commit()
        return "password reset successfully"
    else:
        return "old password is not match"
    
    
    
@user_log.put("/reregister_user")
def update_user_pass(email: str, password: str,token=Header(...)):
    # breakpoint()
    user_id = decode_token_user_id(token)
    db_user = db.query(UserDetail).filter(UserDetail.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    
    if db_user.is_active == False and db_user.is_deleted == True:
        if pwd_context.verify(password,db_user.password):
            db_user.is_active = True
            db_user.is_deleted = False
            db.commit()
            return "you successfully Reregister"
    else:
        raise HTTPException(status_code=404, detail="email or password is not match")
    
    

@user_log.put("/forget_password")
def forget_password(user_newpass: str, token: str = Header(...)):
    user_id = decode_token_user_id(token)
    db_user = db.query(UserDetail).filter(UserDetail.id == user_id, UserDetail.is_active == True, UserDetail.is_verified == True, UserDetail.is_deleted == False).first()
    
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not db_user.is_verified:
        return "User not verified"
    
    db_user.password = pwd_context.hash(user_newpass)
    db.commit()
    return "Forget Password successfully"



@user_log.get("/get_token")
def encode_token(id: str,email: str,password: str):
    access_token = get_token(id,email,password)
    return access_token

