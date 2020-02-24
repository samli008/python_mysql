import xml.etree.ElementTree as ET

tree=ET.parse('c04.xml')
root=tree.getroot()

for vcpu in root.iter('vcpu'):
  vcpu.attrib['current']='1'
  print(vcpu.attrib['current'])

for vcpu in root.iter('vcpu'):
  vcpu.text='20'
  print(vcpu.text)

tree.write('c04.xml')
