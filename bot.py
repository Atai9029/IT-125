import asyncio 
from aiogram import Bot, Dispatcher, types 
from aiogram.filters import Command 

API_TOKEN = '8534788233:AAG59XbG6hxgMfaZ1U8byH4U9erSNEiODZg'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def echo(massage: types.Message):
    await massage.answer('Хай ГИтЛЕР!')

@dp.message()
async def echo(message: types.Message):
    if message.text == "Иван": 
        await message.answer("ЧИСТЫЙ ГЕЙ!")
    elif message.text == "Данияр":
        await message.answer("Красава")
    elif message.text == "Я":
        await message.answer("Великий человек!")
    else:
        await message.answer(f'{message.text} гей')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())