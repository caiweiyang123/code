import yaml

"""
问题1：解析的yaml文件必须是utf-8的格式，可以用notepad++来查看格式
"""


def read_yaml():
    """
    读取yaml文件
    :return:
    """
    with open('get_new.yaml', encoding='UTF-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


if __name__ == '__main__':
    print(read_yaml())
