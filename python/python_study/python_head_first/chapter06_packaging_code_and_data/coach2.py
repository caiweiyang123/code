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
        temp = data.strip().split(',')
        return {'name': temp.pop(0),
                'Dob': temp.pop(0),
                'times': str(sorted(set([sanitize(t) for t in temp]))[0:3])}
    except IOError as err:
        print('filr error' + str(err))
        return None

james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarch = get_coach_data('sarch.txt')
print(james.get('name') + "'s fastest times are: " + james.get('times'))
print(julie.get('name') + "'s fastest times are: " + julie.get('times'))  
print(mikey.get('name') + "'s fastest times are: " + mikey.get('times'))
print(sarch.get('name') + "'s fastest times are: " + sarch.get('times'))
