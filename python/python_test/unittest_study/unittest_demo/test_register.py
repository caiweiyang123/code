import unittest
import requests

class TestRegister(unittest.TestCase):  # 类必须以Test开头，继承TestCase

    def setUp(self):
        print("======开始执行测试用例======")
        self.url = 'http://27.154.55.14:8180/api/fcb2bcrm/webRegister'

    def tearDown(self):
        print("======测试用例执行完毕======")

    # 测试用例 - 正常注册
    def test_register_normal(self):  # 每一条测试用例以test_开头
        # 发送请求
        params = {'LoginAccount': 'apitest08@emai.com', 'Password': '123456', 'Type': 'Pro'}
        res = requests.post(self.url,params)
        # 断言：根据实际测试场景，可以查询数据库是否有新注册的用户、对比接口的返回信息、对比状态码等等
        self.assertEqual(200, res.status_code)

    # 测试用例 - 重复注册
    def test_register_existing(self):
        # 发送请求
        params = {'LoginAccount': 'apitest05@emai.com', 'Password': '123456', 'Type': 'Pro'}
        res = requests.post(self.url,params)
        # 断言
        print("执行结果:", res.json()['Message'])
        self.assertIn("The email has been registered", res.json()['Message'])

    # 测试用例 - 无效的邮箱格式去注册
    def test_register_invalid_email(self):
        # 发送请求
        params = {'LoginAccount': 'testapi@emai', 'Password': '123456', 'Type': 'Pro'}
        res = requests.post(self.url,params)
        # 断言
        print("执行结果:", res.json()['Message'])
        self.assertIn("valid email", res.json()['Message'])

if __name__ == '__main__':  # 从当前模块执行
    unittest.main()