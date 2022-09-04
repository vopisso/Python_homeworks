# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

x = int(input('Enter X: '))
y = int(input('Enter Y: '))
z = int(input('Enter Z: '))

def is_true(x, y, z):
    if not (x or y or z) == (not x) and (not y) and (not z):
        return 'True'
    else:
        return 'False'

print(is_true(x, y, z))