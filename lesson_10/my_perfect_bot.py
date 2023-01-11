import telebot
from telebot import types
import conventer_model as converter
from random import randint, choice
from links import bot_win, user_win

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)
mode = ''
nikname = ''
candys = 117


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я самый лучший на свете бот!
Умею играть в игры и предоставляю актуальный курс валют.
Для получения списка команд пропишите /help
""")


@bot.message_handler(commands=["help"])
def commands_helper(message):
    bot.send_message(message.chat.id, """\
Список доступных команд:
Сыграть в игру - /game
Посмотреть актуальный курс валют - /money
Получить список доступных команд - /help""")


@bot.message_handler(commands=["money"])
def money_welcome(message):
    markup = converter.markup_builder_adv()
    msg = bot.reply_to(message,
                       "Введите буквенный код валюты",
                       reply_markup=markup)
    bot.register_next_step_handler(msg, show_price)


def show_price(message):
    remove = types.ReplyKeyboardRemove()
    char = (message.text).upper()
    if char == 'ВСЕ':
        reply = converter.show_all()
        msg = bot.reply_to(message, reply)
    else:
        finder = converter.char_finder(char)
        if finder is None:
            msg = bot.reply_to(message, 'Неверный код валюты')
            bot.register_next_step_handler(msg, money_welcome)
        else:
            val, name = converter.valute_convert(finder)
            msg = bot.reply_to(message,
                               f"{char} - {name}\nАктуальный курс: {val} руб.",
                               reply_markup=remove)


@bot.message_handler(commands=["game"])
def choose_game(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Конфетки', 'Крестики-нолики')
    msg = bot.reply_to(message,
                       "Выберите игру :)",
                       reply_markup=markup)
    bot.register_next_step_handler(msg, process_game)


def process_game(message):
    global mode
    mode = message.text
    msg = bot.reply_to(message,
                       f"Запускаем {mode}\nВведите свой никнейм")
    if (mode == 'Конфетки'):
        bot.register_next_step_handler(msg, candy_welcome)
    elif (mode == 'Крестики-нолики'):
        msg = bot.reply_to(message, "Эту игру пока еще не добавили")


def candy_welcome(message):
    global nikname
    nikname = message.text
    turn = choice(['Bot', nikname])
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Начать игру')
    msg = bot.reply_to(message,
                       "Начнем?",
                       reply_markup=markup)
    msg = bot.send_message(message.chat.id,
                           f'Начинает {turn}')
    if turn == 'Bot':
        bot.register_next_step_handler(msg, bot_turn)
    elif turn == nikname:
        bot.register_next_step_handler(msg, user_take)


def user_take(message):
    global candys
    if candys > 28:
        msg = bot.send_message(message.chat.id, "Сколько конфет взять?")
        bot.register_next_step_handler(msg, user_turn)
    else:
        msg = bot.send_photo(message.chat.id,
                             photo=user_win,
                             caption=f"На этот раз {nikname} победил")
        candys = 117


def user_turn(message):
    try:
        global candys
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Я всё понял')
        take = int(message.text)
        if 0 < take < 29:
            if candys > 29:
                candys -= take
                msg = bot.send_message(message.chat.id,
                                       f'В коробке осталось {candys}')
                bot_turn(message)
        else:
            msg = bot.reply_to(message,
                               "Можно взять не больше 28 конфет, попробуй еще",
                               reply_markup=markup)
            bot.register_next_step_handler(msg, user_take)
    except ValueError:
        msg = bot.reply_to(message,
                           "Вводите только цифры",
                           reply_markup=markup)
        bot.register_next_step_handler(msg, user_take)


def bot_turn(message):
    global candys
    if candys > 28:
        take = randint(1, 28)
        candys -= take
        bot.send_message(message.chat.id,
                         f'Я взял {take}\nВ коробке осталось {candys}')
        user_take(message)
    else:
        bot.send_photo(message.chat.id,
                       photo=bot_win,
                       caption=f'Увы, ты проиграл {nikname}')             
        candys = 117


bot.infinity_polling()