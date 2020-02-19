# pip3 install xlrd -i https://mirrors.aliyun.com/pypi/simple
# pip3 install pymysql -i https://mirrors.aliyun.com/pypi/simple

import xlrd
import pymysql

book = xlrd.open_workbook('/root/sam.xls')
sheet=book.sheet_by_index(0)

connection=pymysql.connect("192.168.20.161","root","liyang","liyang")
cursor=connection.cursor()

for i in range(0,sheet.nrows):
  value = []
  for j in range(0,sheet.ncols):
    value.append(sheet.cell(i,j).value )
  sql="insert into person(name,phone,age)values('%s','%s',%s);" % (value[0],value[1],value[2])
  count=cursor.execute(sql)
print('insert',i+1,'rows')

connection.commit()
cursor.close()
connection.close()
