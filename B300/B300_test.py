#! /usr/bin/env python
# -*- coding: cp936 -*-
import re
log_filepath = r"c:\netapp\log.txt"
log_file = open(log_filepath,"r")
cmds = log_file.readlines()
log = open(r"c:\netapp\\"+"port.txt",'w')
for cmd in cmds:
	cmd1=cmd.split()
	if len(cmd1) != 0 and (cmd1[0].isdigit()) and not (re.search('No_Module',cmd)):
		log.write(cmd)
log.close()
log_file.close()