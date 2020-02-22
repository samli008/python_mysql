with open('li.txt','r') as f:
  for line in f:
    tmpline=line.split()
    if len(tmpline) >=4:
      if tmpline[0]=='Logical':
        print(tmpline[0],tmpline[-1])
      if tmpline[1]=='Interface':
        print(tmpline[1],tmpline[-1])
      if tmpline[-1]=='false':
        role=tmpline[0]
        is_home=tmpline[-1]
        print(role,is_home) 
