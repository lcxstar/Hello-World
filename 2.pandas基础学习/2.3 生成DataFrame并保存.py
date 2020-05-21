import pandas as pd


# 创建一个DataFrame对象
df = pd.DataFrame({'ID': [1, 2, 3], 'name': ['jack', 'marry', 'des']})

# 默认索引为0,1,2……，使用set_index可以指定某列为索引
df = df.set_index('ID')

# 将DataFrame存储至excel文件中，参数为文件路径
df.to_excel('df.xlsx')
