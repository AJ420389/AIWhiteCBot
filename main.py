import logging
from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("👋 Добро пожаловать! Отправьте ваш запрос на создание whitepaper.
Мы свяжемся с вами в ближайшее время.")

@dp.message_handler()
async def forward_to_admin(message: types.Message):
    admin_id = int(ADMIN_ID)
    text = f"📩 Новая заявка от @{message.from_user.username or message.from_user.id}:

{message.text}"
    await bot.send_message(chat_id=admin_id, text=text)
    await message.reply("✅ Заявка отправлена. Ожидайте ответ.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
