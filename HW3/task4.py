# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def dec_to_bin(num):
    result = ''
    while num != 0:
        result += str(num % 2)
        num = num // 2
    return result[::-1]

number = int(input('Enter number: '))

print(dec_to_bin(number))