import requests

# GET请求
# 从服务器上获取数据
#     get是把参数数据队列加到提交表单的action 属性所指的URL中
#     值和表单内各个字段一一对应
#     在URL中可以看到
# 服务器端用Request。QueryString获取变量的值
# get传送的数据量小，不能大于2KB
# get安全性非常低

# POST请求
# 向服务器传送数据
#     post是通过HTTP post机制
#     将表单内各个字段与其内容放置在HTML header内一起传送到action属性所指的url地址
#     用户看不到这个过程
# 服务器端用Request.Form获取提交的数据
# post传送的数据量较大，一般被默认为不受限制
# post安全性较高
#     如果没有加密，他们安全级别都是一样的。
#     随便一个监听器都可以把所有的数据监听到。

