from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from main import get_content
import json

tg_bot = '5294553710:AAG8yipLIRlr6Zp4ahArJpBmt3_mTzzth9s'

bot = Bot(token=tg_bot, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["news"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("today's news", reply_markup=keyboard)

@dp.message_handler(Text(equals="news"))
async def get_news(message: types.Message):
    await message.answer('Please wait...')

    get_content()

    with open("kloop.json") as file:
        data = json.load(file)

    for item in data:
        card = f"{hlink(item.get('title'), item.get('link'))}\n" \
            f"{hbold('title: ')} {item.get('title')}\n" \
            f"{hbold('link_news: ')} {item.get('link_news')}\n" \
            f"{hbold('date: ')} {item.get('date')}\n" \
            f"{hbold('photo: ')} {item.get('photo')}"
        await message.answer(card)

def main():
    executor.start_polling(dp)

if __name__ == "__main__":
    main()
