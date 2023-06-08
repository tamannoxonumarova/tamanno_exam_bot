# TASK 1
import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

TOKEN = os.environ["6005423465:AAGc51detDC_Utw3NmFI6HhbpY707ueJe6s"]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message, state: FSMContext):
    await message.reply(f"Assalomu alaykum {message.from_user.full_name} 😊")
    await message.answer("Text Kiriting")
    await state.set_state("text")


@dp.message_handler(state="text")
async def echo(message: types.Message, state: FSMContext):
    All_vowels = "aeiouAEIOU"
    summa = sum([1 for i in message.text if i in All_vowels])
    if summa >= 5:
        await message.answer("Text unlilar soni 5 dan oshib ketti. Qayta kiriting")
        await state.set_state("text")
    else:
        await state.set_state("text")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


# TASK 3

# import requests
# from redis import Redis
# from rq import Queue
# from time import sleep
#
# q = Queue(connection=Redis())
#
# def make_request(url):
#     response = requests.get(url)
#     data = response.json()
#     return data
#
# def save_data(data, redis_conn, key):
#     redis_conn.setex(key, 60, data)
#
# def crawl(url, redis_conn, key):
#     data = make_request(url)
#     save_data(data, redis_conn, key)
#
# def threads():
#     redis_conn = Redis()
#     urls = [
#         ('http://example.com', 'oqim1'),
#         ('http://example.org', 'oqim2'),
#         ('http://example.net', 'oqim3'),
#         ('http://example.co.uk', 'oqim4'),
#         ('http://example.edu', 'oqim5')
#     ]
#     while True:
#         for url, key in urls:
#             job = q.enqueue(crawl, url, redis_conn, key)
#         sleep(60)
#
# if __name__ == '__main__':
#
#   threads()




#TASK 4

# import smtplib
#
# from pasword import test
#
#
# password = test
# sender = "tamannoumarova321@gmail.com"
# server = "smtp.gmail.com"
# port = 465
# reciver = "absaitovdev@gmail.com"
# msg = """
# from: {}
# to: {}
# subject:
#     https://github.com/tamannoxonumarova/tamanno_exam_bot.git
# """.format(sender,reciver)
#
# with smtplib.SMTP_SSL(server,port) as server:
#     server.login(sender,password)
#     server.sendmail(sender,reciver,msg)
#     print("Message has been sent")