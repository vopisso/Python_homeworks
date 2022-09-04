# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между 
# ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(int(distance * 100) / 100)  # обрезаю знаки после запятой без округления