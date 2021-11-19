import requests


class Tieba_spider(object):
    def __init__(self, text):
        self.text = text
        self.url = 'https://tieba.baidu.com/f?kw=' + text + '&pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

    def get_url_list(self):
        """生成url列表"""
        list_url = [self.url.format(i * 50) for i in range(5)]
        return list_url

    def get_data_fromurl(self, url):
        """从服务器获取数据 并且解码返回"""
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_html(self, html_str, num):
        """保存本地"""
        filename = "贴吧_" + text + "第{}页".format(num) + ".html"
        with open(filename, 'w', encoding='utf-8')as f:
            f.write(html_str)

    def run(self):
        # 确定url  生成url列表
        list_url = self.get_url_list()
        for item_url in list_url:
            html_str = self.get_data_fromurl(item_url)

            # 保存
            self.save_html(html_str, list_url.index(item_url) + 1)


if __name__ == '__main__':
    text = input("请输入贴吧的名字：")
    spider = Tieba_spider(text)
    spider.run()

    # url = 'https://tieba.baidu.com/f?kw={}&pn={}'
    # text = input("请输入贴吧的名字：")
    # list_url = [url.format(text, i * 50) for i in range(5)]
    # # print(list_url)
    #
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
    # for item_url in list_url:
    #     res = requests.get(item_url, headers=headers)
    #
    # filename = "贴吧_" + text + "第{}页".format(list_url.index(item_url) + 1) + ".html"
    # with open(filename, 'w', encoding='utf-8')as f:
    #     f.write(res.content.decode())
