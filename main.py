from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton,  InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '6261406455:AAE8EQPwyHFtI7uX5jw8C9umRwXSOcnyq8o'
bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text="Записаться на приём",url='http://www.example.com/')
urlButton2 = InlineKeyboardButton(text="Оплатить",url='http://www.example.com/')
urlkb.add(urlButton,urlButton2)
@dp.message_handler(commands=['start']) 
async def url_command(message:types.Message):
    await message.answer("Здравствуйте! Добро пожаловать в чат-бот врача Капасакалиди Дианы Фердинандовны. Здесь вы можете записаться на приём.", reply_markup=urlkb)

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
