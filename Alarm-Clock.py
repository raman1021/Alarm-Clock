import datetime
from playsound import playsound

alarmhour = int(input("enter the hours: "))
alarmmin = int(input("enter the minutes: "))
alarmAm = input("am/pm: ")


if alarmAm=="pm":
        alarmhour += 12

while True:
    if alarmhour == datetime.datetime.now().hour and alarmmin == datetime.datetime.now().minute:
        print("playing sound..")
        playsound("sound.mp3")
        break