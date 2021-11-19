import requests

headers = {
    'User_Agent': ''
}

session = requests.session()

data = {
    'name': '',
    'password': ''
}
r = session.post("登录url", headers=headers, data=data)

response = session.get("首页URL", headers=headers)

with open('rr.html', 'w', encoding='utf-8')as f:
    f.write(response.content.decode())
