class StudentManagerController:
    """
        学生管理控制器，负责业务逻辑处理
    """
    # 类变量 ，表示初始编号
    __init_id = 1000

    def __init__(self):
        # 创建学生列表
        self.__stu_list = []

    @property  # 属性化
    def stu_list(self):
        """
            学生列表
        :return: 存储学生对象的列表
        """
        return self.__stu_list

    def add_student(self, stu_info):
        """
            添加一个新学生
        :param stu_info:没有编号的学生信息
        """
        stu_info.id = self.__generate_id()

        self.stu_list.append(stu_info)

    def __generate_id(self):
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self, id):
        """
            按编号移除学生信息
        :param id: 按学生编号移除
        :return: 返回是否移除成功
        """
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True  # 移除成功
        return False  # 移除失败

    def update_student(self, stu_info):
        # 根据stu_info修改其他信息
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        for i in range(len(self.__stu_list)-1):
            for j in range(0,len(self.__stu_list)-i-1):
                if self.__stu_list[j].score < self.__stu_list[j+1].score:
                    self.__stu_list[j],self.__stu_list[j+1] = self.__stu_list[j+1],self.__stu_list[j]