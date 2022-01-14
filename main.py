import datetime

alarmHour = int(input("The Hour do you want to wake up?"))
alarmMinute = int(input("The minute you want to wake up?"))
amPm = str(input("am or pm"))


if(amPm == "pm"):
    alarmHour = alarmHour + 12

while(1 == 1):
    if(alarmHour == datetime.datetime.now().hour and
        alarmMinute == datetime.datetime.now().minute):
        print("Wake up Lazy")
        break


print("exited")


