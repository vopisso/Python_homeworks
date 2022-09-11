# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый 
# и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from function import create_list

def mult_pair(list):
    j = len(list) - 1
    rez = []
    for i in range(j - 1):
        rez.append(list[i] * list[j])
        j -= 1
    return rez

print(mult_pair(create_list()))
