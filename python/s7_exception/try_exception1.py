# try and exception
try:
  f=open('a.txt','r')
  f.close()
  print('ok')
except:
  print('not found file')

print('finished')
