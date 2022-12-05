# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.


def find_sum(new_list):
    sum = 0
    for i in range(1, len(new_list), 2):
        sum += new_list[i]
    return sum


def print_list(new_list):
    text = '['
    for idx, val in enumerate(new_list):
        if idx != len(new_list)-1:
            text += f'{val}, '
        else:
            text += f'{val}]'
    return text


if __name__ == '__main__':
    initial_list = [3, 2, 5, 10, 1, 9, 2, 6]
    print(f'Исходный список: {print_list(initial_list)}')
    res = find_sum(initial_list)
    print(f'Сумма чисел на нечетных позициях списка равна: {res}')
