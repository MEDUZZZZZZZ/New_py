# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math


def take_cords():
    cord_list = []
    cord_list.append(int(input("Ввдите координату x: ")))
    cord_list.append(int(input("Ввдите координату y: ")))
    for i in range(len(cord_list)):
        if cord_list[i] == 0:
            print("Координаты должны быть не нулевыми:(")
            return take_cords()
        else:
            return cord_list


def find_distance(point_1, point_2):
    first_sqr = (point_2[0] - point_1[0])**2
    second_sqr = (point_2[1] - point_1[1])**2
    result = math.sqrt(first_sqr + second_sqr)
    return result


if __name__ == '__main__':
    try:
        print("Ввелите координаты точки 1: ")
        point_1_cords = take_cords()
        print("Ввелите координаты точки 2: ")
        point_2_cords = take_cords()
        res = round(find_distance(point_1_cords, point_2_cords), 2)
        print(f'Расстояние между заданными точками равно {res}')
    except ValueError:
        print("Вводить координаты точек необходимо в числовом формате")
