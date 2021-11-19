class Wife():
    def __init__(self,name,age,weight):
        self.name = name
        self.__age= age
        self.__weight = weight

w01 = Wife("茜茜公主",18,95)
print(w01.__dict__)