from aiogram.utils import executor
from bot_loader import dp
from handlers import client


client.register_client()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)