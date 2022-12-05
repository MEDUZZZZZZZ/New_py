# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def extended_mult(list_of_nums):
    res_list = []
    res = 1
    if len(list_of_nums) % 2 == 0:
        for i in range(0, int(len(list_of_nums)/2)):
            res = list_of_nums[i]*list_of_nums[-i-1]
            res_list.append(res)
    else:
        for i in range(0, int(len(list_of_nums)/2)+1):
            res = list_of_nums[i]*list_of_nums[-i-1]
            res_list.append(res)
    return res_list

def print_list(new_list):
    text = '['
    for idx, val in enumerate(new_list):
        if idx != len(new_list)-1:
            text += f'{val}, '
        else:
            text += f'{val}]'
    return text


if __name__ == '__main__':
    my_list = [2, 3, 5, 6]
    result = extended_mult(my_list)
    print(print_list(result))