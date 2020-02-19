# pypy test
import time

def test():
  for i in range(1,10):
    n=pow(10,i)
    start_time=time.time()
    sum(x for x in range(1,n+1))
    end_time=time.time()
    print(f'10^{i}:{end_time-start_time}')

test()

"""
[root@c03 ~]# python pypy_test.py 
10^1:6.198883056640625e-06
10^2:1.8835067749023438e-05
10^3:0.00012183189392089844
10^4:0.0012705326080322266
10^5:0.012715578079223633
10^6:0.12456226348876953
10^7:1.226715087890625
10^8:12.505234479904175
10^9:122.98608946800232
"""

