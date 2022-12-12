#  Создайте программу для игры с конфетами человек против человека.
# Правила:
# На столе лежит 117 конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.


import random
candys = 117


def player_turn(gamer):
    global candys
    print(f'Ходит {gamer}')
    while True:
        turn = int(input(f'{gamer} cколько конфет хотите взять ?\n: '))
        if 0 <= turn <= 28 and turn <= candys:
            candys -= turn
            print(f'Осталось {candys}')
            break
        else:
            print('Такое количество конфет взять невозможно:')


def computer_turn(gamer):
    global candys
    print(f'Ходит {gamer}')
    while True:
        turn = random.randint(0, 29)
        if turn > candys:
            continue
        else:
            candys -= turn
            print(f'{gamer} взял {turn}\nОсталось {candys}')
            break


def chose_game_mode():
    print("Выберите игровой режим")
    mode = int(input('1: 2 игрока\n2: игра с ИИ\n: '))
    return mode


def rndm_choise(players):
    winner = random.randint(1, 2)
    if winner == 1:
        print(f'Первым ходит {players[0]}')
    else:
        print(f'Первым ходит {players[1]}')
    return winner


def intodution_player(gm):
    if gm == 1:
        first = input('Имя певрого игрока: ')
        second = input('Имя второго игрока: ')
    elif gm == 2:
        first = input('Имя певрого игрока: ')
        second = 'Компьютер'
    return [first, second]


def perfect_game():
    print("Игра запускается")
    game_mode = chose_game_mode()
    players = intodution_player(game_mode)
    order = rndm_choise(players)
    while True:
        if order == 1:
            player_turn(players[0])
            order = 2
            if candys == 0:
                print(f'Winner {players[0]}')
                break
        else:
            if game_mode == 2:
                computer_turn(players[1])
            else:
                player_turn(players[1])
            order = 1
            if candys == 0:
                print(f'Winner {players[1]}')
                break
            else:
                continue


if __name__ == '__main__':
    print("Приветствем в вас в игре достань конфету")
    perfect_game()
