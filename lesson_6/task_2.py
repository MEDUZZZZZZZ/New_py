# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
from random import randint
from functools import reduce


def init_list(number):
    return [randint(1, 10) for i in range(1, number + 1)]


if __name__ == '__main__':
    lst = init_list(4)
    print(lst)
    result = reduce(lambda x, y: x + y, [lst[i] for i in range(0, len(lst)) if i % 2])
    print(f'Сумма элементов на нечетной позиции: {result}')
