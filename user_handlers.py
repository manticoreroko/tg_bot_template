from aiogram.types import Message
from aiogram.filters import Command, CommandStart

# Этот хэндлер срабатывает на команду /start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Приветствие')


# Этот хэндлер срабатывает на команду /help
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text='Помощь')