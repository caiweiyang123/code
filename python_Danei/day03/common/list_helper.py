"""
    列表助手模块
"""


class Listhelper:
    """
        列表助手类
    """
    @staticmethod
    def find_all(list_target, func_condition):
        """
            通用的查找某个条件的所有元素方法
        """
        for item in list_target:
            if func_condition(item):
                yield item
