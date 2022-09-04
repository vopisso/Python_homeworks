# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def is_weekend(number):
    if 1 <= number <= 5:
        return(f'{number} -> no')    
    elif number == 6 or number == 7:
        return(f'{number} -> yes')
    else:
        return(f'{number} - is incorrect input. Enter number from 1 to 7')

day = int(input('Enter the number of the day of the week: '))

print(is_weekend(day))
