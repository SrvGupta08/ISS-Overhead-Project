''' Check the current location of International Space System (ISS) using APIs, date time and SMTP library and if it is near your location during the night time then send yourself an Email to look up in the sky. '''

import requests
from datetime import datetime
import smtplib

MY_LATITUDE = 22.585905
MY_LONGITUDE = 88.326520
MY_EMAIL = "sourav@gmail.com"
MY_PASSWORD = "shagdjhasgdjh"

time_now = datetime.now()

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

iss_latitude = data["iss_position"]["latitude"]
iss_longitude = data["iss_position"]["longitude"]

print(iss_latitude, iss_longitude)

def my_location():
    if (MY_LATITUDE - 5) <= iss_latitude <= (MY_LATITUDE + 5) and (MY_LONGITUDE - 5) <= iss_longitude <= (MY_LONGITUDE + 5):
        return time_now.hour
    else:
        return False

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password = MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = "souravgupta0809@yahoo.com",
            msg = "Subject: Look Up\n\nLook up in the sky" 
        )

if my_location() >= 17 or my_location() <= 5:
    send_email()
else:
    pass
