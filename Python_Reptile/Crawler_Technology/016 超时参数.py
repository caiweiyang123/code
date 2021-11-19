import requests

url = "http://www.google.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

# 发送请求，获取response
response = requests.get(url, headers=headers, timeout=2)
print(response.status_code)
