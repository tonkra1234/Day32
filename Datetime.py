import datetime as dt

now = dt.datetime.now()
year = now.year
print(year) # type >>> int
print(now) # type >>> datetime object

date_time_birth =dt.datetime(year=1999,month=1,day=8)
print(date_time_birth)

date_time_birth1 =dt.datetime(year=1999,month=1,day=8,hour=10,minute=30)
print(date_time_birth1)