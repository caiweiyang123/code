import pytest
from yaml_util import read_yaml
import requests


class TestApi:

    # 最基本的用法
    # @pytest.mark.parametrize("args", ['百里', '星瑶', '依然', '修习人生'])
    # def test_01_api(self, args):
    #     """
    #     获得网易新闻的接口
    #     :return:
    #     """
    #     print(args)
    # 解包的用法（ddt,unittest这个框架实现数据驱动的装饰器，@unpack）
    @pytest.mark.parametrize("args", read_yaml())
    def test_01_api(self, args):
        """
        获得网易新闻的接口
        :return:
        """
        print(args)
        url = args['api_request']['url']
        method = args['api_request']['method']
        headers = args['api_request']['headers']
        params = args['api_request']['params']
        validate = args['api_validate']
        print(validate)

        if method == 'get':
            requests.get()
        else:
            res = requests.post(url, json=params, )
            for val in validate:
                assert val['eq']['code'] == res.json()['code']

        # print(url)


if __name__ == '__main__':
    pytest.main(['-vs', 'test_api.py'])
