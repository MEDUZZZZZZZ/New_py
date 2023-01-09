import telebot
from telebot import types
from random import randint, choice

API_TOKEN = '5960431180:AAE0_T3_UM-vPfATvPdNQ7sZ5wTKAOTWPl4'

bot = telebot.TeleBot(API_TOKEN)
candys = 117
nikname = ''
bot_win = 'https://www.meme-arsenal.com/memes\
           /3f55b57005fd745cfb18730750b144f9.jpg'
user_win = 'https://i.imgflip.com/4/3nzkub.png'


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я самый лучший на свете бот!
Умею играть в игры, и скоро научусь предоставлять актуальный курс валют.
Для получения списка команд пропишите /help
""")


@bot.message_handler(commands=["help"])
def commands_helper(message):
    bot.send_message(message.chat.id, """\
Список доступных команд:
Сыграть в игру - /game
Получить список доступных команд - /help""")


@bot.message_handler(commands=["game"])
def choose_game(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Конфетки', 'Крестики-нолики')
    msg = bot.reply_to(message,
                       "Выберите игру :)",
                       reply_markup=markup)
    bot.register_next_step_handler(msg, process_game)


def process_game(message):
    mode = message.text
    if (mode == 'Конфетки'):
        msg = bot.reply_to(message,
                           f"Запускаем {mode}\nВведите свой никнейм")
        bot.register_next_step_handler(msg, candy_welcome)
    elif (mode == 'Крестики-нолики'):
        msg = bot.reply_to(message,
                           "Игра в разработке, попробуйте в другой раз")


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
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
                markup.add('Передать ход')
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
