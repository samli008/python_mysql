# sync demo
import time
from datetime import datetime

def print_message(interval_seconds,message='keep alive'):
    while True:
        print(f'{datetime.now()}-{message}')
        start=time.time()
        end=start+interval_seconds
        while True:
            now=time.time()
            if now >= end:
                break

if __name__=="__main__":
    print_message(3,'three')

"""
[root@c03 ~]# python sync.py 
2020-02-19 04:07:45.001575-three
2020-02-19 04:07:48.001747-three
2020-02-19 04:07:51.001896-three
2020-02-19 04:07:54.002028-three
2020-02-19 04:07:57.002158-three
2020-02-19 04:08:00.002328-three
"""

# async demo with yield next()
import time
from datetime import datetime

def print_message(interval_seconds,message='keep alive'):
    while True:
        print(f'{datetime.now()}-{message}')
        start=time.time()
        end=start+interval_seconds
        while True:
            yield
            now=time.time()
            if now >= end:
                break

if __name__=="__main__":
    a=print_message(3,'three')
    b=print_message(10,'ten')
    stack=[a,b]
    while True:
        for task in stack:
            next(task)
"""
[root@c03 ~]# python sync2.py 
2020-02-19 03:47:27.775670-three
2020-02-19 03:47:27.775958-ten
2020-02-19 03:47:30.775959-three
2020-02-19 03:47:33.776087-three
2020-02-19 03:47:36.776254-three
2020-02-19 03:47:37.776009-ten
2020-02-19 03:47:39.776364-three
2020-02-19 03:47:42.776486-three
2020-02-19 03:47:45.776608-three
2020-02-19 03:47:47.776139-ten
"""
