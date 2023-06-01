import os  # Импорт модуля os для работы с операционной системой
from flask import Flask, request, Response  # Импорт классов Flask, request и Response из модуля flask для создания веб-приложения и обработки HTTP-запросов
from telegram import Update, Bot  # Импорт классов Update и Bot из модуля telegram для работы с Telegram API
from telegram.ext import Updater, CommandHandler, CallbackContext  # Импорт классов Updater, CommandHandler и CallbackContext из модуля telegram.ext для создания и настройки Telegram бота

app = Flask(__name__)  # Создание экземпляра приложения Flask

# Устанавливаем настройки для Telegram бота
TELEGRAM_API_TOKEN = os.environ['BOT_TOKEN']  # Получение токена Telegram бота из переменной окружения
bot = Bot(TELEGRAM_API_TOKEN)  # Создание экземпляра Telegram бота
user_chat_id = os.environ['CHANNEL_ID']  # Получение идентификатора чата из переменной окружения

@app.route('/')  # Маршрут для главной страницы
def hello():
    return 'Сервис для отправки уведомлений в Telegram канал'

@app.route('/notify', methods=['POST','GET'])  # Маршрут для обработки уведомлений. Разрешены методы POST и GET
def notify():
    logs = request.json  # Получение данных уведомления в формате JSON
    if (len(logs) == 0):  # Проверка, если массив логов пуст
        print("Пустой массив логов, пропускаем")
    else:
        print(logs)  # Вывод полученных логов

        category = ""
        try:
            category = logs['event']['activity'][0]['category']  # Извлечение категории лога, если она определена
        except:
            print("Категория не определена")

        if logs['webhookId'] == os.environ['ALCHEMY_KEY'] and category == 'token':
            # Извлечение необходимой информации о транзакции
            txhash = from_address = "["+str(logs['event']['activity'][0]['hash'])+"](https://etherscan.io/tx/"+str(logs['event']['activity'][0]['hash'])+")"

            from_address = "["+str(logs['event']['activity'][0]['fromAddress'])+"](https://etherscan.io/address/"+str(logs['event']['activity'][0]['fromAddress'])+"#tokentxns)"
            to_address = "["+str(logs['event']['activity'][0]['toAddress'])+"](https://etherscan.io/address/"+str(logs['event']['activity'][0]['toAddress'])+"#tokentxns)"

            token_symbol = logs['event']['activity'][0]['asset']
            token_address = "["+str(logs['event']['activity'][0]['rawContract']['address'])+"](https://etherscan.io/address/"+str(logs['event']['activity'][0]['rawContract']['address'])+")"

            value = str(round(logs['event']['activity'][0]['value']))

            # Формирование текстовой строки
            #message = f'*Перевод токена:*\n{txhash}\nс {from_address} \nна {to_address}: \nзначение: {value} *{token_symbol}* {token_address}'
            message = f'*Перевод токена:*\n{txhash}\nс {from_address} \nна {to_address}: \nзначение: {value} *{token_symbol}*'
            bot.send_message(chat_id=user_chat_id, text=message, parse_mode='MarkdownV2')  # Отправка сообщения в чат с использованием Telegram бота

    return Response(status=200)  # Возвращение HTTP-ответа со статусом 200

updater = Updater(TELEGRAM_API_TOKEN)  # Создание экземпляра Updater с использованием токена Telegram бота
updater.start_polling()  # Запуск бота и ожидание обновлений

if __name__ == '__main__':
    app.run()  # Запуск приложения Flask
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
