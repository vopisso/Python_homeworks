# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной.

num = int(input('Enter number of coins -> '))

def cout_coins(coin_num):
    count = 0
    for i in range(coin_num):
        side = int(input('Enter side: heads - 1, tails - 0 -> '))
        if side < 0 or side > 1:
            return 'Incorrect input'
        elif side == 1:
            count += 1
    if count < coin_num / 2:
        return f'at least {count} coins needs to be turned'
    else:
        return f'at least {coin_num - count} coins needs to be turned'

print(cout_coins(num))