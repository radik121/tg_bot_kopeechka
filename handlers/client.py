from conf import KP_API
from aiogram import types
from bot_loader import dp, bot
from keyboards import start_menu, code_or_msg_menu, api_menu, back, send_code
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
import asyncio
from additional_func import check, mailbox_reorder, mailbox_message, parse_facebook



class Form(StatesGroup):
    services = State()
    code_or_text = State()
    api = State()
    you_api = State()
    email = State()
    send_message = State()


async def set_default_commands(dp):
    """Стандартные команды для бота"""

    await dp.bot.set_my_commands([
        types.BotCommand("start", "Услуги"),
        types.BotCommand("cancel", "Отменить")
    ])


async def first_command(message: types.Message):
    """Хэндлер на команду /start"""

    await Form.services.set()
    await message.answer(text='Выберите услугу', reply_markup=start_menu)


async def cancel_handler_state(message: types.Message, state: FSMContext):
    """Добавляем возможность отмены, если пользователь передумал заполнять"""

    current_state = await state.get_state()
    match current_state:
        case None:
            return
    await state.finish()
    await message.reply('Хорошо, чтобы начать заново, введите /start', reply_markup=ReplyKeyboardRemove())


async def check_correctness_name_service(message: types.Message):
    """Обработка неправильно введеной услуги"""

    await message.reply("Введите корректную услугу.", reply_markup=start_menu)


async def second_command(message: types.Message, state: FSMContext):
    """Запрашиваем, что получить: КОД или Сообщение целиком"""

    await Form.next()
    await message.answer('Выберите, какое сообщение вы хотите получить?', reply_markup=code_or_msg_menu)


async def select_code_or_message(message: types.Message, state: FSMContext):
    """Записываем в словарь прошлое сообщение и запрашиваем API"""

    match message.text:
        case '◀️ Назад':
            await state.set_state(Form.services)
            await message.answer("Выберите услугу.", reply_markup=start_menu)
        case _:
            await state.update_data(code_or_text = message.text)
            await state.set_state(Form.api)
            await message.answer('Выберите API для получения кода!', reply_markup=api_menu)


async def select_api(message: types.Message, state: FSMContext):
    """Выбрать какое API использовать при запросе и ввести email"""

    match message.text:
        case '◀️ Назад':
            await state.set_state(Form.code_or_text)
            await message.answer('Выберите, какое сообщение вы хотите получить?', reply_markup=code_or_msg_menu)
        case 'Стандартный API':
            await state.update_data(api = KP_API)
            await state.set_state(Form.email)
            await message.answer('Введите email аккаунта', reply_markup=back)
        case 'Ввести свой API':
            await state.set_state(Form.you_api)
            await message.answer('Введите ваш API', reply_markup=back)
    await state.update_data(site = 'facebook.com')
    # data = await state.get_data()
    # print(data)


async def input_api(message: types.Message, state: FSMContext):
    """Ввод собственного API и email"""

    match message.text:
        case '◀️ Назад':
            await state.set_state(Form.api)
            await message.answer('Выберите API для получения кода!', reply_markup=api_menu)
        case _:
            await state.update_data(api = message.text)
            await state.set_state(Form.email)
            await message.answer('Введите email аккаунта', reply_markup=back)
    # data = await state.get_data()
    # print(data)
        

async def input_email(message: types.Message, state: FSMContext):
    """Вводим email и активируем на kopeechka"""

    match check(message.text):
        case '◀️ Назад':
            await state.set_state(Form.api)
            await message.answer('Выберите API для получения кода!', reply_markup=api_menu)
        case True:
            await state.update_data(email = message.text)
            await message.answer("Сейчас активируем почту...")

            data = await state.get_data()
            # print(data)
            response = mailbox_reorder(data['api'], data['site'], data['email'])
            print('mailbox_reorder:', response['status'])

            match response['status']:
                case 'OK':
                    await state.update_data(task_id = response['id'])
                    await state.set_state(Form.send_message)
                    await message.answer("Почта активирована.")
                    await message.answer(
                        f"На сайте {data['site']} нажмите 'Получить код по почте', и только потом нажми <b>'Код отправлен'</b>",
                        reply_markup=send_code
                    )
                case _:
                    await message.answer(
                        "API или email или сайт не корректны, поробуйте заново ввести их",
                        reply_markup=api_menu
                    )
                    await state.set_state(Form.api)
        case _:
            await message.answer('Это не похоже на email адрес!')
            await message.answer('Введите email аккаунта', reply_markup=back)
    # data1 = await state.get_data()
    # print(data1)


async def process_get_code(message: types.Message, state: FSMContext):
    """Отправляем запрос на сайт копеечки и получаем код"""

    await message.answer("Сейчас получим код...Время ожидания составит около 1 мин.")
    await asyncio.sleep(60)
    data = await state.get_data()
    response = mailbox_message(token=data['api'], full='1', id=data['task_id'])
    print(f"mailbox_message: {response['status']} - {response['value']}")
    match response['status']:
        case 'OK':
            match data['code_or_text']:
                case 'КОД':
                    message_email = parse_facebook(str(response['fullmessage']))
                case 'Сообщение':
                    message_email = response['fullmessage']        
            await bot.send_message(message.from_user.id, message_email, reply_markup=start_menu)
            await Form.services.set()
        case _:
            await bot.send_message(
                message.from_user.id,
                "Вы не отправили письмо или оно еще не пришло. Отправьте его повторно или нажмите <b>'Код отправлен'</b>",
                reply_markup=send_code
            )


def register_client():
    # dp.register_message_handler(set_default_commands)
    dp.register_message_handler(first_command, commands='start', state=None)
    dp.register_message_handler(cancel_handler_state, commands='cancel', state='*')
    dp.register_message_handler(cancel_handler_state, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(check_correctness_name_service, lambda message: message.text != '📩 Получить код из почты kopeechka', state=Form.services)
    dp.register_message_handler(second_command, state=Form.services)
    dp.register_message_handler(select_code_or_message, state=Form.code_or_text)
    dp.register_message_handler(select_api, state=Form.api)
    dp.register_message_handler(input_api, state=Form.you_api)
    dp.register_message_handler(input_email, state=Form.email)
    dp.register_message_handler(process_get_code, lambda message: message.text == "Код отправлен", state=Form.send_message)