import pymysql

def main():
    no = int(input("要删除的部门编号："))
    loc = input("部门的新地址：")
    # 1.创建连接对象
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123456", database="student",
                           charset="utf8")
    try:
        # 2.获得游标对象
        with conn.cursor()as cur:
            # 3.执行SQL得到结果
            result = cur.execute("select * from student;")
            if result == 1:
                print("添加成功")
            # 4. 操作成功执行提交
            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        # 5.关闭数据库释放资源
        conn.close()

if __name__ == '__main__':
    main()