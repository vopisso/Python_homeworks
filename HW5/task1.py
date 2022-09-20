from random import randint as rd


# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все 
# конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

def candy_game():
    candies = 50
    player_1 = 0
    player_2 = 0
    winner = 0
    turn = rd(1, 2)

    if turn == 1:
        print(f'Player_{1} starts\n')
    else:
        print(f'Player_{2} starts\n')

    while candies > 0:
        if turn == 1:
            print(f'\n{candies} candies left\n')
            player_1 = int(input('Player_1, how many candies do you want to take?  '))
            while player_1 > candies:
                player_1 = int(input(f"Only {candies} left, you can't take {player_1} candies. Try again:  "))
            while int(player_1) <= 0 or int(player_1) > 28:
                player_1 = int(input('Did you read the rules? You can take from 1 to 28 sweets. Try again:   '))
                while player_1 > candies:
                    player_1 = int(input(f"Only {candies} left, you can't take {player_1} candies. Try again:   "))
            candies -= player_1
            winner = 1
            print(f'\n{candies} candies left\n')
            if candies == 0:
                break

            player_2 = int(input('Player_2, how many candies do you want to take?  '))
            while player_2 > candies:
                player_2 = int(input(f"Only {candies} left, you can't take {player_2} candies. Try again:  "))
            while int(player_2) <= 0 or int(player_2) > 28:
                player_2 = int(input('Did you read the rules? You can take from 1 to 28 sweets. Try again:   '))
                while player_2 > candies:
                    player_2 = int(input(f"Only {candies} left, you can't take {player_2} candies. Try again:  "))
            candies -= player_2
            winner = 2
            if candies == 0:
                break
        else:
            print(f'\n{candies} candies left\n')
            player_2 = int(input('Player_2, how many candies do you want to take?  '))
            while player_2 > candies:
                player_2 = int(input(f"Only {candies} left, you can't take {player_2} candies. Try again:  "))
            while int(player_2) <= 0 or int(player_1) > 28:
                player_2 = int(input('Did you read the rules? You can take from 1 to 28 sweets. Try again:   '))
                while player_2 > candies:
                    player_2 = int(input(f"Only {candies} left, you can't take {player_2} candies. Try again:   "))
            candies -= player_2
            winner = 2
            print(f'\n{candies} candies left\n')
            if candies == 0:
                break

            player_1 = int(input('Player_1, how many candies do you want to take?  '))
            while player_1 > candies:
                player_1 = int(input(f"Only {candies} left, you can't take {player_1} candies. Try again:  "))
            while int(player_1) <= 0 or int(player_1) > 28:
                player_1 = int(input('Did you read the rules? You can take from 1 to 28 sweets. Try again:   '))
                while player_1 > candies:
                    player_1 = int(input(f"Only {candies} left, you can't take {player_1} candies. Try again:  "))
            candies -= player_1
            winner = 1
            if candies == 0:
                break

    if winner == 1:
        print('\nPlayer_1 win!\n')
    else:
        print('\nPlayer_2 win!\n')


candy_game()
