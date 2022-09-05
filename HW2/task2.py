# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

def get_sum(num):
    if num > 10 ** 4:
        return 'The number is too big'
    else:
        sum = 0
        for i in range(1, num + 1):
            sum += i
        return f'The sum is {sum}'

number = int(input('Enter desired number: '))
print(get_sum(number))