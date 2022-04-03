def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    mins, secs = time_string.split(splitter)
    return mins + '.' + secs


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp = data.strip().split(',')
        return AthleteList(temp.pop(0), temp.pop(0), temp)
    except IOError as err:
        print('filr error' + str(err))
        return None


if __name__ == '__main__':
    # vera = AthleteList('Vera vi')
    # vera.append('1.31')
    # vera.extend(['2.22', '1-21', '2:22'])
    # print(vera.top3())
    # print(vera.name)
    james = get_coach_data('james.txt')
    julie = get_coach_data('julie.txt')
    mikey = get_coach_data('mikey.txt')
    sarch = get_coach_data('sarch.txt')
    print(james.name + "'s fastest times are: " + str(james.top3()))
    print(julie.name + "'s fastest times are: " + str(julie.top3()))
    print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
    print(sarch.name + "'s fastest times are: " + str(sarch.top3()))
