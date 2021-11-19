import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "javashop", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("update javashop.es_goods set name ='旺旺挑豆随手包海苔花生11110g/袋' where goods_id =9;")
db.commit()


# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print ("Database version : %s " % data)

# 关闭数据库连接
db.close()