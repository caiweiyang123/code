class GraphicManager:
    """
        图形管理器
    """
    def __init__(self):
        """
            构造一个列表保存图形
        """
        self.__graphic = []

    def add_graphic(self, graphic):
        """
                添加图形到保存图形的列表中
        :param graphic: 获取图形
        """
        if isinstance(graphic, Graphic):
            self.__graphic.append(graphic)
        else:
            raise ValueError()

    def get_total_area(self):
        """
            计算所有图形的总面积
        :return:总面积
        """
        total_area = 0
        for item in self.__graphic:
            total_area += item.calculate_area()
        return total_area


class Graphic():
    def calculate_area(self):
        raise NotImplemented


class Circle(Graphic):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius ** 2 * 3.14


class Rectanlge(Graphic):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.width * self.length
