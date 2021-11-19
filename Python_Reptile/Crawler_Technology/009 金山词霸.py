import hashlib
import json

import requests


class Fy_spider(object):
    def __init__(self, query_str):
        self.query_str = query_str
        sign = (hashlib.md5(("6key_cibaifanyicjbysdlove1" + self.query_str).encode('utf-8')).hexdigest())[0:16]
        url = 'http://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba'
        self.url = url + '&sign=' + sign
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
        # 获取请求体数据
        self.data = self.get_data()

    def get_data(self):
        """获取请求体数据"""
        data = {
            'from': 'auto',
            'to': 'auto',
            'q': self.query_str
        }
        return data

    def get_data_fromurl(self):
        """从服务器获取数据 并且解码返回"""
        response = requests.post(self.url, headers=self.headers, data=self.data)
        return response.content.decode()

    def parse_data(self, json_str):
        dict_data = json.loads(json_str)
        result = dict_data['content']['out']
        print('{}翻译后的结果{}'.format(query_str, result))

    def run(self):
        json_str = self.get_data_fromurl()
        self.parse_data(json_str)


if __name__ == '__main__':
    query_str = input("请输入翻译的内容：")
    spider = Fy_spider(query_str)
    spider.run()
