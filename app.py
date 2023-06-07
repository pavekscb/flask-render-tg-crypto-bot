import os
from flask import Flask, request, Response
from telegram import Bot

app = Flask(__name__)

TELEGRAM_API_TOKEN = os.environ['BOT_TOKEN']
bot = Bot(TELEGRAM_API_TOKEN)
user_chat_id = os.environ['CHANNEL_ID']

@app.route('/')
def hello():
    return 'Сервис для отправки уведомлений в Telegram канал'

@app.route('/notify', methods=['POST'])
def notify():
    bot.send_message(chat_id=user_chat_id, text="HELLO WORD")
    return Response(status=200)

if __name__ == '__main__':
    app.run()
