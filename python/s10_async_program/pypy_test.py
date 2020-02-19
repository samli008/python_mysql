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
