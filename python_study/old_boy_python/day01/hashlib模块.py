"""人分三种
    1.理治君子
    2.法治小人
    3.鞭赶揍驴
"""
"""
1.什么是哈希hash
   hash是一类算法：该算法接受传入的内容，经过运算得到一串hash值
   hash值的特点：
    1.只要传入的值一样得到的hash值也是一样的
    2.不能由hash值反解回内容
    3.只要使用的hash算法不变，无论校验的内容多大，得到的hash值长度固定
2.hash的用途
    1.特点2用于密码密文传输与验证
    2.特点1，3用于文件完整性校验
3.如何用
"""
import hashlib

m = hashlib.md5()
m.update("hello".encode("utf-8"))
m.update("world".encode("utf-8"))
res = m.hexdigest()
print(res)

m1 = hashlib.md5('hello'.encode("utf-8"))
m1.update("wor".encode("utf-8"))
m1.update("ld".encode("utf-8"))
res1 = m1.hexdigest()
print(res1)

# 模拟撞库

str1 = "8110adab260f9ec4dc1ecf2645a45d1f"
pwd = ['12312cd','d14d123','d12312d','13d1d3','13dc31']

# 制作密码字典
dict1 = {}
for i in pwd:
    res = hashlib.md5(i.encode('utf-8'))
    dict1[i]=res.hexdigest()

# 模拟撞库得到密码
for k,v in dict1.items():
    if v ==str1:
        print("装酷成功，明文密码是：%s"%k)
        break

# 提升装酷成本，密码加盐
m = hashlib.md5()
m.update("天王".encode("utf-8"))
m.update("13d1d3".encode("utf-8"))
m.update("盖地虎".encode("utf-8"))
res = m.hexdigest()
print(res)