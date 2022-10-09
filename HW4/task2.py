# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def dividers_list(num):
   i = 2
   list1 = []
   while i * i <= num:
       while num % i == 0:
           list1.append(i)
           num = num / i
       i = i + 1
   if num > 1:
       list1.append(num)
   return list1

NUMBER = int(input('Enter integer number: '))
while NUMBER < 0:
    NUMBER = int(input('Incorrect input. Enter positive number: '))
    
print(dividers_list(NUMBER))