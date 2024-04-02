import pandas as pd
import datetime as dt
import smtplib
import random

MYEMAIL = "manish.d3036@gmail.com"
PASSWORD = "oaugeawisgrjujsg"

now = dt.datetime.now()
today = (now.month, now.day)

data = pd.read_csv("birthdays.csv")
print(data)
birthdays_dict = {(int(row['month']), row['day']): row for (index, row) in data.iterrows()}
print(birthdays_dict)

if today in birthdays_dict:
    person = birthdays_dict[today]
    print(person['name'])
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    print(file_path)
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MYEMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MYEMAIL,
            to_addrs=person['email'],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
