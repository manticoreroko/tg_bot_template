from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import ReplyKeyboardRemove

async def on_startup(_):
    await bot.send_message(chat_id=MAIN_ID, text='Бот запущен', reply_markup=ReplyKeyboardRemove())
    await set_main_menu(dp=dp)