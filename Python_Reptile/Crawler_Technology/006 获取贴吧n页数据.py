import requests

url = 'https://tieba.baidu.com/f?kw={}&pn={}'
text = input("请输入贴吧的名字：")
list_url = [url.format(text, i * 50) for i in range(5)]
# print(list_url)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
for item_url in list_url:
    res = requests.get(item_url, headers=headers)

    filename = "贴吧_" + text + "第{}页".format(list_url.index(item_url) + 1) + ".html"
    with open(filename, 'w', encoding='utf-8')as f:
        f.write(res.content.decode())
