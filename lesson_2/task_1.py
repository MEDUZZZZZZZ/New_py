# Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр.


def take_args():
    arg = input("Введите вещественное число: ")
    return arg


def sum_of_nums(num):
    sum = 0
    for element in num:
        if element != "," and element != ".":
            sum += int(element)
        else:
            continue
    return sum


if __name__ == '__main__':
    try:
        number = take_args()
        result = sum_of_nums(number)
        print(f'Сумма цифр числа {number} равна {result}')
    except ValueError:
        print('Вы ввели число в неверном формате')
