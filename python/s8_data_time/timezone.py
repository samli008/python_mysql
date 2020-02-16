# time zone
pip3 install arrow

>>> import arrow
>>> utc=arrow.utcnow()
>>> utc
<Arrow [2020-02-16T14:06:15.875214+00:00]>

>>> utc.date()
datetime.date(2020, 2, 16)
>>> utc.time()
datetime.time(14, 6, 15, 875214)

# timestamp
>>>import time
>>> t=time.time()
>>> t
1581862562.6568382
>>> t1=utc.fromtimestamp(t)
>>> t1
<Arrow [2020-02-16T09:16:02.656838-05:00]>

# utc8 with utc.to
>>> utc8=utc.to('Asia/Shanghai')
>>> utc8
<Arrow [2020-02-16T22:06:15.875214+08:00]>

>>> utc8.date()
datetime.date(2020, 2, 16)
>>> utc8.time()
datetime.time(22, 6, 15, 875214)

>>> dir(arrow)
['Arrow', 'ArrowFactory', 'ParserError', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_version', 'api', 'arrow', 'constants', 'factory', 'formatter', 'get', 'locales', 'now', 'parser', 'utcnow', 'util']
