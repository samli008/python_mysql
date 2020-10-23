#! /usr/bin/env python
# -*- coding: cp936 -*-
import paramiko
import time
starttime = time.strftime('%Y-%m-%d %T')
start_info = "开始时间："+str(starttime)
cmd_filepath = r"c:\netapp\b300.txt"
cmd_file = open(cmd_filepath,"r")
cmds = cmd_file.readlines()
dev_filepath = r"c:\netapp\device_info.txt"
dev_file = open(dev_filepath,"r")
while 1: 
   dev_info = dev_file.readline()
   if not dev_info :
       break
   else :
       devs = dev_info.split(',') 
       ip = devs[0]
       username = devs[1]
       password = devs[2].strip()
       password = password.strip('\n')
       ssh = paramiko.SSHClient()
       ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       ssh.connect(hostname = ip,username = username,password = password)
       print("成功连接",ip)
       command = ssh.invoke_shell()
       time.sleep(3)
       for cmd in cmds:
           command.send(cmd+'\n')
       time.sleep(40)
       output = command.recv(65535).decode()
       log = open(r"c:\netapp\\"+ip+".txt",'a')
       endtime = time.strftime('%Y-%m-%d %T')
       end_info = "结束时间："+str(endtime)
       log.write(start_info+'\n\n'+output+'\n\n'+end_info)
       log.close()
dev_file.close()
