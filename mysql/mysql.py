# pip3 install pymysql -i https://mirrors.aliyun.com/pypi/simple
import pymysql

# connect mysql with ip user passwd database port
connection=pymysql.connect("192.168.20.161","root","liyang","database1",3306)
cursor=connection.cursor()

sql="insert into person(name,phone,age)values('xxx','18116583538',40),('li','18116583538',40);"
count=cursor.execute(sql)
print(count)
connection.commit()

cursor.close()
connection.close()

# connect mysql insert into rows with list and for
connection=pymysql.connect("192.168.20.161","root","liyang","database1")
cursor=connection.cursor()

data = [
  ['sam1', '1811177998',35],
  ['sam2', '1811177997',34],
  ['sam3', '1811177995',37],
]
for i in range(0,len(data)):
  sql="insert into person(name,phone,age)values('%s','%s',%s);" % (data[i][0],data[i][1],data[i][2])
  count=cursor.execute(sql)
print('insert',i+1,'rows')
connection.commit()

cursor.close()
connection.close()

# search database default result is double tuple
connection=pymysql.connect("192.168.20.161","root","liyang","database1")
cursor=connection.cursor()

sql="select * from person;"
count=cursor.execute(sql)
print(count)
result=cursor.fetchall()
#print(result)

for one in result:
  print(f"{one['name']},{one['phone']},{one['age']}")

cursor.close()
connection.close()

# search database with dictionary cursor
connection=pymysql.connect("192.168.20.161","root","liyang","database1")
cursor=connection.cursor(pymysql.cursors.DictCursor)

sql="select * from person;"
count=cursor.execute(sql)
print(count)
result=cursor.fetchall()
print(result)

for one in result:
  print("name is {0}".format(one['name']))
  print("phone is {0}".format(one['phone']))
  print("age is {0}".format(one['age']))

cursor.close()
connection.close()
