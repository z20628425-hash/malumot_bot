import asyncio
import logging
import os
import sys

import asyncio

from aiogram import Dispatcher,Bot,F
from aiogram.filters import Command
from aiogram.types import Message, BotCommand
from dotenv import load_dotenv
load_dotenv()
API=os.getenv('API')
dp=Dispatcher()
ovozlar={
    '👨‍✈️ Sardor 🇺🇿':'uz-UZ-SardorNeural',
    '👩‍✈️ Sardor 🇺🇿':'uz-UZ-MadinaNeural'
}
async def defolut(bot :Bot):
    command=[
        BotCommand(command='start',description='Boslab ber'),
        BotCommand(command='help',description='Boslab ber')
    ]
    await bot.set_my_commands(command)

@dp.message(Command('start'))
async def start_handler(msg:Message):
    await msg.answer("salom hush kelibsiz")

@dp.message(Command('help'))
async def start_handler(msg:Message):
    await msg.answer("Assalomu allekum sizga qanday yordam bera olaman")

@dp.message(F.text.in_('Men'))
async def salom_handler(msg:Message):
    await msg.answer('Salom')

@dp.message()
async def message_handler(msg:Message):
    T=msg.text
    await msg.answer('Assalomu allekum')


async def main():
    bot=Bot(token=API)
    await defolut(bot)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,stream=sys.stdout)
    asyncio.run(main())
