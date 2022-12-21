# Задайте список из n чисел последовательности
#  (1+1/n)^n и выведите на экран их сумму.


def take_args():
    arg = int(input("Введите число: "))
    return arg


def universal_comprehension(func, number):
    return [func(i) for i in range(1, number + 1)]


if __name__ == '__main__':
    try:
        number = take_args()
        result = universal_comprehension(lambda x: (1 + 1 / x)**x, number)
    except ValueError:
        print('Вы ввели число в неверном формате')
