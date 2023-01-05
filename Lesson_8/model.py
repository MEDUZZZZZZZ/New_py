def assign_id(data):
    if len(data.split("\n")) == 0 or len(data) == 0:
        return 1
    else:
        last_line = data.split('\n')[len(data.split("\n")) - 2]
        print(data)
        print(len(data.split("\n")))
        print(data.split('\n'))
        cur_id = last_line.split(" |-| ")[0]
        return int(cur_id) + 1


def search_in_base(data, request):
    data = data.split("\n")
    notification = 'Пользователи по запросу не найдены :('
    res = []
    switch = True
    for user in data:
        if request in user:
            res.append(user)
            switch = False
    if switch:
        res.append(notification)
    return res


def change_user_info(data, user, new_user):
    data = data.split('\n')
    cur_id = user.split(' |-| ')[0]
    data[data.index(user)] = cur_id + " |-| " + new_user
    return data


def delete_user(data, user):
    data = data.split("\n")
    data.remove(user)
    return data
    