import telebot, random, time

bot = telebot.TeleBot('910461142:AAFdjWJQnU5uFXphLPyY0RqwaY7cgnZYuwY')


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет, я - бот польских слов. \nДобро пожаловать в чудный мир просвящения польским языком.Я весь к вашим услугам!😁 \n/help - список всех доступных команд ")


@bot.message_handler(commands=['new'])
def new_command(message):
    lines = open('Polish_words.txt', encoding='utf-8').read().splitlines()
    my_line = random.choice(lines)
    bot.send_message(message.chat.id, my_line)


@bot.message_handler(commands=['mailing'])
def new_command(message):
    while True:
        lines = open('Polish_words.txt', encoding='utf-8').read().splitlines()
        my_line = random.choice(lines)
        bot.send_message(message.chat.id, my_line)
        bot.send_message(message.chat.id, "🕘")
        time.sleep(900)


@bot.message_handler(commands=['help'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/new', '/mailing', '/test')
    bot.send_message(message.chat.id, 'Доступные команды:\n/new - пришлю новое слово с переводом\n/mailing - буду высылать слова с переводом каждые 15 минут\n/test - единоразовое тестирование', reply_markup=keyboard)


@bot.message_handler(commands=['test'])
def start_message(message):
    lines1 = open('Polish_words.txt', encoding='utf-8').read().splitlines()
    my_line1 = str(random.choice(lines1))
    lis_tik1 = my_line1.split('-')
    lines = open('Polish_words.txt', encoding='utf-8').read().splitlines()
    my_line = str(random.choice(lines))
    lis_tik = my_line.split('-')
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text=lis_tik[1], callback_data='true'))
    markup.add(telebot.types.InlineKeyboardButton(text=lis_tik1[1], callback_data='false'))
    bot.send_message(message.chat.id, text="Какой перевод слова " + lis_tik[0] + "?", reply_markup=markup)
    time.sleep(6)
    bot.send_message(message.chat.id, "Верный перевод:\n" + my_line)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    answer = ''
    if call.data == 'true':
        answer = 'Правильно!'
    elif call.data == 'false':
        answer = 'Не правильно!'

    bot.answer_callback_query(callback_query_id=call.id, text=answer)




@bot.message_handler(content_types=['text'])
def send_ans(message):
    bot.send_message(message.chat.id, "Не понимаю о чем говоришь.\n/help - список доступных комманд")


if __name__ == '__main__':
    bot.polling(none_stop=True)

