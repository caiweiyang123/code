# import requests
#
# url = "http://suggest.taobao.com/sug"
# data ={"code": "utf-8", "q": "泡面"}
# rr = requests.get(url=url, params=data)
#
# if rr.status_code == 200:
#     assert len(rr.json()["result"]) == 10
#     assert rr.json()["result"][-1][0] == "泡面神器"
#     print("响应成功")
# else:
#     print("响应失败")


# import requests
#
# url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php"
# data = {"query": "210.51.167.169" , "resource_id" : "6006"}
# qq = requests.get(url=url, params=data)
# print(qq.json())
# if qq.status_code == 200:
#     assert qq.json()["data"][0]["location"] == "北京市北京市 联通"
#     print("响应成功")
# else:
#     print("响应失败")


import requests
import assertpy


url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php"
ip = ["202.102.199.68", "114.106.183.223"]

for i in range(len(ip)):
    params = {'query': ip[i], 'resource_id': 6006}
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        assertpy.assert_that(response.json()["status"]).is_equal_to("0")
        assertpy.assert_that(response.json()['data'][0]['origip']).is_equal_to(ip[i])
        assertpy.assert_that(response.json()['data'][0]['location']).does_not_contain('上海') # 断言响应体不包含上海
        print('响应成功')
    else:
        print('响应失败')

    print(response.json())
