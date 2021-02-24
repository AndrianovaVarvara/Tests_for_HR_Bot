# Для начала следует импортировать библиотеку и подключить токен Telegram-бота на Python
import telebot
bot = telebot.TeleBot('1674146353:AAH_RT5G4jqkoFNcSC6oKM_fYc0SVYWk0dI')

# Теперь напишем обработчик текстовых сообщений, который будет обрабатывать входящие команды /start и /help
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

# Добавим ещё один обработчик для получения текстовых сообщений. Если бот получит «Привет», он также поздоровается. 
# Все остальные сообщения будут определены, как нераспознанные    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Пока что это всё, что я умею :(')

# Запускаем бота следующей строкой. Так мы задаём боту непрерывное отслеживание новых сообщений. 
# Если бот упадёт, а сообщения продолжат поступать, они будут накапливаться в течение 24 часов 
# на серверах Telegram, и в случае восстановления бота прилетят ему все сразу.
bot.polling(none_stop=True)