class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super(B, self).__init__()


class C(A):
    def __init__(self):
        print("C")
        super(C, self).__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super(D, self).__init__()


# 既然重构了init函数，为什么还要用父类方法？
# super 到底执行顺序是怎么样的？

if __name__ == '__main__':
    print(D.__mro__)
    d = D()
