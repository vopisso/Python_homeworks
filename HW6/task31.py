def same_by(characteristic, objects):
    list1 = []
    for i in objects:
        if characteristic(i) == 0:
            list1.append(True)
        else:
            list1.append(False)
    y = list1[0]
    res = list(filter(lambda x: x == y, list1))
    if len(list1) == len(res):
        return True
    else:
        return False


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')