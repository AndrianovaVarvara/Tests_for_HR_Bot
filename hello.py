# Для начала следует импортировать библиотеку и подключить токен Telegram-бота на Python
import telebot
from telebot import types

bot = telebot.TeleBot('1674146353:AAH_RT5G4jqkoFNcSC6oKM_fYc0SVYWk0dI')

# Теперь напишем обработчик текстовых сообщений, который будет обрабатывать входящую команду /start, через запятую
# можно добавить /help
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Начинаем! Поздоровайся с ботом, ему будет приятно")

# Добавим ещё один обработчик для получения текстовых сообщений. Если бот получит «Привет», он также поздоровается.

#  это кнопочки чтобы ответить боту. ReplyKeyboardMarkup — это шаблоны сообщений.
#  К примеру, ваш бот задаёт пользователю вопрос и предлагает варианты ответа.
#  Пользователь может самостоятельно напечатать ответ, либо нажать на готовую кнопку.
#  Такая клавиатура показывается вместо основной и не привязана ни к какому сообщению.
#  В кнопки такой клавиатуры нельзя заложить никакой информации,
#  нельзя запрограммировать для неё подобный алгоритм, если пользователь нажимает кнопку с текстом «abc» отправить
#  текст «qwerty»  отправлено будет только то, что написано на кнопке (есть два исключения, о которых ниже).

mm = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
button1 = types.KeyboardButton(" Учиться")
button2 = types.KeyboardButton(" Играть")
mm.add(button1,button2)
# keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, True)
# # первый Тру отвечает за размер, второй за исчезновение
# keyboard1.row('Учиться', 'Играть')

@bot.message_handler(content_types=['text'])
def hello_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}')
        bot.send_message(message.from_user.id, 'Чем хочешь заняться? Будем учиться или пойграем?',
                         reply_markup=mm)

    if message.text == " Учиться":
        bot.send_message(message.chat.id, "Отлично!")
    if message.text == " Играть":
        bot.send_message(message.chat.id, "Будь серьезней!")
        # if message.from_user.id == 'Учиться':
        #     bot.send_message(message.from_user.id, 'Ok')
        # else:
        #     bot.send_message(message.from_user.id, 'Будь серьезней!')
    # else:
    #     # Все остальные сообщения будут определены, как нераспознанные
    #     bot.send_message(message.from_user.id, 'А поздороваться?!')

# @bot.message_handler(content_types=['sticker'])
# def stics(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, 'Привет, мой создатель')
#     elif message.text.lower() == 'пока':
#         bot.send_message(message.chat.id, 'Прощай, создатель')

# Запускаем бота следующей строкой. Так мы задаём боту непрерывное отслеживание новых сообщений. 
# Если бот упадёт, а сообщения продолжат поступать, они будут накапливаться в течение 24 часов 
# на серверах Telegram, и в случае восстановления бота прилетят ему все сразу.
bot.polling(none_stop=True)