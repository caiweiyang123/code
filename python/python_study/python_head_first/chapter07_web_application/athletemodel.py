import pickle
from chapter06_packaging_code_and_data.coach_继承 import AthleteList


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp = data.strip().split(',')
        return AthleteList(temp.pop(0), temp.pop(0), temp)
    except IOError as err:
        print('filr error' + str(err))
        return None


def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as err:
        print('file error(put_and_store):' + str(err))
    return all_athletes


def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as err:
        print('file error(get_from_store):' + str(err))
    return all_athletes


if __name__ == '__main__':
    the_files = ['james.txt', 'julie.txt', 'mikey.txt', 'sarch.txt']
    data = put_to_store(the_files)
    print(data)
