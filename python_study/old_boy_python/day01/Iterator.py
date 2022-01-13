"""
    迭代器：是指迭代取值的工具，迭代是一个重复的过程，每次重复都是基于上一次的结果而继续的
            单纯的重复不是迭代。
    python 提供了一种不依赖于索引的取值方式，这就是迭代器。
    可迭代的对象：但凡内置有__iter__方法的就是可迭代对象。
    迭代器对象：内置有__next__方法并且内置有__iter__方法的对象
    for 循环的工作原理
        1.d.__iter__()得到一个迭代器对象
        2.迭代器对象.__next__()拿到一个返回值，然后赋值给K
        3.循环反复步骤2，知道抛出异常佛如循环捕捉异常然后结束
    迭代器优缺点总结：
        1.
"""
# 迭代器
with open('a.txt',mode='a+',encoding='utf-8')as f:
    f.write('hahaha')


def dog(name):
    print('dog%s准备吃东西了'%name)
    while True:
        # x拿到的是yeild 接收到的值
        x = yield
        print('dog%s吃了 %s'%(name,x))

g = dog('tom')
# g.__next__()
# # generator
g.send(None)
g.send('一根骨头')

# 三元表达式
# 语法格式：条件成立时要返回的值 if 条件 else 条件不成立时返回的值
x,y =1,2
res = x if x>y else y
