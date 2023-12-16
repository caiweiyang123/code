import numpy as np
import pandas as pd

# arr = np.array(['张三','李四','王五'])
# print(arr)
# print(type(arr))
# arr1 = np.array((['张三','李四','王五'],[12,22,55]))
# print(arr1)
# print(type(arr1))

# arr1 =np.arange(4)
# arr2 =np.arange(7,12)
# arr3 =np.arange(100,110,2)
# print(arr1)
# print(arr2)
# print(arr3)

# rnd = np.random.rand()
# arr1 = np.random.rand(4)
# arr2 = np.random.rand(2,4)
# arr3 = np.random.rand(2,4,3)
# print(rnd)
# print(arr1)
# print(arr2)
# print(arr3)

# rndint = np.random.randint(10, 99)
# arr1 = np.random.randint(10, 99, size=(3))
# arr2 = np.random.randint(10, 99, size=(3, 2))
# arr3 = np.random.randint(10, 99, size=(3, 2, 4))
# print(rndint)
# print(arr1)
# print(arr2)
# print(arr3)

# 3.2.4 转换数组


# df = pd.read_excel("test_pandas.xlsx","成绩表")
# arr1 = np.array(df)
# arr2 = df.to_numpy()
# arr3 = df.values
# print(df,type(df))
# print(arr1,type(arr1))
# print(arr2,type(arr2))
# print(arr3,type(arr3))

df = pd.read_excel("test_pandas.xlsx","成绩表")
for t,s in df.items():
    print(t)
    print(s)
# arr = np.array(([100,'123',99]))
# print(arr.astype('int'))
# print(arr.astype('float'))
# print(arr.astype('str'))

# 3.3.2 缺失值处理

# arr = np.array()
