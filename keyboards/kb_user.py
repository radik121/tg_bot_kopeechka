from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

btnGetCode = KeyboardButton('📩 Получить код из почты kopeechka')
btnCode = KeyboardButton('КОД')
btnMassage = KeyboardButton('Сообщение')
btnBack = KeyboardButton('◀️ Назад')
btnApiSt = KeyboardButton('Стандартный API')
btnApiEnter = KeyboardButton('Ввести свой API')
btnSendCode = KeyboardButton('Код отправлен')


start_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnGetCode)
code_or_msg_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCode).add(btnMassage).add(btnBack)
api_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnApiSt).add(btnApiEnter).add(btnBack)
back = ReplyKeyboardMarkup(resize_keyboard=True).add(btnBack)
send_code = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSendCode)