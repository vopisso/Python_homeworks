
# dic = {'id': ('First name', 'Last name', 'Phone', 'description')}
# dic[0] = ('------------', '---------', '-----', '-----------')

def add_record(dic):
    list1 = input('-> ').split()
    dic1 = {int(list(dic.keys())[-1]) + 1: tuple(list1)}
    dic.update(dic1)
    return dic

def print_phonebook(dic):
    for key, value in dic.items():
        print(f'{key}: {value}')