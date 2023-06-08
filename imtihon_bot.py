# TASK 1

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6005423465:AAGc51detDC_Utw3NmFI6HhbpY707ueJe6s'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    word = ""
    await message.reply("Iltimos, biror bir so'z kiriting!:")
    for i in message:
        if i in 'aeiou':
            word+=i

    if len(word) > 5:
        await message.delete()


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

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
#      this email sent by python script
# """.format(sender,reciver)
#
# with smtplib.SMTP_SSL(server,port) as server:
#     server.login(sender,password)
#     server.sendmail(sender,reciver,msg)
#     print("Message has been sent")