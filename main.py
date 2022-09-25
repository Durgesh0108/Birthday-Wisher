##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import smtplib
import random
import datetime as dt

EMAIL = "testcode9653@gmail.com"
PASSWORD = "9653320535"

today = dt.datetime.now()
today_tuple = (today.month,today.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {
    (data_row.month,data_row.day): data_row for (index, data_row) in data.iterrows()
}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,to_addrs=birthday_person.email,msg=f"Subject:Happy Birthday\n\n{content}")





