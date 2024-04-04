import pandas as pd
import datetime as dt
import smtplib
import random

birthdays = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
this_month = now.month
this_day = now.day
matching_birthdays = birthdays[(birthdays["day"] == this_day) & (birthdays["month"] == this_month)]

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user="my_dummy_mail@yahoo.com", password="thepasswordisdummy")
    text = ''
    for index, row in matching_birthdays.iterrows():  # Use matching_birthdays instead of birthdays
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
            text = file.read()
        mail = text.replace("[NAME]", row["name"])  # Use row["name"] instead of row["name"]
        connection.sendmail(
            from_addr="my_dummy_mail@yahoo.com",
            to_addrs=row["email"],
            msg=mail
        )