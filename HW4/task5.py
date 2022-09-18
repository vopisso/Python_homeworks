# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.


def sum_of_polynomials(path1, path2):
    with open(path1) as file1, open(path2) as file2:
        list1 = list(file1.read().replace('+', ' ').replace('=0', ' ').split())
        list2 = list(file2.read().replace('+', ' ').replace('=0', ' ').split())
        list_result = []
        polyn_1 = []
        polyn_2 = []
        last_x = 0
        for i in list1:
            if 'x' in i or '^' in i:
                polyn_1.append(i.replace('x', '').replace('^', " ").split())
        polyn_1.append(list1[-1].split())
        for j in list2:
            if 'x' in j or '^' in j:
                polyn_2.append(j.replace('x', '').replace('^', " ").split())
        polyn_2.append(list2[-1].split())
        for i in polyn_1:
            for j in polyn_2:
                if len(i) > 1:
                    if i[-1] == j[-1]:
                        list_result.append([int(i[0]) + int(j[0]), int(i[-1])])
                if len(i) == 1:
                    if len(j) == 1 and last_x < 1:
                        list_result.append(int(i[0]) + int(j[0]))
                        last_x += 1
        list_result.append(int(i[0]) + int(j[0]))
        for i in polyn_1:
            for j in polyn_2:
                if len(i) > 1:
                    if i[-1] != j[-1]:
                        list_result.insert(0, [int(i[0]), int(i[-1])])
                        break
                break
            break
        polynomial = []
        for i in range(len(list_result)-2):
            polynomial.extend(list_result[i])
        polynomial.append(list_result[-2])
        polynomial.append(list_result[-1])
        for i in range(len(polynomial)-1):
            if i % 2 == 0:
                polynomial[i] = str(f"{polynomial[i]}x^")
            else:
                polynomial[i] = str(f"{polynomial[i]}+")
        if 'x^' in str(polynomial[-2]):
            polynomial[-2] = str(polynomial[-2]).replace("x^", "x+")
        polynomial = " ".join(map(str, polynomial)).replace(" ", "")
        polynomial += '=0'
    return polynomial

path1 = 'F:/GB/Courses/Python1/Homeworks/HW4/task5_1.txt'
path2 = 'F:/GB/Courses/Python1/Homeworks/HW4/task5_2.txt'
path_result = 'F:/GB/Courses/Python1/Homeworks/HW4/task5_result.txt'

with open(path_result, 'w') as file_result:
    file_result.write(sum_of_polynomials(path1, path2))
    