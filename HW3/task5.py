# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Доп)
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def negafibonacci(num):
    if num == 1 or num == 2:
        return -1
    else:
        return negafibonacci(num + 2) - negafibonacci(num + 1)

fibo_list = []

number = input("Enter number: ")
if int(number) > 0:
    i = int(number) * (-1)
    k = int(number)
else:
    i = int(number)
    k = int(number) * (-1)

j = 0

while i < 0:
    fibo_list.append(negafibonacci(i) * (-1))
    i += 1

fibo_list.append(0)

while j < k:
    j += 1
    fibo_list.append(fibonacci(j))

print(fibo_list)
