from random import randint as rd

# a) Добавьте игру против бота

def candy_game_with_bot():
    candies = 201
    player_1 = 0
    bot = 0
    winner = 0
    turn = rd(1, 2)

    if turn == 1:
        print(f'Player_{1} starts\n')
    else:
        print(f'Bot starts\n')

    while candies > 0:
        if turn == 1:
            print(f'\n{candies} candies left\n')
            player_1 = int(input('Player_1, how many candies do you want to take?  '))
            while player_1 > candies:
                player_1 = int(input(f"Only {candies} left, you can't take {player_1} candies. Try again:  "))
            while int(player_1) <=0 or int(player_1) > 28:
                player_1 = int(input('Did you read the rules? You can take from 1 to 28 sweets. Try again:   '))
                while player_1 > candies:
                    player_1 = int(input(f"Only {candies} left, you can't take {player_1} candies. Try again:   "))
            candies -= player_1
            winner = 1
            print(f'\n{candies} candies left\n')
            if candies == 0:
                break

            if candies > 28:
                bot = rd(1, 29)
                print(f'Bot takes {bot} candies')
            else:
                bot = rd(1, candies)
                print(f'Bot takes {bot} candies')
            candies -= bot
            winner = 2
            if candies == 0:
                break
        else:
            print(f'\n{candies} candies left\n')
            if candies > 28:
                bot = rd(1, 29)
                print(f'Bot takes {bot} candies')
            else:
                bot = rd(1, candies)
                print(f'Bot takes {bot} candies')
            candies -= bot
            winner = 2
            print(f'\n{candies} candies left\n')
            if candies == 0:
                break
            player_1 = int(input('Player_1, how many candies do you want to take?  '))
            while player_1 > candies:
                player_1 = int(input(f"Only {candies} left, you can't take {player_1} candies. Try again:  "))
            while int(player_1) <=0 or int(player_1) > 28:
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
        print('\nBot win!\n')

candy_game_with_bot()
