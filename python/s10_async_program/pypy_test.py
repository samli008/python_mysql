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

# install pypy
tar xzvf pypy36.tar
sh pypy.sh

"""
[root@c03 ~]# pypy pypy_test.py 
10^1:3.814697265625e-05
10^2:0.00010132789611816406
10^3:0.004961490631103516
10^4:0.0002181529998779297
10^5:0.0018601417541503906
10^6:0.010174751281738281
10^7:0.09891963005065918
10^8:0.9911918640136719
10^9:9.927046537399292
"""
[root@c03 ~]# python
Python 3.6.8 (default, Aug  7 2019, 17:28:10) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-39)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
[root@c03 ~]# pypy
Python 3.6.9 (1608da62bfc7, Dec 23 2019, 10:50:04)
[PyPy 7.3.0 with GCC 7.3.1 20180303 (Red Hat 7.3.1-5)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>>
