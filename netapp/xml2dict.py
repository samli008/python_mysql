# pip3 install xmltodict -i https://mirrors.aliyun.com/pypi/simple
import sys
import xmltodict
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

doc=xmltodict.parse(xo.sprintf())
 
a=doc['results']

for k,v in a['attributes-list']['volume-attributes'][0].items():
  print(k,v)

b=a['attributes-list']['volume-attributes']
#print(b[0])
#print(b[1])
#print(b[2])

print(b[0]['volume-id-attributes'])

print(b[0]['volume-id-attributes']['node'])
print(b[0]['volume-id-attributes']['name'])
print(b[0]['volume-id-attributes']['type'])

