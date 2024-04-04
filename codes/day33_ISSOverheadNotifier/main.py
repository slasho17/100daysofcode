import requests
from datetime import datetime
import smtplib
import time
MY_LATITUDE = -22.865510
MY_LONGITUDE = -47.045018
APROXIMATION = 5

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="teasertester39@gmail.com", password="Senha74@teste")
        connection.sendmail(
            from_addr="teasertester39@gmail.com",
            to_addrs="b.veiga74@gmail.com",
            msg="Subject:ISS overhead notifier\n\nLook up"
        )

def is_dark():
    parameters = {
        'lat': MY_LATITUDE,
        'lng': MY_LONGITUDE,
        "formatted": 0,
        "tzid": "America/Sao_Paulo"
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sun_data = response.json()

    sunrise_hour = sun_data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset_hour  = sun_data["results"]["sunset"].split("T")[1].split(":")[0]
    now_hour = datetime.now().hour

    return now_hour < int(sunrise_hour) or now_hour > int(sunset_hour)

def is_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    print(iss_longitude, iss_latitude)
    print(MY_LONGITUDE, MY_LATITUDE)
    # This return doesn't work the best because the values can be negative
    return (MY_LATITUDE - APROXIMATION <= iss_latitude or MY_LATITUDE + APROXIMATION >= iss_latitude) and (MY_LONGITUDE - APROXIMATION <= iss_longitude or MY_LONGITUDE + APROXIMATION >= iss_longitude)

while True:
    if is_dark() and is_overhead():
        send_email()
        time.sleep(600)
    else:
        time.sleep(60)
