# Задайте последовательность чисел.
# Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint


def generate_list():
    res = []
    for i in range(12):
        res.append(randint(1, 5))
    return res


if __name__ == '__main__':
    my_list = generate_list()
    print(f'Исходный список: \n{my_list}')
    my_list = list(set(my_list))
    print(f'Список неповторяющихся элементов:\n{my_list}')
