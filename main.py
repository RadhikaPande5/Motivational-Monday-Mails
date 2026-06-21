import smtplib
from datetime import datetime
from random import choice

import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

if datetime.now().weekday() == 0:
    with open("quotes.txt") as quotes_file:
        quotes_list = quotes_file.readlines()
        quote = choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Mailing Monday Quote!\n\n {quote}\n Wish you a Motivational Monday."
        )
