# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.

def find_difference(initial_list):
    min = round(initial_list[0] % 1, 2)
    max = min
    for idx, val in enumerate(initial_list):
        fraction = round(val % 1, 2)
        if fraction == 0:
            continue
        elif min > fraction:
            min = fraction
        elif max < fraction:
            max = fraction
    res = max - min
    return res


if __name__ == '__main__':
    my_list = [1.1, 1.2, 3.1, 5, 10.01]
    result = find_difference(my_list)
    print(f'Разница между наибольшей и наименьшей дробной частью: {result}')
