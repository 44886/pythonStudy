# 44886
# 学习作用，py操作xls
# 一个简单的九九乘法表的生成
# 2019-03-15
from openpyxl import Workbook
wb = Workbook()  # 创建文件对象
ws1 = wb.active  # 活跃的sheet
ws1.title = "数据"



# 思路：共9行，每行分别是1,2,3,4,5,6,7,8,9个内容
# 用两层循环来进行

foo = 1
while foo <= 9:
    i = 1
    row = []    # 用一个列表来存储 每一行的 i 个乘式
    while i <= foo:
        row.append("{}x{}={}".format(i, foo, foo*i))
        i = i+1
    ws1.append(row) #把刚刚那行，添加进表格中
    foo = foo+1

# 生成文件
wb.save("sample.xlsx")
