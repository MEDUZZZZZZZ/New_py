# Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.
from pathlib import Path
from task_4 import polinom_gen, save_pol


def open_and_read(name_of_file):
    file_path = Path('.', 'lesson_4', 'Files', f'{name_of_file}.txt')
    with open(file_path, mode='r', encoding='utf-8') as file:
        polinom = file.read()
    return polinom


def revers_to_dict(polinom: str):
    idxes = polinom.split(' + ')
    polinom_dict = {}
    for i in range(0, len(idxes)):
        data = idxes[i].split('*')
        if len(data) == 1:
            if data[0].isdigit():
                polinom_dict['constant'] = int(data[0])
            elif data[0] == '':
                polinom_dict['constant'] = 0
            else:
                polinom_dict[data[0]] = 1
        else:
            value, key = data
            polinom_dict[key] = int(value)
    return polinom_dict


def polinom_calc(first: dict, second: dict):
    if len(first) > len(second):
        big_dict = first
        small_dict = second
    else:
        big_dict = second
        small_dict = first
    for key, value in big_dict.items():
        if small_dict.get(key):
            value += small_dict[key]
            big_dict[key] = value
        else:
            continue
    for key, value in small_dict.items():
        if not big_dict.get(key):
            big_dict[key] = value
    return big_dict


def get_pol_from_dict(pol_dict: dict):
    pol = ''
    counter = 1
    for key, value in pol_dict.items():
        if key == 'constant':
            pol += f' + {value}'
        else:
            if value == 1:
                if counter != 1:
                    pol += f' + {key}'
                else:
                    pol += f'{key}'
            else:
                if counter != 1:
                    pol += f' + {value}*{key}'
                else: 
                    pol += f'{value}*{key}'
        counter += 1
    return pol


if __name__ == '__main__':
    try:
        degree = int(input('Введите степень полинома:\n'))
        first_pol = polinom_gen(degree)
        second_pol = polinom_gen(degree)
        save_pol(first_pol, 'first_pol')
        save_pol(second_pol, 'second_pol')
        print(f'Первый полином:\n {first_pol}')
        print(f'Второй полином:\n {second_pol}')
        first_input_pol = open_and_read('first_pol')
        second_input_pol = open_and_read('second_pol')
        first_dict = revers_to_dict(first_input_pol)
        second_dict = revers_to_dict(second_input_pol)
        sum_dict = polinom_calc(first_dict, second_dict)
        result = get_pol_from_dict(sum_dict)
        save_pol(result, 'result_pol')
        print(f' Сумма полиномов: \n {result}')
    except ValueError:
        print("Степень введена в неверном формате")
