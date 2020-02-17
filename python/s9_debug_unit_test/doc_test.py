# doctest
def func_demo(a,b):
  """doc test demo
  >>> func_demo(1,2)
  2
  >>> func_demo('a',3)
  'aaa'
  """
  try:
    return a**b
  except:
    raise ValueError

if __name__=="__main__":
  import doctest
  doctest.testmod()
