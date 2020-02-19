# pip3 install xlwt -i https://mirrors.aliyun.com/pypi/simple
# pip3 install xlrd -i https://mirrors.aliyun.com/pypi/simple

# excel write with python
import xlwt
workbook=xlwt.Workbook()
liyang=workbook.add_sheet('liyang')
liyang.write(0,0,'name')
liyang.write(0,1,'id')
liyang.write(1,0,'liyang')
liyang.write(1,1,'1929')
workbook.save('/root/liyang.xls')

# excel read with python
import xlrd
workbook = xlrd.open_workbook('/root/liyang.xls')
#liyang = workbook.sheet_by_index(0)
liyang = workbook.sheet_by_name('liyang')
print(liyang.cell(0,0).value )
print(liyang.cell(0,1).value )
print(liyang.cell(1,0).value )
print(liyang.cell(1,1).value )

# excel write with list and for
import xlwt
workbook = xlwt.Workbook()
liyang = workbook.add_sheet('liyang')
data = [
  ['name', 'id'],
  ['liyang', '1929'],
  ['sam', '2111'],
]

for i in range(0, len(data)):
  for j in range(0, len(data[i])):
    liyang.write(i, j, data[i][j] )

workbook.save('/root/sam.xls')

# excel read with list and for
import xlrd
workbook = xlrd.open_workbook('/root/sam.xls')
liyang=workbook.sheet_by_index(0)

for i in range(0,liyang.nrows):
  value = []
  for j in range(0,liyang.ncols):
    value.append(liyang.cell(i,j).value )
  print(value)
