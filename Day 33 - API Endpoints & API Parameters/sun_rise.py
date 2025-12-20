import requests
import datetime as dt
import smtplib

MY_LAT = 102.291023
MY_LONG = -8.1827371

def is_iss_overhead():
    # Get ISS Position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data     = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data['iss_position']["longitude"])

    # Your Position is within +5 or - 5 degree of the iss position
    if MY_LAT <= 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

    return False

def is_night():
    # Get my sunset, sunrise
    url = "https://api.sunrise-sunset.org/json"
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        'formatted': 0  # Matikan Format time ISO 8601
    }

    response = requests.get(url=url, params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

    return False

if is_iss_overhead() and is_night():
    my_email = "tantowi675811@gmail.com"
    password = "xxnw ldce dqmw bgor"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="tantowi675811@yahoo.com",
            msg="Subject: Look Up\n\nThe ISS is above you in the sky."
        )
