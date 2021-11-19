# try:
#     with open(r"F:\p1\b1.txt","r")as wstream:
#         file = wstream.read()
# except Exception as err:
#     print("出错啦！",err)

"""
try:
    pass
except:
    pass
finally:
    pass
"""
def func():
    stream = None
    try:
        stream = open(r"F:\p1\bb.txt")
        con = stream.read()
        print(con)
    except Exception as err:
        print(err)
    finally:
        print("-------finally--------")
        if stream:
            stream.close()

func()