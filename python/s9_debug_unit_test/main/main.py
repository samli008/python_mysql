import sys
del sys.path[0]
sys.path.append('/root/git/python_mysql/python/s9_debug_unit_test')
print(sys.path)

from main.math_func import add

def main():
  print(add(8,7))

main()
