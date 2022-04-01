from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __getattr__(self, item):
        return "not found attr"

    def __getattribute__(self, item):
        return "aaaa"

if __name__ == '__main__':
    user = User("cai", date(year=1987, month=1, day=1))
    print(user.name)