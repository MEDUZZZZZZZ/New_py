import view
import logger
import model


def add_new_user():
    user = view.new_user()
    data = logger.get_data()
    id = model.assign_id(data)
    logger.add_user(user, id)


def search():
    user = view.input_for_search()
    data = logger.get_data()
    search_res = model.search_in_base(data, user)
    view.print_result(search_res)


def edit_user():
    user = view.input_for_search()
    data = logger.get_data()
    search_res = model.search_in_base(data, user)
    view.print_result(search_res)
    if 'Пользователи по запросу не найдены' not in search_res[0] and len(search_res) > 1:
        search_res = model.search_in_base(data, view.clarification())[0]
        new_user = view.new_user()
        edited_user = model.change_user_info(data, search_res, new_user)
        logger.update_data(edited_user)
    elif 'Пользователи по запросу не найдены' not in search_res[0]:
        new_user = view.new_user()
        edited_user = model.change_user_info(data, search_res[0], new_user)
        logger.update_data(edited_user)


def delete_user():
    user = view.input_for_search()
    data = logger.get_data()
    search_res = model.search_in_base(data, user)
    view.print_result(search_res)
    if 'Пользователи по запросу не найдены' not in search_res[0] and len(search_res) > 1:
        search_res = model.search_in_base(data, view.clarification())[0]
        edited_user = model.delete_user(data, search_res)
        logger.update_data(edited_user)
    elif 'Пользователи по запросу не найдены' not in search_res[0]:
        edited_user = model.delete_user(data, search_res[0])
        logger.update_data(edited_user)


def menu():
    flag = True
    while flag:
        cur_mode = view.select_mode()
        if cur_mode == 1:
            add_new_user()
        elif cur_mode == 2:
            search()
        elif cur_mode == 3:
            edit_user()
        elif cur_mode == 4:
            delete_user()
        elif cur_mode == 5:
            view.stop_program()
            flag = False
        else: 
            view.error_notification()


