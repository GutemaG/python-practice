import datetime
import pytz  #it is recommended work with pytz when using timezone
d=datetime.date(2016,07,24) #yr,month,day ,,with out houre minute and sec
print (d) #2016-7-26
today=datetime.date.today()
print(today.weekday()) #monday =0.sunday-6
print(today.isoweekday())#monday-1,sunday-7
# timedelta is d/c b/n two times

tdelta=datetime.timedelta(days=7)
print(today+tdelta) # it print 7 days form now
print(today-tdelta)

birthday=datetime.date(2016,9,5)
tillday=birthday-today
print(tillday) # print(tillday.total_seconds)


t=datetime.time(8,40,34,10000)## hr,min,sec,ms, with out yr day and month
print(t) #print(t.hooure),


t2=datetime.datetime(2016,7,26,12,30,45,1000) # yr,month,dat,hr,min,sec,ms
print(t2) #it print both day and time
tdelta=datetime.timedelta(hours=12) #it add 12 ht to the t2
print(t2+tdelta)
print(t2.date())# print only date  t2.year,t2.

dt=datetime.datetime(2016,7,27,12,30,45,tyinfo=pytz.UTC)##
dt_today=datetime.datetime.today() ##
dt_now=datetime.datetime.now(tz=pytz.UTC)##
dt_utcnow=datetime.datetime.utcnow().repalce(tzingo=pytz.UTC)##

dt_mtn=dt.astimezone(pytz.timezone('US/Mountain'))#convert the timezone

# for tz in pytz.all_timezones:#print time all timezone
#     print(tz)

dt=datetime.datetime.now()
print(dt.strftime('%B %d, %Y'))
