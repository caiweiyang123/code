# 1.什么是继承？
#   继承是一种创建新类的的方式，新建的类可以成为子类或者派生类，父类又可称为基类或超类，子类可以继承父类的属性和功能
#   需要注意的是：python支持多继承。在python中有新式类和经典类之分。
#       1.新式类，python3都是新式类，默认继承object
#       2.经典类，自己是父类，没有继承其他类
#
#
#
#
#   python的多继承的优缺点：
#       优点：子类可以同时遗传多个父类的属性，最大限度地重复用代码
#       缺点：违背了人的思维习惯：继承表达的是一种”什么是什么“的关系
#            代码可读性会变差
#            不建议使用多继承，扩展性变差，如果真的涉及到一个子类不可避免地使用多个父类的属性，应该用Mixins
#
#
# 2.为何要有继承：用来解决代码冗余的问题

# 3.如何实现继承
# 示例一：类出现冗余问题
# class Student:
#     school = 'oldboy'
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def chioce_course(self):
#         print("学生%s选课" % self.name)
#
#
# class Teacher:
#     school = 'oldboy'
#
#     def __init__(self, name, age, sex, salary, level):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.salary = salary
#         self.level = level
#
#     def teach(self):
#         print("老师%s正在给学生打分" % self.name)

# 示范二：基于继承解决类与类之间的冗余问题
class Oldpeoplie:
    school = 'oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Student(Oldpeoplie):
    def chioce_course(self):
        print("学生%s选课" % self.name)


class Teacher(Oldpeoplie):
    school = 'oldboy'

    def __init__(self, name, age, sex, salary, level):
        # Oldpeoplie.__init__(self,name, age, sex)
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.level = level

    def teach(self):
        print("老师%s正在给学生打分" % self.name)


t1 = Teacher("lili", 29, "nan", 5000, 5)
print(t1.__dict__)

# 菱形问题
# class A:
#     def test(self):
#         print("from A")
#
#
# class B(A):
#     def test(self):
#         print("from B")
#
#
# class C(A):
#     def test(self):
#         print("from C")
#
#
# class D(B, C):
#     # def test(self):
#     #     print("from D")
#     pass
#
#
# # d1 = D()
# # d1.test()
# print(D.mro())


# 总结：类相关的属性查找（类名。属性，该类的对象属性），都是参照该类的mro查找
# 多继承要不要用？
# 要用但是要规避几个问题
# 1.继承结构不要太复杂
# 2.要在多继承的背景下满足”什么是什么“的关系


# 多继承的正确打开方式
# mixins机制核心：1.就是在多继承的背景下尽可能提升代码的可读性。2.让多继承满足人的思维习惯-->”什么是什么“
# class Vehicle:
#     pass
#
#
# class FlyableMixin:
#     def fly(self):
#         pass
#
#
# class Minghangfeiji(FlyableMixin, Vehicle):
#     pass
#
#
# class Zhishengfeiji(FlyableMixin, Vehicle):
#     pass
#
#
# class Car(Vehicle):
#     pass
