import asyncio
from aiogram import Bot,Dispatcher
from dotenv import load_dotenv
import os
import funksiyalar
from aiogram.filters import Command
from aiogram.types import  Message
load_dotenv(override=True)
dp=Dispatcher()
@dp.startup()
async def bot_ishlaganda(bot:Bot):
    await bot.send_message(chat_id=os.getenv("Admin_id"),text="Bot ishladi✅")
@dp.shutdown()
async def bot_toxtaganda(bot:Bot):
    await bot.send_message(chat_id=os.getenv("Admin_id"),text="Bot to'xtadi❗")
@dp.message(Command("start"))
async def start_bosilganda(m:Message):
    await m.answer(f"xush kelipsiz {m.from_user.full_name}")
@dp.message(Command("help"))
async def help_bosilganda(m:Message):
    await m.answer(f"Yordam bo'limi hurmatli: {m.from_user.full_name}")
@dp.message()
async def echo(m:Message):
    try:
        await m.answer(funksiyalar.obhavo(funksiyalar.lakatsiya_aniqlash(m.text)))
    except:
        await m.answer("shahar nomini to'g'ri kiriting")


async def main():
    bot=Bot(token=os.getenv("Bot_Token"))
    await dp.start_polling(bot)

if __name__== '__main__':
    asyncio.run(main())


