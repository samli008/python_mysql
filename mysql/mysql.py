# python mysql
pip3 install pymysql -i https://mirrors.aliyun.com/pypi/simple
import pymysql

# connect mysql with ip user passwd database port
connection=pymysql.connect("192.168.20.161","root","liyang","database1",3306)
cursor=connection.cursor()

sql="insert into person(name,phone,age)values('xxx','18116583538',40);"
count=cursor.execute(sql)
print(count)
connection.commit()

cursor.close()
connection.close()

# search database default result is tuple
connection=pymysql.connect("192.168.20.161","root","liyang","database1")
cursor=connection.cursor()

sql="select * from person;"
count=cursor.execute(sql)
print(count)
result=cursor.fetchall()
print(result)

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

cursor.close()
connection.close()
