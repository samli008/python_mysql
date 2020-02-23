# NETAPP NaServer API with python XML
import sys
from NaServer import *

s = NaServer("192.168.20.111", 1 , 160)
s.set_server_type("FILER")
s.set_transport_type("HTTPS")
s.set_port(443)
s.set_style("LOGIN")
s.set_admin_user("admin", "netapp123")

api = NaElement("volume-get-iter")

xi = NaElement("desired-attributes")
api.child_add(xi)

xi1 = NaElement("volume-attributes")
xi.child_add(xi1)

xi2 = NaElement("volume-id-attributes")
xi1.child_add(xi2)

xi3 = NaElement("aggr-list")
xi2.child_add(xi3)

xi3.child_add_string("aggr-name","<aggr-name>")
xi2.child_add_string("junction-path","<junction-path>")
xi2.child_add_string("msid","<msid>")
xi2.child_add_string("name","<name>")
xi2.child_add_string("node","<node>")
xi2.child_add_string("style","<style>")
xi2.child_add_string("type","<type>")
xi2.child_add_string("uuid","<uuid>")

xi4 = NaElement("volume-space-attributes")
xi1.child_add(xi4)

xi4.child_add_string("percentage-size-used","<percentage-size-used>")
xi4.child_add_string("percentage-snapshot-reserve","<percentage-snapshot-reserve>")
xi4.child_add_string("percentage-snapshot-reserve-used","<percentage-snapshot-reserve-used>")
xi4.child_add_string("size","<size>")
xi4.child_add_string("size-available","<size-available>")
xi4.child_add_string("size-used","<size-used>")
xi4.child_add_string("size-used-by-snapshots","<size-used-by-snapshots>")
xi4.child_add_string("snapshot-reserve-available","<snapshot-reserve-available>")
xi4.child_add_string("snapshot-reserve-size","<snapshot-reserve-size>")

xi5 = NaElement("volume-state-attributes")
xi1.child_add(xi5)

xi5.child_add_string("is-cluster-volume","<is-cluster-volume>")
xi5.child_add_string("is-flexgroup","<is-flexgroup>")
xi5.child_add_string("is-node-root","<is-node-root>")
xi5.child_add_string("is-vserver-root","<is-vserver-root>")
xi5.child_add_string("state","<state>")
xi5.child_add_string("status","<status>")
api.child_add_string("max-records","1000")

xo = s.invoke_elem(api)

#print (xo.sprintf())

result=xo.child_get("attributes-list")
res=xo.child_get("attributes-list").children_get()

print("{node:10}{name:10}{style:10}{type:10}{state:10}{size:15}{available:15}{used:5}".format(node="node",name="name",style="style",type="type",state="state",size="size",available="available",used="used"))
for i in res:
  node=i.child_get("volume-id-attributes").child_get_string("node")
  name=i.child_get("volume-id-attributes").child_get_string("name")
  style=i.child_get("volume-id-attributes").child_get_string("style")
  type=i.child_get("volume-id-attributes").child_get_string("type")
  state=i.child_get("volume-state-attributes").child_get_string("state")
  size=int(i.child_get("volume-space-attributes").child_get_string("size"))
  available=int(i.child_get("volume-space-attributes").child_get_string("size-available"))
  used=int(i.child_get("volume-space-attributes").child_get_string("percentage-size-used"))
  size=str(int(size/1024/1024))+'MB'
  available=str(int(available/1024/1024))+'MB'
  used=str(used)+'%'
  print(f"{node:10}{name:10}{style:10}{type:10}{state:10}{size:15}{available:15}{used:5}")

"""
[root@c03 ~]# python api.py 
result type <class 'NaElement.NaElement'>
res type <class 'list'>
node      name      style     type      state     size      available used 
zw-01     svm_root  flex      rw        online    20MB      18MB      4%   
zw-01     vol0      flex      rw        online    807MB     40MB      94%  
zw-02     vol0      flex      rw        online    807MB     93MB      87%
"""
