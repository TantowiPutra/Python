import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = 1

if weekday == 1:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        all_quotes = list(map(lambda x: x.strip(), all_quotes))

    quote = random.choice(all_quotes)

    my_email = "tantowi675811@gmail.com"
    password = "xxnw ldce dqmw bgor"  # app password

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Today's Quotes\n\n{quote}"
        )
