

def input_for_search():
    return input("Введите запрос: ")


def select_mode():
    return int(input("Выберите режим [1 - добавление]\n[2 - поиск]\
                \n[3 - изменение]\n[4 - удаление]\n [5 - остановить программу]: "))


def new_user():
    name = input("Укажите имя: ")
    nik_name = input("Укажите корпоративный никнейм: ")
    work = input("Укажите занимаемый пост: ")
    phone_number = input("Укажте номер мобильного:")
    e_mail = input("Укажите адрес почты:")
    return f'{name} |-| {nik_name} |-| {work} |-| {phone_number} |-| {e_mail}'


def print_result(result):
    print("Результат поиска по важему запросу: ")
    for i in result:
        print(i)


def clarification():
    return input('Укажите необходимый идентификатор: ')


def error_notification():
    print('Введено неправильное значение')


def stop_program():
    print("Завершение работы программы ...")

