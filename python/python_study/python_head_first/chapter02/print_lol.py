import sys


def print_lol(the_list, indent=False, level=0, fn=sys.stdout):
    for item in the_list:
        if isinstance(item, list):
            print_lol(item, indent=indent, level=level + 1, fn=fn)
        else:
            if indent:
                for i in range(level):
                    print("\t", end="", file=fn)
            print(item, file=fn)


if __name__ == '__main__':
    names = ['join', 'eric', ['chess', 'idle', ['aaa', 'bbb', 'ccc', ['d', 'e']]], 'micle', ['paline', ['aaa', 'ccc']]]
    print_lol(the_list=names, indent=True, level=4)
