import requests

url = "https://www.baidu.com"

proxies = {
    "http": "http://60.167.23.19:1133",
    # "https": "代理 地址"
}
response = requests.get(url, proxies=proxies)
print(response.status_code)
