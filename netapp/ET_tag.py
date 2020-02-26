# get xml node tree
import xml.etree.ElementTree as ET

def walkData(node,level): 
  global layer
  count=len(node.tag)
  print(node.tag.rjust(count+level))

  #for sub_nodes
  children = node.getchildren() 
  if len(children) == 0: 
    return

  for child in children: 
    walkData(child,level+2) 
  return 
 
def getXml(xml): 
  level=0
  root = ET.parse(xml).getroot() 
  walkData(root,level) 
  
if __name__ == '__main__':
  xml=input("pls input xml name: ")
  getXml(xml)   
