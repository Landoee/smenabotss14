import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
TOKEN_API = "7560720475:AAF_ScGyPV8hy2N4ilLvgeRjm8HO_eOP9TM"
bot = Bot(TOKEN_API)
dp = Dispatcher()

@dp.message(Command("start"))
async def bot_start(message: types.Message):
    await message.answer("Ку бро, рад что ты заинтересовался нашим сервером")

@dp.message(Command("description"))
async def bot_describe(message: types.Message):
    await message.answer("тут типо описание")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())