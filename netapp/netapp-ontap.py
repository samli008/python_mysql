# pip3 install netapp-ontap -i https://mirrors.aliyun.com/pypi/simple

# volume create with python
from netapp_ontap import config
from netapp_ontap.host_connection import HostConnection
from netapp_ontap.resources import Volume

config.CONNECTION = HostConnection('192.168.20.111','admin','netapp123',verify=False)
config.CONNECTION.verify = False

vol1=input("input vol name: ")
size1=int(input("input vol size[GB]: "))
size1=int(size1*1024**3)

volume1 = Volume(name=vol1,
                 size=size1,
                 svm={'name': 'svm1'},
                 aggregates=[{'name': 'aggr1_zw01'}])

volume1.post()
