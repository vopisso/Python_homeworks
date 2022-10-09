# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.


def find_minimal_divider(num):
    if num < 1 or num > 10 ** 6:
        return 'Incorrect input'
    else:
        i = 1
        while i <= num:
            i += 1
            if num % i == 0:
                return f'The minimal divider is {i}'

NUMBER = int(input('Enter number: '))
print(find_minimal_divider(NUMBER))
