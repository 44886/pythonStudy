# 44886
# 学习作用，py操作xls
# 一个简单的九九乘法表的生成
# 2019-03-15
from openpyxl import Workbook
wb = Workbook()  # 创建文件对象
ws1 = wb.active  # 活跃的sheet
ws1.title = "数据"

foo = 1
while foo <= 9:
    i = 1
    row = []
    while i <= foo:
        row.append("{}x{}={}".format(i, foo, foo*i))
        i = i+1
    ws1.append(row)
    foo = foo+1

# 生成文件
wb.save("sample.xlsx")
