import bisect
import os.path
import sys

traveler_ids = [("usa", "31195855"), ("bra", "ce342567"), ("esp", "205856")]
for i in traveler_ids:
    print("%s/%s" % i)

# divmod()返回一个包含商和余数的元组
print(divmod(20, 8))  # (2, 4)
t = (20, 8)
print(divmod(*t))

_, filename = os.path.split("d:\code\code\python\python_study\demo01.py")
print(filename)
print(_)

board = [['_'] * 3 for i in range(3)]
print(board)
board[1][1] = "X"
print(board)
t = (1, 2, [30, 40])
# t[2]+=[50,60]
print(t)

fruits = ["grape", "raspberry", "apple", "banana"]

print(sorted(fruits))
print(fruits)

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 29, 30, 31]
ROW_FMT = "{0:2d} @ {1:2d}   {2} {0:<2d}"


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * "  |"
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':
    if sys.argv[-1] == "left":
        bisect_fn = bisect.insort_left
    else:
        bisect_fn = bisect.bisect
    print("DEMO:", bisect_fn.__name__)
    print("haystack->", " ".join("%2d" % i for i in HAYSTACK))
    demo(bisect_fn)
