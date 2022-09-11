def create_list():
    numbers = []
    n = ''
    flag = True
    while flag:
        n = input('Enter number (press "x" for exit): ')
        if n.lower() == 'x' or n.lower() == 'ч':
            flag = False
        else:
            numbers.append(int(n))
    return numbers