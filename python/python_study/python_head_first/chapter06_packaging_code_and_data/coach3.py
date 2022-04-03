def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    mins, secs = time_string.split(splitter)
    return mins + '.' + secs


class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return sorted((set([sanitize(t) for t in self.times])))[0:3]

    def add_time(self, time=None):
        self.times.append(time)

    def add_times(self, times=[]):
        self.times.extend(times)


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp = data.strip().split(',')
        return Athlete(temp.pop(0), temp.pop(0), temp)
    except IOError as err:
        print('filr error' + str(err))
        return None


james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarch = get_coach_data('sarch.txt')
# print(james.name + "'s fastest times are: " + str(james.top3()))
# print(julie.name + "'s fastest times are: " + str(julie.top3()))
# print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
# print(sarch.name + "'s fastest times are: " + str(sarch.top3()))
vera = Athlete('Vera vi')
vera.add_time('1.31')
vera.add_times(['2.22', '1-21', '2:22'])
print(vera.top3())
