import requests

url = "http://www.renren.com/976604051/newsfeed/photo"

headers = {
    'User_Agent': '',
}
cookie = ''
cookies = {}
cookie_list = cookie.split(': ')
for i in cookie_list:
    cookies[i.split('=')[0]] = i.split('=')[1]

response = requests.get(url, headers=headers, cookies=cookies)
print(response.status_code)

with open('rr.html', 'w', encoding='utf-8')as f:
    f.write(response.content.decode())
