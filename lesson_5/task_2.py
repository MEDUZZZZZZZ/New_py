import random
data = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
dict_positions = {1: [0, 0], 2: [0, 1], 3: [0, 2],
                  4: [1, 0], 5: [1, 1], 6: [1, 2],
                  7: [2, 0], 8: [2, 1], 9: [2, 2]}


def print_filed():
    global data
    rows = len(data)
    columns = len(data[0])
    separator = "-+-".join('-' * columns)
    for i in (range(rows)):
        if 0 < i < rows:
            print(separator)
        result = []
        for j in range(columns):
            item = data[i][j]
            result.append(item)
        print(' | '.join(result))
    print()


def transl_cords(num):
    global dict_positions
    row, col = dict_positions[num]
    return row, col


def players_turn(gamer, symbol):
    global data
    print(f'Ход игрока: {gamer}\n')
    while True:
        pos = int(input("Введите позицию на игровом поле: "))
        i, j = transl_cords(pos)
        if data[i][j] != 'X' and data[i][j] != 'O':
            data[i][j] = symbol
            print()
            break
        else:
            print('Позиция занята\n')
            continue


def computer_turn(symbol):
    global data
    print('Ходит компьютер\n')
    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if data[i][j] != 'X' and data[i][j] != 'O':
            data[i][j] = symbol
            break
        else:
            continue


def chose_game_mode():
    print("Выберите игровой режим\n")
    mode = int(input('1: два игрока\n2: игра с ИИ\n: '))
    return mode


def intodution_player(mode):
    if mode == 1:
        first = input('Имя певрого игрока: ')
        second = input('Имя второго игрока: ')
    elif mode == 2:
        first = input('Имя певрого игрока: ')
        second = 'самый глупый в мире искусственый интеллект'
    return [first, second]


def rndm_choise(players):
    winner = random.randint(1, 2)
    if winner == 1:
        print(f'Первым ходит {players[0]}\n')
    else:
        print(f'Первым ходит {players[1]}\n')
    print('-' * 20)
    return winner


def win_condition(symbol, player):
    global data
    win_list = [[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]],
                [[2, 0], [2, 1], [2, 2]], [[0, 0], [1, 0], [2, 0]],
                [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]],
                [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]
    counter = 0
    flag = True
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'X' or data[i][j] == "O":
                counter += 1
                continue
            else:
                break
    if counter == (len(data) * len(data[0])):
        print("Ничья:(")
        flag = False
        return flag
    for i in range(len(win_list)):
        counter = 0
        for j in range(len(win_list[0])):
            raws, columns = win_list[i][j]
            if data[raws][columns] == symbol:
                counter += 1
            if counter == 3:
                print(f'!====!Победил {player}!====!')
                flag = False
                return flag
            else:
                continue
    return flag 


def ex_zero_game():
    print('Приветствуем вас в игре крестики-нолики')
    game_mode = chose_game_mode()
    players = intodution_player(game_mode)
    print('Печатаем игровое поле')
    print_filed()
    turn_order = rndm_choise(players)
    if turn_order == 1:
        pl_symb = "X"
        ii_symb = "O"
    else:
        pl_symb = "O"
        ii_symb = "X"
    Flag = True
    while Flag:
        if turn_order == 1:
            players_turn(players[0], pl_symb)
            print_filed()
            Flag = win_condition(pl_symb, players[0])
            turn_order = 2
        elif turn_order == 2:
            if game_mode == 2:
                computer_turn(ii_symb)
            else:
                players_turn(players[1], ii_symb)
            print_filed()
            Flag = win_condition(ii_symb, players[1])
            turn_order = 1


if __name__ == '__main__':
    ex_zero_game()
