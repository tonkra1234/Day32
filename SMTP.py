# SMTP >>> simple mail transfer protocol >>>> https://docs.python.org/3/library/smtplib.html

import smtplib

"""
gmail >>>> smtp.gmail.com
hotmail >>> smtp.live.com
yahoo >>> smtp.mail.yahoo.com

"""

connection = smtplib.SMTP("smtp.gmail.com")

# TLS >>> Transport layer security
connection.starttls()

connection.login(user="nattawat.08012542@gmail.com", password="Ton25422542")

connection.sendmail(from_addr="nattawat.08012542@gmail.com",
                    to_addrs="tonkr.a@hotmail.com",
                    msg = "Subject:Hello\n\n This is the body of my email")

connection.close()

"""
with  smtplib.SMTP("smtp.gmail.com") as connection:

# TLS >>> Transport layer security
connection.starttls()

connection.login(user="nattawat.08012542@gmail.com", password="Ton25422542")

connection.sendmail(from_addr="nattawat.08012542@gmail.com",
                    to_addrs="tonkr.a@hotmail.com",
                    msg = "Subject:Hello\n\n This is the body of my email")


"""
