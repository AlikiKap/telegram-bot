from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '6261406455:AAE8EQPwyHFtI7uX5jw8C9umRwXSOcnyq8o'
bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)
@dp.message_handler(commands=['start']) 
async def send_welcome(message: types.Message):
    await message.reply("Здравствуйте! Добро пожвловать в чат-бот врача Капасакалиди Дианы Фердинандовны. Здесь вы можете записаться на приём.")
@dp.message_handler()
async def echo(message: types.Message):
   await message.answer(message.text)
 
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
