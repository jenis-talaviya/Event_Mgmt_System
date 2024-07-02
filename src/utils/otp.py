import random
import smtplib
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime,timedelta
from src.schemas.userschemas import OtpRequest
from src.models.userdetail import OTPDetail

# Jeni$@ 3178
# zgho imvl npze rzkv

#ova game
#game pc iso

# Email configuration
# sender_email = "jenistalaviya404@gmail.com"
# receiver_email = "jenistalaviya3178@gmail.com"
# password = "zghoimvlnpzerzkv"
# subject = "Your OTP Code"
# otp = str(random.randint(100000,999999))
# message_text = f"Your OTP is {otp} which is valid for 1 minute"


# # Create the email message
# message = MIMEMultipart()
# message["From"] = sender_email
# message["To"] = receiver_email
# message["Subject"] = subject

# # Attach the message text
# message.attach(MIMEText(message_text, "plain"))


# # Send the email
# try:
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message.as_string())
#     print("Mail sent successfully")
#     server.quit()
# except Exception as e:
#     print(f"Failed to send email: {e}")
    
    
#--------------------------------------------------------------------------------


def generate_otp(length=6):
    digits = string.digits
    return ''.join(random.choice(digits) for _ in range(length))

def send_otp_via_email(sender_email, receiver_email, password, otp):
    subject = "Your OTP Code"
    message_text = f"Your OTP is {otp} which is valid for 10 minutes"

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the message text
    message.attach(MIMEText(message_text, "plain"))

    # Send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        return True, "Mail sent successfully"
    except Exception as e:
        return False, f"Failed to send email: {e}"
    
    
    
#------------------------------email for payment system-------------------------
def send_email(sender_email, receiver_email, password, transaction_id):
    subject = "Your Transaction ID"
    message_text = f"Your transaction ID is {transaction_id}"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(message_text, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        return True, "Email sent successfully"
    except Exception as e:
        return False, f"Failed to send email: {e}"