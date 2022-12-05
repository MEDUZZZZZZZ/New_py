# Реализуйте алгоритм перемешивания списка.
from random import randint


def take_args():
    arg = int(input("Введите число: "))
    return arg


def form_list(num):
    required_list = []
    for i in range(-num, num+1):
        required_list.append(i)
    return required_list


def list_shuffle(initial_list):
    storage = 0
    for idx in range(0, len(initial_list)-1):
        flag = True
        storage = initial_list[idx]
        while flag:
            new_idx = randint(0, len(initial_list)-1)
            if new_idx == idx:
                continue
            else:
                flag = False
        initial_list[idx] = initial_list[new_idx]
        initial_list[new_idx] = storage
    return initial_list


def print_list(new_list):
    text = '['
    for idx, val in enumerate(new_list):
        if idx != len(new_list)-1:
            text += f'{val}, '
        else:
            text += f'{val}]'
    return text


if __name__ == '__main__':
    try:
        # list_diap = take_args()
        my_list = form_list(2)
        print(f'Исходный список: \n{print_list(my_list)}')
        result_list = list_shuffle(my_list)
        print(f'Перемешанный список: \n{print_list(result_list)}')
    except ValueError:
        print('Вы ввели число в неверном формате')
