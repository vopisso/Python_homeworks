def is_rhyme(string):
    list_string = string.split()
    count = 0
    list_temp = []
    vowels = 'ауоыэяюёиеaeiouy'
    for i in list_string:
        for j in i:
            for g in vowels:
                if g in j:
                    count += 1
        if count > 0:
            list_temp.append(count)
        count = 0
    y = list_temp[0]
    res = list(filter(lambda x: x == y, list_temp))
    if len(list_temp) == len(res):
        return True
    else:
        return False

# poem = 'если-я-чешу-в-затылке-не-беда в-голове-моей-опилки-да-да-да'
poem = str(input('Enter poem: '))

if is_rhyme(poem):
    print("Парам пам-пам")
else:
    print("Пам парам")
