import unittest
#import HTMLTestRunner  # 导入用于生成测试报告
import project_path  # 读取文件路径
from test_register import TestRegister  # 导入测试类

suite=unittest.TestSuite()

# 1. 加载测试用例：把测试用例放到测试套件suite里面
suite.addTest(TestRegister('test_register_normal'))
suite.addTest(TestRegister('test_register_existing'))
suite.addTest(TestRegister('test_register_invalid_email'))


# 2.运行测试集, 并生成Html测试报告
with open(project_path.report_path,'wb') as file:
    pass
    # runner=HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2,title='ServiceX API Testing',description='ServiceX API Testing',tester='Jiali')
    #runner.run(suite)