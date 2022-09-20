# Создайте программу для игры в ""Крестики-нолики"".

def print_board(b):
    for i in range(0, len(b)):
        for j in range(0, len(b[i])):
            print(b[i][j], end=' ')
        print()
    print()


def CheckWins(b):
    if (b[0][0] == 'X' and b[0][1] == 'X' and b[0][2] == 'X' or b[0][0] == '0' and b[0][1] == '0' and b[0][2] == '0' or
        b[1][0] == 'X' and b[1][1] == 'X' and b[1][2] == 'X' or b[1][0] == '0' and b[1][1] == '0' and b[1][2] == '0' or
        b[2][0] == 'X' and b[2][1] == 'X' and b[2][2] == 'X' or b[2][0] == '0' and b[2][1] == '0' and b[2][2] == '0' or
        b[0][0] == 'X' and b[1][0] == 'X' and b[2][0] == 'X' or b[0][0] == '0' and b[1][0] == '0' and b[2][0] == '0' or
        b[0][1] == 'X' and b[1][1] == 'X' and b[2][1] == 'X' or b[0][1] == '0' and b[1][1] == '0' and b[2][1] == '0' or
        b[0][2] == 'X' and b[1][2] == 'X' and b[2][2] == 'X' or b[0][2] == '0' and b[1][2] == '0' and b[2][2] == '0' or
        b[0][0] == 'X' and b[1][1] == 'X' and b[2][2] == 'X' or b[0][0] == '0' and b[1][1] == '0' and b[2][2] == '0' or
            b[0][2] == 'X' and b[1][1] == 'X' and b[2][0] == 'X' or b[0][2] == '0' and b[1][1] == '0' and b[2][0] == '0'):
        return True
    else:
        return False


board_size = 3
board = ['*'] * 3
winner = 0
row = 0
column = 0
step = ''
for i in range(board_size):
    board[i] = ['*'] * board_size
print_board(board)
for i in range(9):
    if i % 2 == 0:
        step = "X"
    else:
        step = "0"
    row = int(input('Enter row number: ')) - 1
    column = int(input('Enter column number: ')) - 1
    while int(row) < 0 or int(row) > 2 or int(column) < 0 or int(column) > 2 or board[row][column] != '*':
        print('\nIncorrect input. Try again: \n')
        row = int(input('Enter row number: ')) - 1
        column = int(input('Enter column number: ')) - 1
    board[row][column] = step
    print()
    print_board(board)
    CheckWins(board)
    if CheckWins(board) == True:
        winner = step
        break
if winner == 'X':
    print("-X- WIN!!!")
elif winner == '0':
    print("-0- WIN!!!")
else:
    print("\nStandoff!!!")