import datetime
from playsound import playsound


alarmhour= int(input("hour\n"))
alarmmin = int(input("min\n"))
ampm = input("am/pm\n")
alarm_label =input("enter label\n")

if ampm =="pm":
    alarmhour+=12

while True:
    if alarmhour ==datetime.datetime.now().hour and alarmmin== datetime.datetime.now().minute:
        print(alarm_label)
        playsound("dave.mp3")

        break
