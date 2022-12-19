from random import randint
from pathlib import Path


def polinom_gen(k):
    pol = ''
    for i in range(k, -1, -1):
        number = randint(0, 100)
        if number == 0:
            continue
        elif number == 1:
            if i == 0:
                pol += f'{number}'
            elif i == 1:
                pol += 'x + '
            else:
                pol += f'x^{i} + '
        else:
            if i == 0:
                pol += f'{number}'
            elif i == 1:
                pol += f'{number}^x + '
            else:
                pol += f'{number}*x^{i} + ' 
    return pol


def save_pol(polinom, name_of_file='new_pol'):
    file_plath = Path('.', 'lesson_4', 'Files', f'{name_of_file}.txt')
    print(file_plath)
    with open(file_plath, mode='w+', encoding='utf-8') as res_file:
        res_file.write(polinom)
    return 'Запись завершена'


if __name__ == '__main__':
    try:
        degree = int(input('введите степень полинома: '))
        my_polinom = polinom_gen(degree)
        print(f'Получившийся полином:\n {my_polinom}')
        print(save_pol(my_polinom))
    except ValueError:
        print('Степень введена в неверном формате')

# '../', 'Files', 5

