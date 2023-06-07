import os  # Импорт модуля os для работы с операционной системой
from flask import Flask, request, Response  # Импорт классов Flask, request и Response из модуля flask для создания веб-приложения и обработки HTTP-запросов
from telegram import Update, Bot  # Импорт классов Update и Bot из модуля telegram для работы с Telegram API
from telegram.ext import Updater, CommandHandler, CallbackContext  # Импорт классов Updater, CommandHandler и CallbackContext из модуля telegram.ext для создания и настройки Telegram бота

app = Flask(__name__)  # Создание экземпляра приложения Flask

# Устанавливаем настройки для Telegram бота
TELEGRAM_API_TOKEN = os.environ['BOT_TOKEN']  # Получение токена Telegram бота из переменной окружения
bot = Bot(TELEGRAM_API_TOKEN)  # Создание экземпляра Telegram бота
user_chat_id = os.environ['CHANNEL_ID']  # Получение идентификатора чата из переменной окружения

@app.route('/')
def hello():
    return 'Сервис для отправки уведомлений в Telegram канал'

@app.route('/notify', methods=['POST'])
def notify():
    bot.send_message(chat_id=user_chat_id, text="HELLO WORD")
    return Response(status=200)

if __name__ == '__main__':
    app.run()
