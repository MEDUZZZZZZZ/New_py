# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.


def factorization(number):
    result = []
    start_simple = 2
    while start_simple <= number:
        if number % start_simple == 0:
            if start_simple not in result:
                result.append(start_simple)
            number //= start_simple
        else:
            start_simple += 1
    return result


if __name__ == '__main__':
    try:
        num = int(input('Введите число, которое необходимо разложить: '))
        res = factorization(num)
        print(res)
    except ValueError:
        print('Число введено в неверном формате')