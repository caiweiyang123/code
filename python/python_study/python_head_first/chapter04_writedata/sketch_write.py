from chapter02 import print_lol

man = []
other = []
try:
    data = open('sketch.txt')
    for item in data:
        try:
            role, line_speak = item.split(':', 1)
            line_speak = line_speak.strip()
            if role == 'Man':
                man.append(line_speak)
            elif role == 'Other Man':
                other.append(line_speak)
        except ValueError:
            pass
    data.close()
except IOError:
    print('the data file is missing!')

try:
    with open('man_data.txt', 'w') as man_data:
        print_lol.print_lol(man, indent=True, fn=man_data)
    with open('other_data.txt', 'w') as other_data:
        print_lol.print_lol(other, indent=True, fn=other_data)
except Exception as e:
    print(e)

# man = []
# other = []
# try:
#     data = open('sketch.txt')
#     for item in data:
#         try:
#             role, line_speak = item.split(':', 1)
#             line_speak = line_speak.strip()
#             if role == 'Man':
#                 man.append(line_speak)
#             elif role == 'Other Man':
#                 other.append(line_speak)
#         except ValueError:
#             pass
#     data.close()
# except IOError:
#     print('the data file is missing!')
# try:
#     man_data = open('man_data.txt', 'w')
#     other_data = open('other_data.txt', 'w')
#     print(man, file=man_data)
#     print(other_data, file=other_data)
# except Exception as e:
#     print(e)
# finally:
#     man_data.close()
#     other_data.close()
