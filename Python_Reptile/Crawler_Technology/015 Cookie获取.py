import requests

url = "http://www.baidu.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

# 发送请求。获取response
response = requests.get(url, headers=headers)
print(type(response.cookies))

# 使用方法送cookiejar中获取数据
cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies)
