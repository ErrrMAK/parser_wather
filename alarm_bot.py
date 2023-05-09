# Бот уведомлялка об окончании скрипта
import telegram
import time
import os
import asyncio
from ip_rotate import proxys

# Создаем объект бота
bot = telegram.Bot(token='5674190609:AAFfqNuRVyJJzU0_aOGiDy6e7S8Q5iPGtus')

# Отправляем сообщение
async def send_message():
    await bot.send_message(chat_id='257661905', text='Ваш код завершил работу! \n'+'cnt_200 ='+ str(proxys[1]) + '\n cnt_400 =' + str(proxys[2]))
# Запускаем ваш код
async def run_code():
    # здесь ваш код
    os.system('ip_rotate.py')
    time.sleep(1) # пример задержки в 10 секунд

# Запускаем код и отправляем сообщение
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.gather(run_code(), send_message()))
    finally:
        loop.close()
