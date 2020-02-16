# datatime
>>> from datetime import datetime
>>> cur=datetime(year=2020,month=2,day=16,hour=9,minute=8,second=15,microsecond=5)
>>> cur
datetime.datetime(2020, 2, 16, 9, 8, 15, 5)
>>> cur.date()
datetime.date(2020, 2, 16)
>>> cur.time()
datetime.time(9, 8, 15, 5)

>>> datetime.today()
datetime.datetime(2020, 2, 15, 20, 10, 43, 355899)
>>> datetime.now()
datetime.datetime(2020, 2, 15, 20, 10, 55, 341893)
>>> 

>>> import time
>>> a=time.time()
>>> print(a)
1581815545.132651
>>> datetime.fromtimestamp(a)
datetime.datetime(2020, 2, 15, 20, 12, 25, 132651)

# combine date and time
>>> from datetime import date
>>> from datetime import time
>>> d=date(year=2020,month=2,day=16)
>>> print(d)
2020-02-16
>>> t=time(hour=9,minute=16)   
>>> print(t)
09:16:00
>>> datetime.combine(d,t)
datetime.datetime(2020, 2, 16, 9, 16)

# replace() method
>>> t1=datetime.now()
>>> t1.date()
datetime.date(2020, 2, 15)
>>> t1.time()
datetime.time(20, 19, 55, 170002)

>>> t2=t1.replace(month=t1.month+1)
>>> t2.date()
datetime.date(2020, 3, 15)

>>> t2=t1.replace(month=t1.month+1,day=t1.day+3)
>>> t2.date()
datetime.date(2020, 3, 18)

# delta
>>> t1=datetime.now()
>>> t2=datetime.now()
>>> t=t2-t1
>>> t
datetime.timedelta(0, 128, 638181)
>>> t.seconds
128
>>> t.days
0
>>> t.microseconds
638181

# timedelta
>>> from datetime import timedelta

>>> a=timedelta(days=7,hours=5)
>>> a
datetime.timedelta(7, 18000)

>>> now=datetime.now()
>>> now
datetime.datetime(2020, 2, 15, 20, 34, 55, 808950)

>>> now+a
datetime.datetime(2020, 2, 23, 1, 34, 55, 808950)

# calendar
import calendar
>>> print(calendar.calendar(2020))
