# 持久化保存：文件
# list 元组，字典---》内存
# encode = utf-8

# 用户注册
def register():
    username = input("输入用户户名：")
    password = input("输入密码：")
    repassword = input("请确认密码：")

    if password == repassword:
        # 保存信息
        with open(r"f:\p1\book\user.txt", "a")as wstream:
            wstream.write(f"{username} {password}\n")
        print("注册成功！")
    else:
        print("两次密码不一致！")


# 用户登录
def login():
    username = input("输入用户名")
    password = input("输入密码：")
    input_user = f"{username} {password}\n"
    if username and password:
        while True:
            with open(r"f:\p1\book\user.txt", "r")as rstream:
                user = rstream.readline()
            if user == input_user:
                print("登录成功！")
                break
            if not user:
                print("用户名或者密码错误！")
                break


# 展示书
def show_books():
    print("----------图书馆的书------------")
    with open(r"f:\p1\book\books.txt", "r", encoding="utf-8")as rstream:
        books = rstream.readlines()
        for book in books:
            print("图书馆里有" + book, end="")


show_books()
