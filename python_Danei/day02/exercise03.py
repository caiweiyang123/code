class Graphics_manager():
    """
        管理所有图形
    """

    def get_area(self, *args):
        pass


class Circular(Graphics_manager):
    def get_area(self, r):
        pi = 3.14
        area = pi * r ** 2
        print(f"圆的面积是：{area}")


class Rectangle(Graphics_manager):
    def get_area(self, c, k):
        area = c * k
        print(f"矩形的面积是：{area}")


class Triangle(Graphics_manager):
    def get_area(self, d, h):
        area = (d * h) / 2
        print(f"三角形的面积是：{area}")

