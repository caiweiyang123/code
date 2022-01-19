"""
    有参装饰器模板
        def auth(db_type): 最外层负责传参数（可以有多个参数）
            def deco(func): 装饰哪个函数
                def wrapper(*args, **kwargs): 装饰的代码
                    pass
                return wrapper
            return deco
    多层装饰器的加载顺序是自下而上的，执行顺序是自上而下的

"""
# 有参装饰器
def auth(db_type):
    def deco(func):
        def wrapper(*args, **kwargs):
            if db_type == 'file':
                name = input("your name>>>: ", ).strip()
                pwd = input("your pwd>>>: ", ).strip()
                if name == "admin" and pwd == "123456":
                    print("基于文件的验证")
                    res = func(*args, **kwargs)
                    return res
                else:
                    print("登陆失败")
            else:
                pass
        return wrapper
    return deco


@auth('file')
def index(x, y):
    print("index->>>%s:%s" %(x, y))\

@auth
def home(x, y):
    print("home->>>%s:%s" %(x, y))

@auth
def dbever(x, y):
    print("dbever->>>%s:%s" %(x, y))


index(1,2)
