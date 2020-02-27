# pip3 install netapp-ontap -i https://mirrors.aliyun.com/pypi/simple

from netapp_ontap import config
from netapp_ontap.host_connect import HostConnection
from netapp_ontap.resources import Volume

config.CONNECTION = HostConnection('192.168.20.111','admin','netapp123')
config.CONNECTION.verify = False

volume1 = Volume(name='vol_liyang',
		 svm={'name': 'svm1'},
		 aggregates=[{'name': 'aggr1'}])

volume1.post()
