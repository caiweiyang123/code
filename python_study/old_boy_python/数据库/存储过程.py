import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    passwd="123456",
    db="day48",
    charset="utf8",
    autocommit=True
)

cursor = conn.cursor(pymysql.cursors.DictCursor)
# 调用存储过程
cursor.callproc("p1",(1,5,10))
"""
@_p1_0 = 1
@_p1_1 = 5
@_p1_2 = 10
"""
print(cursor.fetchall())

"""
函数
跟存储过程有区别的，存储过程是自定义函数，函数就是内置函数
流程控制
1. if判断
2. while循环
"""