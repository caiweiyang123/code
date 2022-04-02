import os

try:
    data = open('sketch.txt')
    for item in data:
        try:
            role, line_speak = item.split(':', 1)
            print(role, end='')
            print(' said:', end='')
            print(line_speak, end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print('the data file is missing!')

# if os.path.exists('sketch.txt'):
#     data = open('sketch.txt')
#     for item in data:
#         try:
#             role, line_speak = item.split(':', 1)
#             print(role, end='')
#             print(' said:', end='')
#             print(line_speak, end='')
#         except:
#             pass
#     data.close()
# else:
#     print('the data file is missing!')
