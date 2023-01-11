import requests
from bs4 import BeautifulSoup
import lxml
from telebot import types
import links
url = links.url_adress
text = requests.get(url).content
soup = BeautifulSoup(text, features='xml')


def char_finder(user_input, source=soup):
    return soup.find('CharCode', string=user_input)


def valute_convert(taged_char, source=soup):
    valute_info = taged_char.parent
    value = float((valute_info.find('Value').string).replace(',', '.'))
    nominal = int(valute_info.find('Nominal').string)
    name = valute_info.find("Name").string
    if nominal > 1:
        value = reduction_to_ruble(nominal, value)
    return value, name


def markup_builder_adv(source=soup, columns=7):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                       row_width=columns)
    raw_valutes_list = source.find_all('CharCode')
    valutes = list(map(lambda x: x.string, raw_valutes_list))
    buttons = [types.KeyboardButton(valute) for valute in valutes]
    markup.add(*buttons, 'ВСЕ')
    return markup


def show_all(source=soup):
    all_data = source.find_all('Valute')
    result = ''
    separator = "-"*60
    for valute in all_data:
        val = float((valute.find('Value').string).replace(',', '.'))
        name = valute.find("Name").string
        char_out = valute.find('CharCode').string
        nominal = int(valute.find('Nominal').string)
        if nominal > 1:
            val = reduction_to_ruble(nominal, val)
        result += f'{char_out} - {name}\n Актуальный курс: {val} руб.\n'
        result += f'{separator}\n'
    return result


def reduction_to_ruble(nom, value):
    true_value = value / nom
    return round(true_value, 4)

print(char_finder('USD'))