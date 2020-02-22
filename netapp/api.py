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

xi4.child_add_string("size","<size>")
xi4.child_add_string("size-available","<size-available>")

xi5 = NaElement("volume-state-attributes")
xi1.child_add(xi5)

xi5.child_add_string("state","<state>")
xi5.child_add_string("status","<status>")
api.child_add_string("max-records","1000")

xo = s.invoke_elem(api)

#print (xo.sprintf())

result=xo.child_get("attributes-list")
res=xo.child_get("attributes-list").children_get()
print('result type',type(result))
print('res type',type(res))
print("{node:10}{name:10}{style:10}{type:10}{state:10}{size:10}".format(node="node",name="name",style="style",type="type",state="state",size="size"))
for i in res:
  node=i.child_get("volume-id-attributes").child_get_string("node")
  name=i.child_get("volume-id-attributes").child_get_string("name")
  style=i.child_get("volume-id-attributes").child_get_string("style")
  type=i.child_get("volume-id-attributes").child_get_string("type")
  state=i.child_get("volume-state-attributes").child_get_string("state")
  size=int(i.child_get("volume-space-attributes").child_get_string("size"))
  size=str(size/1024/1024)
  mb="MB"
  print(f"{node:10}{name:10}{style:10}{type:10}{state:10}{size}{mb}")
