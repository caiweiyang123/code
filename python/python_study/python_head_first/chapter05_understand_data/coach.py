def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    mins, secs = time_string.split(splitter)
    return mins + '.' + secs


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return data.strip().split(',')
    except IOError as err:
        print('filr error' + str(err))
        return None


james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarch = get_coach_data('sarch.txt')

james = sorted(set([sanitize(item) for item in james]))
julie = sorted(set([sanitize(item) for item in julie]))
mikey = sorted(set([sanitize(item) for item in mikey]))
sarch = sorted(set([sanitize(item) for item in sarch]))

print(james[0:3])
print(julie[0:3])
print(mikey[0:3])
print(sarch[0:3])
