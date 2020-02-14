import sys
sys.path.append('/root/git/python_mysql/python/s6_module_package')
from module1_package.module1 import sum
#print(sys.path)
a=sum(1,3,5)
print(a)
