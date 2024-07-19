from dotenv import load_dotenv
import os
load_dotenv()
db_url = os.environ.get("DB_URL")

sender_email = os.environ.get("sender_email")
email_password = os.environ.get("email_password")