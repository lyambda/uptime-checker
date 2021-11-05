# -*- coding: utf-8 -*-

# AIOGRAM
from aiogram import Bot, Dispatcher, types, filters
from aiogram.utils import executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# ...
import asyncio, requests

group_id = -1001779124992
bot_token = '2101306193:AAGJyt5ShywY7dzxtJA1Mih3THfqL7DT2gc'

json_text= ''
last_status_code = 0
loop = asyncio.get_event_loop()
delay = 60.0

async def my_func():
    global last_status_code
    when_to_call = loop.time() + delay  # delay -- промежуток времени в секундах.
    loop.call_at(when_to_call, my_callback)
    try:
        res = requests.post('https://lyabmda.herokuapp.com/me', data={"token": "TNhrDiyY5LBRUZHMztjKgq6sa78PJCdc"})
        emoji = '🔴'
        if res.status_code >= 200 and res.status_code <= 299:
            emoji = '✅'
        if last_status_code != res.status_code:
            await bot.send_message(group_id, f'<b>🌐 λ api: </b> [{emoji}] {res.status_code} <i>/me</i>\n\n<code>{res.text}</code>', parse_mode='HTML')
        last_status_code = res.status_code
    except Exception as e:
        await bot.send_message(group_id, f'<code>{e}</code>', parse_mode='HTML')

def my_callback():
    asyncio.ensure_future(my_func())

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

# /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.chat.id, 'https://lyambda.github.io/')
    try:
        res = requests.post('https://lyabmda.herokuapp.com/me', data={"token": "TNhrDiyY5LBRUZHMztjKgq6sa78PJCdc"})
        emoji = '🔴'
        if res.status_code >= 200 and res.status_code <= 299:
            emoji = '✅'
        await bot.send_message(group_id, f'<b>🌐 λ api: </b> [{emoji}] {res.status_code}', parse_mode='HTML')
    except Exception as e:
        await bot.send_message(group_id, f'<code>{e}</code>', parse_mode='HTML')

# /start
@dp.message_handler(commands=['me'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.chat.id, '-_-')

if __name__ == "__main__":
    my_callback()
    executor.start_polling(dp)