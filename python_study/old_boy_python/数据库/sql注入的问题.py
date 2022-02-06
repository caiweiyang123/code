"""
sql 注入问题
    利用一些语法的特性 书写一些特点的语句实现固定的语法
    mysql利用的是MySql的注释语法
    select * from user where name = 'jason' --hfij2824323
    select * from user where name = 'xxx' or 1=1   --hfij28asfddf24323
日常生活中很多软件注册的时候不允许含有特殊符号
因为怕你构造出特定的语句入侵数据库，不安全。
# 敏感的数据不要自己做拼接，交给execute帮我拼接即可
"""
import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="123456",
    database="day48",
    charset="utf8",  # 编码千万不要加 -
)  # 连接数据库

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 产生一个游标对象（就是用来执行命令的对象）

username = input("请输入用户名：")
password = input("请输入密码：")

sql = f"select * from user where user= %s and password=%s"
# 不要手动拼接数据， 先用%s占位，之后将需要拼接的数据直接交给execute方法即可
print(sql)

rows = cursor.execute(sql, (username, password))  # 自动识别sql百分号s用后面元组去替换
if rows:
    print("用户登录成功！")
    cursor.fetchall()
else:
    print("用户登陆失败！")

"""
总结：熟悉pymysql的使用
sql注入产生的原因和解决方法  了解
"""
