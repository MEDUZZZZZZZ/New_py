# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

import math


def input_quater():
    num = int(input("Введите номер четсверти плоскости: "))
    if num < 0 or num > 4:
        print('Введите номер плоскости от 1 до 4')
        return input_quater()
    else:
        return num


def find_range_of_cords(quater):
    pos_inf = math.inf
    neg_inf = -math.inf
    if quater == 1:
        return f'Координаты x ({0},{pos_inf})\nКоординаты y ({0},{pos_inf})'
    elif quater == 2:
        return f'Координаты x ({neg_inf},{0})\nКоординаты y ({0},{pos_inf})'
    elif quater == 3:
        return f'Координаты x ({neg_inf},{0})\nКоординаты y ({neg_inf},{0})'
    else:
        return f'Координаты x ({0},{pos_inf})\nКоординаты y ({neg_inf},{0})'


if __name__ == '__main__':
    try:
        my_quater = input_quater()
        print(find_range_of_cords(my_quater), '\n')
    except ValueError:
        print("Вводить номер четверти необходимо в числовом формате")
