import xml.etree.ElementTree as ET

tree=ET.parse('li.xml')
root=tree.getroot()

print("{node:10}{name:10}{style:10}{type:10}{state:10}{size:15}{available:15}{used:5}".format(node="node",name="name",style="style",type="type",state="state",size="size",available="available",used="used"))

for i in root[0]:
  for j in i.findall('volume-id-attributes'):
    name=j.find('name').text
    node=j.find('node').text
    style=j.find('style').text
    type=j.find('type').text

  for j in i.findall('volume-state-attributes'):
    state=j.find('state').text

  for j in i.findall('volume-space-attributes'):
    size=int(int(j.find('size').text)/1024/1024)
    size=str(size)+'MB'
    available=int(int(j.find('size-available').text)/1024/1024)
    available=str(available)+'MB'
    used=int(j.find('percentage-size-used').text)
    used=str(used)+'MB'

  print(f"{node:10}{name:10}{style:10}{type:10}{state:10}{size:15}{available:15}{used:5}") 

for vol in root.iter('name'):
  print(vol.text)

for i in root:
  print(i.tag,i.attrib)
