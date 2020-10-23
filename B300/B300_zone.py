#! /usr/bin/env python
# -*- coding: cp936 -*-
import re
log_filepath = r"c:\netapp\wwn.txt"
log_file = open(log_filepath,"r")
cmds = log_file.readlines()
log = open(r"c:\netapp\\"+"zone.txt",'w')

# storage ports get
vwwn=[]
wwn=[]
sv=[]
for cmd in cmds:
  cmd1=cmd.split()
  if re.search('vport',cmd):
    vwwn.append(cmd1[2])
  if re.search('wwn',cmd):
    wwn.append(cmd1[2])
  if re.search('sv',cmd):
    sv.append(cmd1[2])

# storage virtual zone
word="zonecreate cml_v,\""
for i in range(len(vwwn)):
  word=word+(vwwn[i]+';')
word=word.strip(";")
word=word+"\""
log.write(word+'\n')

# storage port zone
word="zonecreate cml_p,\""
for j in range(len(wwn)):
  word=word+(wwn[j]+';')
word=word.strip(";")
word=word+"\""
log.write(word+'\n')

# server wwn zone
for i in range(len(sv)):
  word="zonecreate "
  word=word+'sv'+str(i)+",\""+sv[i]+";"
  for j in range(len(vwwn)):
    word=word+(vwwn[j]+';')
  word=word.strip(";")
  word=word+"\""
  log.write(word+'\n')

log.close()
log_file.close()