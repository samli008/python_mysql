# python mysql
pip3 install pymysql -i https://mirrors.aliyun.com/pypi/simple
import pymysql

# connect mysql ip user passwd database port
connection=pymysql.connect("192.168.20.161","root","liyang","liyang",3306)
cursor=connection.cursor()
sql="insert into person(name,phone,age)values('xxx','18116583538',40);"
count=cursor.execute(sql)
print(count)
connection.commit()
cursor.close()
connection.close()
