# pip3 install paramiko -i https://mirrors.aliyun.com/pypi/simple
import paramiko
import sys

ssh = paramiko.SSHClient()
know_host = paramiko.AutoAddPolicy()
ssh.set_missing_host_key_policy(know_host)

ssh.connect(
    hostname = "192.168.20.111",
    port = 22,
    username = "admin",
    password = "netapp123"
)

stdin,stdout,stderr = ssh.exec_command("vserver show;net int show")

with open('li.txt','w') as f:
    f.writelines(stdout)

ssh.close()
