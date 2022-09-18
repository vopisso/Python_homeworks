# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.


def unique_sequence(list1):
    list_res = []
    for i in range(len(list1)):
        if list1[i].isdigit():
            list_res.append(int(list1[i]))
    list_res = list(set(list_res))
    return list_res

sequense = input('Enter numbers serated by space: ').split()

print(unique_sequence(sequense))