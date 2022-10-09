# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи.

NUMBER = int(input('Enter number: '))

def find_n_fibonacci(num):
    while num < 0:
        num = int(input('Incorrect input! '))
    fib1 = 0
    fib2 = 1
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        for i in range(1, num):
            fib_temp = fib2 + fib1
            fib1 = fib2
            fib2 = fib_temp
    return fib_temp

print(find_n_fibonacci(NUMBER))
