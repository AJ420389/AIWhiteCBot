import asyncio
from aiogram import Bot, Dispatcher, types
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я бот по генерации whitepaper на ИИ. Введи команду /whitepaper.")

@dp.message_handler(commands=['whitepaper'])
async def whitepaper(message: types.Message):
    await message.reply("Отлично! Генерация whitepaper скоро будет доступна. Пока это заглушка 😉")

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
