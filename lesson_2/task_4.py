# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)

from pathlib import Path


def take_args():
    arg = int(input("Введите число: "))
    return arg


def form_list(num):
    required_list = []
    for i in range(-num, num+1):
        required_list.append(i)
    return required_list


def read_and_mult(path_file, nums_list):
    list_of_idx = []
    res = 1
    file = open(path_file, mode='r', encoding='utf-8')
    for line in file:
        list_of_idx.append(int(line))
    file.close()
    for i in list_of_idx:
        res *= nums_list[i]
    return res


if __name__ == '__main__':
    path_of_file = Path('Files', 'file.txt')
    try:
        list_dia = take_args()
        initial_list = form_list(list_dia)
        result = read_and_mult(path_of_file, initial_list)
        print(result)
    except ValueError:
        print('Вы ввели число в неверном формате')
