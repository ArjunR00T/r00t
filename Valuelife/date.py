import datetime

d=datetime.date.today()
k=(d+ (datetime.timedelta(days=3))).weekday()
print(k)