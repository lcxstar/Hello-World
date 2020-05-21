# 读取.xlsx文件
import pandas as pd


path = ''
# 用到read_excel函数，输入的参数为文件的路径，生成DataFrame类型变量
df = pd.read_excel(path)
# Dataframe的shape属性可以查看行、列数目
print(df.shape)

# Dataframe的columns属性可以查看表头
# 默认使用第0行作为表头，可以使用columns参数指定表头所在的行，首行全为空值时可以不指定
print(df.columns)

# 要查看列表内容，可以只读入前几行
de = pd.read_excel(path, header=3)

# 设置某列作为索引列，加上inplace参数可以直接覆盖原数据
de.set_index('col1', inplace=True)
print(de.columns)

# 若excel文件中缺少列名，需要在读取时设置headers = None,默认生成columns为0,1,2……
dw = pd.read_excel(path, header=None)

# 读取文件后可以自定义columns
dw.columns = ['col1', 'col2', 'col3']
print(dw.columns)

# 直接保存的excel文件列名已经加好，但默认index没有删除，去掉自定义的index有两种方法
# （1）第一中方法是将index更改后重新赋值给dw
# dw = dw.set_index('col')

# （2）第二种方法加上inplace参数
dw.set_index('name', inplace=True)

de.to_excel(path)
