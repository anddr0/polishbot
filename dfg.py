import keyboard, time, pyautogui, win32gui, win32com.client, random, glob, pyowm, telebot, os
from prjcts import my_libs
from telebot import types
from win32gui import SetForegroundWindow
from pathlib import Path
from threading import Thread
from math import sqrt


def my_bot():  # Это бот
    try:
        chat_id = 840550973
        bot = telebot.TeleBot('1206860124:AAEFLYwaHK1SUKg1pt0ene4qt9IdULOBAo4')

        @bot.message_handler(commands=['help'])
        def answrrr(message):
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row(my_libs.game_boot[0], my_libs.sint_the_word[0])
            keyboard.row(my_libs.screen_shots[0], my_libs.auds[0])
            keyboard.row(my_libs.vids[0], '/напиши')
            keyboard.row('/погода')
            bot.send_message(message.chat.id, 'Доступные команды:\n/напиши - напишу на комп то, что отправлено\n/видео - пришлю видос \n/скриншот - пришлю скриншот', reply_markup=keyboard)

        @bot.message_handler(content_types=['text'])        # Реагирование на текст
        def get_text_messages(message):  # Это мы ищем команды в тексте и реагируем на них
            if message.text.lower() in my_libs.hi:  # Приветствие пользователя
                hism = random.randrange(0, len(my_libs.hi_smiles))
                hit = random.randrange(1, len(my_libs.bot_hi))
                bot.send_message(message.from_user.id, my_libs.bot_hi[hit])
                bot.send_message(message.from_user.id, my_libs.hi_smiles[hism])
            elif message.text.lower() in my_libs.game_boot:  # Запускание игры
                bot.register_next_step_handler(message, get_game_boot)
            elif message.text.lower() == "зашифруй":  # Шифр Цезаря
                bot.register_next_step_handler(message, get_open)
            elif message.text.lower() in my_libs.sint_the_word:  # Включается браузер и проговариваеться заданый текст
                quesm = random.randrange(0, len(my_libs.que_smiles))
                bot.send_message(message.from_user.id, "Что прочесть?")
                bot.send_message(message.from_user.id, my_libs.que_smiles[quesm])
                bot.register_next_step_handler(message, get_sint)
            elif message.text.lower() in my_libs.screen_shots:  # Делается скриншот и отправляется
                quesm = random.randrange(0, len(my_libs.que_smiles))
                bot.send_message(message.from_user.id, "Какое название?")
                bot.send_message(message.from_user.id, my_libs.que_smiles[quesm])
                bot.register_next_step_handler(message, send_photo)
            elif message.text.lower() in my_libs.auds:  # Записывается аудио и отправляется
                quesm = random.randrange(0, len(my_libs.que_smiles))
                bot.send_message(message.from_user.id, "Сколько секунд?")
                bot.send_message(message.from_user.id, my_libs.que_smiles[quesm])
                bot.register_next_step_handler(message, send_voice)
            elif message.text.lower() in my_libs.vids:  # Записывается видео и отправляется
                quesm = random.randrange(0, len(my_libs.que_smiles))
                bot.send_message(message.from_user.id, "Сколько секунд?")
                bot.send_message(message.from_user.id, my_libs.que_smiles[quesm])
                bot.register_next_step_handler(message, send_video)
            elif message.text.lower() in my_libs.comms:  # Перечисление команд
                bot.send_message(message.from_user.id, my_libs.game_boot[0] + "     " + my_libs.sint_the_word[0] + "     " + my_libs.screen_shots[0] + "     " + my_libs.auds[0] + "     " + my_libs.vids[0] + "   /напиши   " + "    /погода    ")
            elif message.text.lower() in my_libs.keyb:  # Это моя клавиатурка и я ею горжусь
                bot.register_next_step_handler(message, start_message)
            elif message.text.lower() == "enter":
                keyboard.press('enter')
            elif message.text.lower() == "space":
                keyboard.press('space')
            elif message.text.lower() == "backspace":
                keyboard.press('backspace')
            elif message.text.lower() == "/напиши":   # Это бот копирует и пишет на компе все что я ему скажу
                quesm = random.randrange(0, len(my_libs.que_smiles))
                bot.send_message(message.from_user.id, "А что?")
                bot.send_message(message.from_user.id, my_libs.que_smiles[quesm])
                bot.register_next_step_handler(message, write)
            elif message.text == "⬅️":
                keyboard.press('left')
            elif message.text == "➡️":
                keyboard.press('right')
            elif message.text == "⬆️":
                keyboard.press('up')
            elif message.text == "⬇️":
                keyboard.press('down')
            elif message.text.lower() == "/погода":  # Это я узнаю погоду
                weather(message)
            elif message.text.lower() == "/квадрат":  # Это мне решают квадратное уравнение
                bot.send_message(message.from_user.id, "Введи число a ")
                bot.register_next_step_handler(message, get_a)
            else:  # Это если я не то написал
                fusm = random.randrange(0, len(my_libs.fu_smiles))
                hit = random.randrange(1, len(my_libs.no_und))
                bot.send_message(chat_id, my_libs.fu_smiles[fusm])
                bot.send_message(chat_id, my_libs.no_und[hit])

        def get_a(message):
            global a
            a = int(message.text)
            bot.send_message(message.from_user.id, "Введи число b ")
            bot.register_next_step_handler(message, get_b)

        def get_b(message):
            global b
            b = int(message.text)
            bot.send_message(message.from_user.id, "Введи число c ")
            bot.register_next_step_handler(message, get_c)

        def get_c(message):
            global c
            c = int(message.text)
            calculate(message)

        def calculate(message):
            D = b ** 2 - 4 * a * c
            if D < 0:
                bot.send_message(message.from_user.id, "Уравнение не имеет решения, D < 0")
            elif D == 0:
                x = -b / 2 * a
                bot.send_message(message.from_user.id, "x = " + str(x))
            else:
                x1 = (-b - sqrt(D)) / (2 * a)
                x2 = (-b + sqrt(D)) / (2 * a)
                bot.send_message(message.from_user.id, "D = " + str(D) + ", √D = " + str(sqrt(D)))
                bot.send_message(message.from_user.id, "x1 = " + str(x1))
                bot.send_message(message.from_user.id, "x2 = " + str(x2))

        def weather(message):
            city = 'Karlivka,UA'
            owm = pyowm.OWM('9ef8de92394c439b01c6180c6fae3dda')
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(city)
            w = observation.weather
            temperature = w.temperature('celsius')['temp']
            wind_dict_in_meters_per_sec = observation.weather.wind()
            humid = w.humidity
            sens = temperature - 0.4 * (temperature - 10) * (1 - humid / 100)
            sky_is = w.detailed_status
            bot.send_message(message.from_user.id, "☀" + sky_is + "⛈")
            bot.send_message(message.from_user.id, "💨Скорость ветра: <b>" + str(wind_dict_in_meters_per_sec['speed']) + " </b>м/с", parse_mode='html')
            bot.send_message(message.from_user.id, "🔥Температура: <b>" + str(temperature) + "°C</b>" + " \n(Ощущается как: <b>" + str(int(sens)) + "°C)</b>", parse_mode='html')
            bot.send_message(message.from_user.id, "💦Влажность составляет: <b>" + str(humid) + "%</b>", parse_mode='html')
            bot.send_message(message.from_user.id, "📁")

        def write(message):
            mess = message.text
            keyboard.write(mess)

        def start_message(message):
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row('Space', 'Enter', 'BackSpace')
            keyboard.row('➡️', '⬅️', '⬆️', '⬇️')
            bot.send_message(message.chat.id, 'Keyboard', reply_markup=keyboard)

        def send_video(message):
            chat_id = 840550973
            directory = 'E:\\видс\\Desktop\\'
            os.chdir(directory)
            files = glob.glob('*.mp4')
            for filename in files:
                        os.unlink(filename)
            files = glob.glob('*.ogg')
            for filename in files:
                os.unlink(filename)
            secs = int(message.text)
            keyboard.press_and_release('alt + f9')
            time.sleep(secs)
            keyboard.press_and_release('alt + f9')
            time.sleep(5)
            name = os.listdir(path="E:\\видс\\Desktop\\")[0]
            video = open('E:\\видс\\Desktop\\' + name, 'rb')
            bot.send_video(chat_id, video)

        def send_voice(message):
            chat_id = 840550973
            directory = 'E:\\видс\\Desktop\\'
            os.chdir(directory)
            files = glob.glob('*.ogg')
            for filename in files:
                os.unlink(filename)
            files = glob.glob('*.mp4')
            for filename in files:
                os.unlink(filename)
            secs = int(message.text)
            keyboard.press_and_release('alt+f9')
            time.sleep(secs)
            keyboard.press_and_release('alt+f9')
            time.sleep(1)
            filename = os.listdir(path="E:\\видс\\Desktop\\")[0]
            new_filename = Path(filename).stem + ".ogg"
            os.rename('E:\\видс\\Desktop\\' + filename, 'E:\\видс\\Desktop\\' + new_filename)
            voice = open('E:\\видс\\Desktop\\' + new_filename, 'rb')
            bot.send_voice(chat_id, voice)

        def send_photo(message):
            chat_id = 840550973
            name = message.text + '.png'
            pyautogui.screenshot('D:\\3.14ton\\photos\\' + name)
            img = open('D:\\3.14ton\\photos\\' + name, 'rb')
            bot.send_photo(chat_id, img)

        def get_game_boot(message):
            keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
            key_apex = types.InlineKeyboardButton(text='Apex Legends', callback_data='apex')  # кнопка «Да»
            keyboard.add(key_apex)  # добавляем кнопку в клавиатуру
            key_factory = types.InlineKeyboardButton(text='Satisfactory', callback_data='factory')
            keyboard.add(key_factory)
            question = 'Какую?'
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_games(call):
            if call.data == "apex":
                os.startfile(r"D:\origin\Apex\r5apex")
                time.sleep(45)
                keyboard.press('space')
                bot.send_message(call.message.chat.id, 'Готово 🥴')
            elif call.data == "factory":
                os.startfile(r"D:\Satisfactory\FactoryGame")
                bot.send_message(call.message.chat.id, 'Готово 😬')


        def get_open(message):
            global op
            op = message.text
            bot.send_message(message.from_user.id, 'На сколько символов?')
            bot.register_next_step_handler(message, get_number)

        def get_number(message):
            global number
            number = int(message.text)
            bot.send_message(message.from_user.id, 'Готов узреть?')
            bot.register_next_step_handler(message, сaesars_code)

        def сaesars_code(message):
            mess = op
            if mess[0] in my_libs.ru_book:
                lang = my_libs.ru_book
            else:
                lang = my_libs.eng_book
            num = number
            a = list(mess)
            for i in a:
                try:
                    lang.index(i) + num
                    if i in lang:
                        ind = lang.index(i)
                        ans1 = (lang[ind + num])
                        bot.send_message(message.from_user.id, ans1)
                    else:
                        ans2 = ("Я еще не добавил этот язык ¯\_(ツ)_/¯ ")
                        bot.send_message(message.from_user.id, ans2)
                except IndexError:
                    kek = num - (len(lang) - lang.index(i))
                    bot.send_message(message.from_user.id, (lang[kek]))

        def get_sint(message):
            send = message.text
            pyautogui.click(x=165, y=1050)
            time.sleep(3)
            keyboard.press_and_release('ctrl + t')
            time.sleep(1)
            pyautogui.click(x=500, y=60)
            time.sleep(1)
            keyboard.write("https://ru.piliapp.com/text-to-speech/")
            time.sleep(1)
            keyboard.press('enter')
            time.sleep(1)
            pyautogui.click(x=600, y=210)
            time.sleep(1)
            keyboard.write(send)
            time.sleep(1)
            pyautogui.click(x=1100, y=210)
            bot.send_message(message.from_user.id, "Готово 🙃")

        if __name__ == '__main__':
            bot.polling(none_stop=True)
    except Exception:
        wnd = win32gui.FindWindow('SunAwtFrame', None)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        time.sleep(1)
        ifka = win32gui.GetForegroundWindow()
        if ifka == wnd:
            time.sleep(2)
            pyautogui.click(x=1818, y=45)
        else:
            SetForegroundWindow(wnd)
            time.sleep(2)
            keyboard.press_and_release('shift + f10')


thread1 = Thread(target=my_bot())
thread1.start()
