import pandas as pd


# 创建一个Series对象，需要的参数包括内容及索引
s1 = pd.Series([100, 200, 300], index=['x', 'y', 'z'])

# 将多个Series对象组合成一个DataFrame对象
s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[1, 2, 3], name='C')

# （1）以字典的形式将Series加入到DataFrame，每个Series被当做一列
df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})

# （2）以列表的形式将Series加入到DataFrame，每个Series被当做一行
df1 = pd.DataFrame([s1,s2,s3])

# Series中index相同的对象成为一行，若index不相同，则生成新行并用NaN补齐
s4 = s3 = pd.Series([100, 200, 300], index=[2, 3, 4], name='C')
df2 = pd.DataFrame({s1.name: s1, s2.name: s2, s4.name: s4})
