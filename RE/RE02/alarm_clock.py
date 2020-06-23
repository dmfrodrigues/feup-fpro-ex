import datetime
time_begin = datetime.datetime.now()
print("%d:%d"%(time_begin.hour, time_begin.minute))
tdif = 8*60*60 + 30*60
time_now = datetime.datetime.now()
dif = time_now - time_begin
tdif_ = dif.days*24*60*60 + dif.seconds
while tdif_ < tdif:
    time_now = datetime.datetime.now()
    dif = time_now - time_begin
    tdif_ = dif.days*24*60*60 + dif.seconds
print("%d:%d"%(time_now.hour, time_now.minute))
