# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
# точек в этой четверти (x и y).

quarter = int(input('Enter quarter number: '))

def show_coordinate_range(num):
    while num < 1 or num > 4:
        num = int(input('Incorrect input. Enter the number from 1 to 4: '))
    if num == 1:
        return 'x ∈ (0; +∞); y ∈ (0; +∞)'
    elif num == 2:
        return 'x ∈ (-∞; 0); y ∈ (0; +∞)'
    elif num == 3:
        return 'x ∈ (-∞; 0); y ∈ (-∞; 0)'
    else:
        return 'x ∈ (0; +∞); y ∈ (-∞; 0)'

print(show_coordinate_range(quarter))
