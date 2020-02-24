import xml.etree.ElementTree as ET

tree=ET.parse('c04.xml')
root=tree.getroot()

for vcpu in root.iter('vcpu'):
  vcpu.attrib['current']='2'
  vcpu.text='10'
  print(vcpu.attrib['current'])
  print(vcpu.text)

tree.write('c04.xml')
