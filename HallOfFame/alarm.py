def alarm(hour, minutes):
    minutes += 60*6 + 51
    hour += minutes//60
    minutes %= 60
    hour %= 24
    return "%02d:%02d"%(hour,minutes)

while True:
    print(alarm(int(input("hour:")), int(input("minutes:"))))
