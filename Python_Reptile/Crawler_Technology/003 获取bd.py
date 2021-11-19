import requests

image_url = 'https://www.baidu.com/s?wd={}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
text = input("请输入要搜索的内容：")
res = requests.get(image_url.format(text), headers=headers)

print(res.content.decode())

