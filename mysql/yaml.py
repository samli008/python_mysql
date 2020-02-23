# pip3 install pyyaml -i https://mirrors.aliyun.com/pypi/simple
import yaml

with open('mysql.yaml','r') as f:
  result=yaml.load(f,Loader=yaml.FullLoader)

print(result['mysql']['host'])
print(result['mysql']['username'])
print(result['mysql']['password'])
print(result['mysql']['port'])

# result is class dict

"""
mysql.yaml

mysql:
  host: 192.168.20.161
  port: 3306
  username: root
  password: liyang
"""
