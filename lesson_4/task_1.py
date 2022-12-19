# 1'. Вычислить число Пи c заданной точностью d
from math import pi


def take_arg():
    accuracy = input("Введите необходимою точность. Например: 0.01\n: ")
    if accuracy.find(","):
        accuracy = accuracy.replace(",", ".")
    res = len(accuracy.split('.')[1])
    return res


def round_num(new_accuraccy, num=pi):
    rounded_num = f'{num:0.{new_accuraccy}f}'
    return f'Значение числа pi: {rounded_num}'


if __name__ == '__main__':
    try:
        acc = take_arg()
        print(round_num(acc))
    except ValueError:
        print('Вы ввели число в неверном формате')
