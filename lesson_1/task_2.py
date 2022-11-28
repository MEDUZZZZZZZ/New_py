# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат. ¬ - Отрицание
# ⋁ - логическое "Или"
# ⋀ - логическое "И"


def take_args():
    list_of_args = []
    for i in range(1, 4):
        var = input(f'Введите значение {i}: ')
        list_of_args.append(var)
    return list_of_args


def theory_check(my_list):
    first_half = not (my_list[0] or my_list[1] or my_list[2])
    second_half = not my_list[0] and not my_list[1] and not my_list[2]
    res = first_half == second_half
    if res:
        return "Истина"
    else:
        return "Ложь"


if __name__ == '__main__':
    input_list = take_args()
    print(theory_check(input_list))
