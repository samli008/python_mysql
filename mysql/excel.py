# pip3 install xlwt -i https://mirrors.aliyun.com/pypi/simple
# pip3 install xlrd -i https://mirrors.aliyun.com/pypi/simple

# excel write with python
import xlwt

book=xlwt.Workbook()
sheet=book.add_sheet('liyang')

print(type(book))
print(type(sheet))
print(isinstance(book,xlwt.Workbook))
print(isinstance(sheet,xlwt.Worksheet))

sheet.write(0,0,'name')
sheet.write(0,1,'id')
sheet.write(1,0,'liyang')
sheet.write(1,1,'1929')
book.save('/root/liyang.xls')

# excel read with python
import xlrd
book = xlrd.open_workbook('/root/liyang.xls')
#sheet = book.sheet_by_index(0)
sheet = book.sheet_by_name('liyang')
print(sheet.cell(0,0).value )
print(sheet.cell(0,1).value )
print(sheet.cell(1,0).value )
print(sheet.cell(1,1).value )

# excel write with list and for
import xlwt
book = xlwt.Workbook()
sheet = book.add_sheet('liyang')
data = [
  ['liyang', '18116588888',40],
  ['samli008', '18116587777',38],
  ['sam', '18116589999',39],
]

for i in range(0, len(data)):
  for j in range(0, len(data[i])):
    sheet.write(i, j, data[i][j] )

book.save('/root/sam.xls')

# excel read with list and for
import xlrd
book = xlrd.open_workbook('/root/sam.xls')
sheet=book.sheet_by_index(0)

for i in range(0,sheet.nrows):
  value = []
  for j in range(0,sheet.ncols):
    value.append(sheet.cell(i,j).value )
  print(value)
