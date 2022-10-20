# Telegram Bot

**Задача:**

Написать бота для telegram.
Бот должен уметь принимать от пользователя данные, при помощи которох отправлять запросы к API сервиса kopeechka.store. После чего пользователь получает необходимую информацию.

#### Используемые технологии:
aiogram, API, регулярные выражения

#

**Для запуска бота необходимо:**

1. Клонировать репозиторий:
```bash
git clone https://github.com/radik121/tg_bot_kopeechka.git
```

2. Перейти в корневую папку проекта:
```bash
cd tg_bot_kopeechka
```

3. Для запуска проекта выполнить команду:
```bash
docker-compose up -d --build
```
*либо через консоль python3 ./app.py*