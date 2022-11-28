# Напишите программу, которая принимает на вход цифру, обозначающую
#  день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def take_args():
    arg = int(input("Введите число обозначающее день недели: "))
    if 0 < arg < 8:
        return arg
    else:
        return take_args()


def is_day_off(day_num):
    if day_num <= 5:
        return "no"
    else:
        return "yes"


if __name__ == '__main__':
    day = take_args()
    print(is_day_off(day))

