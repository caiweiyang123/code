import pandas as pd

df = pd.read_excel('test_pandas.xlsx','成绩表')
# print(df)
# df1 = pd.read_excel('test_pandas.xlsx','成绩表')
# df2 = pd.read_excel('test_pandas.xlsx','成绩表')
# df3 = pd.read_excel('test_pandas.xlsx',1)
# df4 = pd.read_excel('test_pandas.xlsx','业绩表')
# print(df1)
# print(df2)
# print(df3)
# print(df4)
# df = pd.read_csv('1-1.csv', encoding="GB2312")
# print(df)

print(df.index)
print(df.columns)
print(df.values)