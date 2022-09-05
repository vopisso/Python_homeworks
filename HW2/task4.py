# Петя впервые пришел на урок физкультуры в новой школе. Перед началом урока ученики 
# выстраиваются по росту, в порядке невозрастания. Напишите программу, которая определит 
# на какое место в шеренге Пете нужно встать, чтобы не нарушить традицию, если заранее 
# известен рост каждого ученика и эти данные уже расположены по невозрастанию (то есть 
# каждое следующее число не больше предыдущего). Если в классе есть несколько учеников 
# с таким же ростом, как у Пети, то программа должна расположить его после них.


def get_place_in_line(num, height):
    list_of_height = list()
    for i in range(num):
        heigth_temp = int(input('Enter height: '))
        if heigth_temp < 50 or heigth_temp > 200:
            return 'Incorrect input'
            exit()
        else:
            list_of_height.append(heigth_temp)
    list_of_height.sort()
    place = 0
    for i in range(len(list_of_height)):
        if  height >= list_of_height[i]:
            place += 1
    return f'Your place in line is {place + 1}'

pupils_number = int(input('Enter the number of pupils: '))
if pupils_number < 0 or pupils_number > 100:
    print('Incorrect input')
    exit()
your_height = int(input('Enter your height: '))
if your_height < 50 or your_height > 200:
    print('Incorrect input')
    exit()

print(get_place_in_line(pupils_number, your_height))


