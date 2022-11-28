# Напишите программу, которая принимает на вход координаты точки (X и Y),
# Причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


def take_cords():
    cord_list = []
    cord_list.append(int(input("Ввдите координату точки x: ")))
    cord_list.append(int(input("Ввдите координату точки y: ")))
    for i in range(len(cord_list)):
        if cord_list[i] == 0:
            print("Координаты должны быть не нулевыми:(")
            return take_cords()
        else:
            return cord_list


def find_quater(cords):
    if cords[0] > 0 and cords[1] > 0:
        return 1
    elif cords[0] < 0 and (cords[1] > 0):
        return 2
    elif cords[0] < 0 and cords[1] < 0:
        return 3
    else:
        return 4


if __name__ == '__main__':
    try:
        my_cords = take_cords()
        print(f'Номер четверти на плоскости: {find_quater(my_cords)}')
    except ValueError:
        print("Вводить координаты точек необходимо в числовом формате")
