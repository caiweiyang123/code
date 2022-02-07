# import pymysql
#
# conn = pymysql.connect(
#     host="127.0.0.1",
#     port=3306,
#     user="root",
#     password="123456",
#     database="day48",
#     charset="utf8",  # 编码千万不要加 -
# )  # 连接数据库
#
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 产生一个游标对象（就是用来执行命令的对象）
# """
# cursor=pymysql.cursors.DictCursor 将查询结果以字典的形式展示
# """
#
# sql = "select * from teacher;"
# res = cursor.execute(sql)
# # print(res) # execute 返回的是当前sql语句所影响的行数，改进
# # 获取命令执行的查询结果
# # print(cursor.fetchone())  # 只拿一条
# # print(cursor.fetchall())   #拿所有
# # print(cursor.fetchmany(2))  # 可以指定那几条
# print(cursor.fetchone())
# print(cursor.fetchone())# 读取文件类似于文件光标的移动
# # cursor.scroll(1, "relative")  #相对于光标所在的位置继续移动一位
# cursor.scroll(1, "absolute")  #相对于数据的开头往后继续移动一位
# print(cursor.fetchall())

"""
pymysql模块补充
"""
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

# 增加数据
sql = "insert into user(name,password) values(%s,%s);"
# rows = cursor.excute(sql, ("jackson", 123))# 插入单个数据
rows = cursor.executemany(sql, [("jackson", 123),("xxx",123)]) # 插入多个数据
print(rows)
conn.commit()  # 确认
# 修改数据
sql = "update user set username='jasonr' where id=1;"
rows = cursor.excute(sql)
print(rows)
conn.commit()  # 确认
# 查找
sql = "select * from user;"
cursor.execute(sql)
print(cursor.fetchall())

"""
增删改查中
    增删改他们的操作涉及到数据的修改
    需要二次确认
"""
