# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков 
# после запятой, сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

def calc_pi(num):
    pi = (1/16**0) * (4/(8 * 0 + 1) - 2/(8 * 0 +4) - 1/(8 * 0 + 5) - 1/(8 * 0 + 6))
    for k in range(1, num):
        pi += (1/16**k) * (4/(8 * k + 1) - 2/(8 * k +4) - 1/(8 * k + 5) - 1/(8 * k + 6))
    return round(pi, num)

NUMBER = int(input('Enter number: '))

while NUMBER < 1 or NUMBER > 15:
    NUMBER = int(input('Incorrect input. Enter number from 1 to 15: '))

print(calc_pi(NUMBER))
