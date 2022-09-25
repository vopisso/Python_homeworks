def print_operation_table(func, rows, columns):
    for i in range(0, rows + 1):
        for j in range(0, columns + 1):
            print(func(i, j), end='\t')
        print('\n')

operation = ['+', '*', '**']
action = input('Enter desired operation: +, *, ** -> ')

while action not in operation:
    action = input('Incorrect input! Enter desired operation: +, *, ** -> ')

num_rows = int(input('Enter desired number of rows -> '))
num_columns = int(input('Enter desired number of columns -> '))

if action == '*':
    print_operation_table(lambda x, y: x * y, num_rows, num_columns)
elif action == '+':
    print_operation_table(lambda x, y: x + y, num_rows, num_columns)
elif action == '**':
    print_operation_table(lambda x, y: x ** y, num_rows, num_columns)