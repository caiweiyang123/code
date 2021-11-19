import pymysql


def main():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123456", database="student",
                           charset="utf8")

    try:
        with conn.cursor()as cur:
            result = cur.execute("select * from student;")
            if result == 1:
                print("添加成功")
            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    main()
