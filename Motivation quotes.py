import smtplib
import datetime as dt
from random import *

username = "nattawat.08012542@gmail.com"
password = "Ton25422542"

now =dt.datetime.now()
weekday = now.weekday()
if weekday == 1:

    with open("quotes.txt") as data:
        data1 = data.readlines()
        number = choice(data1)

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:

        connection.login(user = username,password= password)
        connection.sendmail(from_addr="nattawat.08012542@gmail.com",
                            to_addrs="tonkr.a@hotmail.com",
                            msg=f"Subject:Tuesday motivation\n\n {number}"
                            )