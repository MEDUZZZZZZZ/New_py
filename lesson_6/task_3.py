# Напишите программу, которая принимает на вход число N
#  и выдает набор произведений чисел от 1 до N.


def take_args():
    arg = int(input("Введите число: "))
    return arg

if __name__ == '__main__':
    try:
        number = take_args()
        tmp_func = lambda x: 1 if x == 1 else x * tmp_func(x - 1)
        result = [tmp_func(i) for i in range(1, number + 1)]
        print(result)
    except ValueError:
        print('Вы ввели число в неверном формате')
