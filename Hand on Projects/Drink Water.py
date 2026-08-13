import time
from plyer import notification

while True:
    print("Please sip some water!")
    notification.notify(Title = "Please drink some water", message = "You need to drink some water")
    time.sleep(60 * 60)
    