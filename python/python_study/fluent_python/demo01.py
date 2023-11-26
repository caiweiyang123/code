import os.path

traveler_ids = [("usa", "31195855"), ("bra", "ce342567"), ("esp", "205856")]
for i in traveler_ids:
    print("%s/%s" % i)

# divmod()返回一个包含商和余数的元组
print(divmod(20, 8))  # (2, 4)
t = (20,8)
print(divmod(*t))

_,filename = os.path.split("d:\code\code\python\python_study\demo01.py")
print(filename)
print(_)

board = [['_']*3 for i in range(3)]
print(board)
board[1][1] = "X"
print(board)