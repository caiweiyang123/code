import requests

url = "http://www.renren.com/976604051/newsfeed/photo"

headers = {
    'User_Agent': '',
    'Cookie': ''
}

response = requests.get(url, headers=headers)
print(response.status_code)

with open('rr.html', 'w', encoding='utf-8')as f:
    f.write(response.content.decode())
