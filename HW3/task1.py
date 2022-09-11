# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from function import create_list

def sum_on_odd_position(list):
    sum = 0
    for i in range(len(list)):
        if i % 2 != 0:
            sum += list[i]
    return f'The sum of elements on odd positions is {sum}'

print(sum_on_odd_position(create_list()))
