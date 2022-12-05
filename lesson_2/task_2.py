# Напишите программу, которая принимает на вход число N
#  и выдает набор произведений чисел от 1 до N.


def take_args():
    arg = int(input("Введите число: "))
    return arg


def form_list_of_mult(num):
    res = 1
    list_of_mults = []
    for i in range(1, num+1):
        res *= i
        list_of_mults.append(res)
    return list_of_mults


def print_list(my_list):
    text = f'Набор произведений чисел от 1 до {len(my_list)}:\n['
    for idx, val in enumerate(my_list):
        if idx != len(my_list)-1:
            text += f'{val}, '
        else:
            text += f'{val}]'
    return text


if __name__ == '__main__':
    try:
        number = take_args()
        new_list = form_list_of_mult(number)
        print(print_list(new_list))
    except ValueError:
        print('Вы ввели число в неверном формате')
