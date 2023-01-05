import csv


def add_user(new_user, id):
    user = f"{id} |-| " + new_user
    user_csv = [user.split(' |-| ')]
    try:
        with open("data_base.csv", mode='a', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(user_csv)
        with open("data_base.txt", mode='a', encoding="utf-8") as txt_file:
            txt_file.write(f'{user}\n')
    except FileNotFoundError:
        with open("data_base.csv", mode='w+', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(user_csv)
        with open("data_base.txt", mode='w+', encoding="utf-8") as txt_file:
            txt_file.write(f'{user}')


def get_data():
    try:
        with open("data_base.txt", mode='r', encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        with open("data_base.txt", mode='w+', encoding="utf-8") as file:
            return ''

    
    
    #         reader = csv.reader(file)
    #         for row in reader:
    #             data += "\n".join(row)
    #     return data
    # except FileNotFoundError:
    #     with open("data_base.csv", mode='w+', encoding="utf-8") as file:
    #         return ''

def update_data(updated_data):
    new_data = [i.split(" |-| ") for i in updated_data]
    with open("data_base.csv", mode='w', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(new_data)
    with open("data_base.txt", mode='w+', encoding="utf-8") as txt_file:
        txt_file.write("\n".join(updated_data))

        