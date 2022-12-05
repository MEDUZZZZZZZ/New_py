# Напишите программу, которая будет
#  преобразовывать десятичное число в двоичное.

def take_args():
    arg = int(input("Введите число: "))
    return arg


def formated_binary(num):
    bin_num = bin(num).split('b')[1]
    return bin_num


if __name__ == '__main__':
    try:
        number = take_args()
        binary_num = formated_binary(number)
        print(binary_num)
    except ValueError:
        print('Вы ввели число в неверном формате')
