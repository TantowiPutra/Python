import smtplib

my_email = "tantowi675811@gmail.com"
password = "xxnw ldce dqmw bgor"  # app password

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="tantowi675811@yahoo.com",
        msg="Subject: Test\n\nHello 3"
    )