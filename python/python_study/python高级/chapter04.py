# class Cat:
#     def say(self):
#         print("i am a cat")
#
#
# class Dog:
#     def say(self):
#         print("i am a Dog")
#
#
# class Duck:
#     def say(self):
#         print("i am a Duck")
#
#
# animal_list = [Cat, Dog, Duck]
# for i in animal_list:
#     i().say()

# class Company:
#     def __init__(self, employee_list):
#         self.employee = employee_list
#
#     def __len__(self):
#         return len(self.employee)
#
#
# company = Company(['a', 'b', 'c', 'd'])
# print(hasattr(company, '__len__'))
# from collections.abc import Sized
#
# print(isinstance(company, Sized))

# import abc
#
#
# class CacheBase(metaclass=abc.ABCMeta):
#
#     @abc.abstractmethod
#     def get(self, key):
#         pass
#
#     @abc.abstractmethod
#     def set(self, key, value):
#         pass
#
#
# class RedisCache(CacheBase):
#     pass
#
# redis_cache = RedisCache()

# class A:
#     pass
#
# class B(A):
#     pass
#
# b=B()
# print(isinstance(b,A))
# print(type(b) == A)

# class A:
#     aa = 1
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# a = A(2, 3)
# print(A.aa)
# A.aa = 100
# print(a.x, a.y, a.aa)
# print(A.aa)

class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"


if __name__ == '__main__':
    new_day = Date(2022, 3, 30)
    new_day.tomorrow()
    print(new_day)
