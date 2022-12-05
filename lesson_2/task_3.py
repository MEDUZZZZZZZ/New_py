# Задайте список из n чисел последовательности
#  (1+1/n)^n и выведите на экран их сумму.


def take_args():
    arg = int(input("Введите число: "))
    return arg


def form_list(lenght):
    subsequence_list = []
    for i in range(1, lenght+1):
        res = (1 + 1 / i)**i
        subsequence_list.append(res)
    return subsequence_list


def print_list(my_list):
    text = f'Набор чисел заданной последовательности от 1 до {len(my_list)}:\n['
    for idx, val in enumerate(my_list):
        if idx != len(my_list)-1:
            text += f'{val}, '
        else:
            text += f'{val}]'
    return text


if __name__ == '__main__':
    try:
        number = take_args()
        new_list = form_list(number)
        print(print_list(new_list))
    except ValueError:
        print('Вы ввели число в неверном формате')
