import smtplib
import datetime as dt
import random

MY_EMAIL = "nihaopython21@gmail.com"
MY_PASSWORD = "helloPython!9"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes).strip().encode('ascii', 'ignore')
        quote = quote.decode("utf-8", "ignore")

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Works Now!\n\n{quote}."
        )

