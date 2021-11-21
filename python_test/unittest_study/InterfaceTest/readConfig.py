import os
import configparser
import getpathInfo  # 引入我们自己的写的获取路径的类

# 这句话是在path路径下再加一级，最后变成E:\pyproject\code\python_test\unittest_study\InterfaceTest\config.ini
path = getpathInfo.get_Path()
# 调用实例化，还记得这个类返回的路径为E:\pyproject\code\python_test\unittest_study\InterfaceTest
config_path = os.path.join(path, "config.ini")
# 调用外部的读取配置文件的方法
config = configparser.ConfigParser()
config.read(config_path, encoding="utf-8")


class ReadConfig():

    def get_http(self, name):
        value = config.get("HTTP", name)
        return value

    def get_email(self, name):
        value = config.get("EMAIL", name)
        return value

    # 写好，留以后备用。但是因为我们没有对数据库的操作，所以这个可以屏蔽掉
    def get_mysql(self, name):
        value = config.get("DATABASE", name)
        return value


if __name__ == '__main__':
    print("HTTP中的baseurl值为：", ReadConfig().get_http("baseurl"))
    print("EMAIL中的on_off值为：", ReadConfig().get_email("on_off"))
