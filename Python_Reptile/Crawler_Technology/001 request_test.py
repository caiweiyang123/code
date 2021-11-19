import requests

r = requests.get("http://www.baidu.com")
print(r)
print(r.status_code)
r.encoding = 'utf-8'
print(r.text)
print(r.content.decode())