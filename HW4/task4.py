from random import randint as rd

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


def polynomial(k):
    str_res = ''
    fact = 0
    for i in range(k, 0, -1):
        fact = rd(0, 100)
        if fact == 0:
            str_res += ''
        elif fact == 1:
            str_res += str(f'x^{i}+')
        elif i != 1:
            str_res += str(f'{fact}x^{i}+')
        else:
            str_res += str(f'{fact}x')
    fact = rd(0, 100)
    if fact != 0:
        str_res += str(f'+{fact}=0')
    else:
        str_res += str(f'=0')
    return str_res


k = int(input('Enter number: '))
while k <= 0:
    k = int(input('Incorrect input! Enter positive number: '))

with open('F:/GB/Courses/Python1/Homeworks/HW4/task4.txt', 'w') as data:
     data.write(polynomial(k))
