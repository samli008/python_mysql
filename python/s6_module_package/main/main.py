import sys
sys.path.append('/root/git/python_mysql/python/s6_module_package')
del sys.path[0]
print(sys.path)
from main.math_func import add
def main():
  print(add(11,12))

main()
