# pip3 install pyyaml -i https://mirrors.aliyun.com/pypi/simple
import yaml

with open('mysql.yaml','r') as f:
  result=yaml.load(f,Loader=yaml.FullLoader)
  print(result)
  print(type(result))

"""
mysql.yaml

mysql:
  host: 192.168.20.161
  port: 3306
  username: root
  password: liyang
"""
