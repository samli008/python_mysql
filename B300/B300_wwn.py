#! /usr/bin/env python
# -*- coding: cp936 -*-
import re
log_filepath = r"c:\netapp\log.txt"
log_file = open(log_filepath,"r")
cmds = log_file.readlines()
log = open(r"c:\netapp\\"+"wwn.txt",'w')

for cmd in cmds:
   	if re.search('Online',cmd):
   		cmd1=cmd.split()
   		if len((cmd1[len(cmd1)-1])) == 23:
   			log.write(cmd1[0]+' '+'sv'+' '+cmd1[len(cmd1)-1]+'\n')

port="0"
num=0
for cmd in cmds:
    cmd1=cmd.split()
    if len(cmd1) != 0 and re.search('portIndex',cmd):
    	port=cmd1[1]
    if len(cmd1) != 0 and len(cmd1[0]) == 23:
        num+=1
        if (num%2) != 0:
            log.write(port+' '+'vport'+' '+cmd1[0]+'\n')
        else:
            log.write(port+' '+'wwn'+'  '+cmd1[0]+'\n')

log.close()
log_file.close()