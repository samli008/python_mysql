import xml.etree.ElementTree as ET

tree=ET.parse('c04.xml')
root=tree.getroot()

for vcpu in root.iter('vcpu'):
  vcpu.attrib['current']='1'
  vcpu.text='5'
  print(vcpu.attrib['current'])
  print(vcpu.text)

for mem in root.iter('currentMemory'):
  mem.text='2048000'
for memory in root.iter('memory'):
  memory.text='2048000'

tree.write('c04.xml')
