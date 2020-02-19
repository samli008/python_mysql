>>> import time
>>> def foo():
...   for i in range(1000):
...     print(i)
...     time.sleep(0.5)
... 
>>> a=foo()
0
1
2
3
4
5
6

# async with yield
>>>import time
>>> def foo():
...   for i in range(1000):
...     print(i)
...     yield
...     time.sleep(0.5)
... 
>>> a=foo()
>>> a
<generator object foo at 0x7f13f48c8360>
>>> next(a)
0
>>> next(a)
1
>>> next(a)
2
>>> next(a)
3
>>> print('testing')
testing
>>> next(a)
5
>>> next(a)
6
>>> print('testing')
testing
