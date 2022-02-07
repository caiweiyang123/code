import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
import readExcel

# 调用我们的geturlParams获取我们拼接的URL
url = geturlParams.GeturlParams().get_url()
login_xls = readExcel.ReadExcel().get_xls("userCase.xls", "login")


@paramunittest.parametrized(*login_xls)
class TestUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        # set params
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description(self):
        # test report description
        return self.case_name

    def setUp(self):
        print(self.case_name + "测试开始前准备")

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完成测试\n\n")

    def checkResult(self):
        url1 = "http://www.xxx.com/login?"
        new_url = url1 + self.query
        # 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        info = RunMain().run_main(self.method, url, data1)
        # 将响应转换为字典格式
        ss = json.loads(info)
        if self.case_name == "login":  # 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(ss["code"], 200, msg="登录成功")
        if self.case_name == "login_error":
            self.assertEqual(ss["code"], -1, msg="参数不正确")
        if self.case_name == "login_null":
            self.assertEqual(ss["code"], 10001, msg="参数不能为空")
