import datetime

today = datetime.date.today()
formattedDate = today.strftime("%d-%m-%y")

print("Welcome to the session.")

print("Today's Date: " + formattedDate)