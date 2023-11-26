import os

a = r"F:\p1"
b = r"F:\p2"


def copy(a, b):
    filelist = os.listdir(a)
    for file in filelist:
        path = os.path.join(a,file)
        if os.path.isdir(path):
            copy(path,b)
        else:
            with open(path, "rb")as f:
                filename = f.read()
                path1 = os.path.join(b,file)
                with open(path1, "wb")as f1:
                    f1.write(filename)
    else:
        print("复制成功！")

copy(a, b)
