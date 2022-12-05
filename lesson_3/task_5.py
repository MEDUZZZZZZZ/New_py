# Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.(Дополнительно)


def take_args():
    arg = int(input("Введите число: "))
    return arg


def fibonacci(num):
    if num == 1 or num == 2:
        return 1
    elif num > 2:
        return fibonacci(num-1) + fibonacci(num-2)
    elif num == 0:
        return 0
    elif num < 0:
        return fibonacci(num+2) - fibonacci(num + 1)


def fib_list_former(num):
    fib_list = []
    for i in range(-num, num + 1):
        fib_list.append(fibonacci(i))
    return fib_list


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
        number = take_args()
        result = fib_list_former(number)
        print(print_list(result))
    except ValueError:
        print('Вы ввели число в неверном формате')
