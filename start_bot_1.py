from aiogram import Bot, Dispatcher , types , executor
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Салам алейкум")
    
@dp.message_handler(commands='help')
async def start(message:types.Message):
    await message.answer("Че надо черт?")
    
@dp.message_handler(text='Привет')
async def hello(message:types.Message):
    await message.reply("че делаешь черт?")
    
@dp.message_handler(commands='test')
async def test(message:types.Message):
    await message.answer_location(534, 976)
    await message.answer_photo("https://sun9-50.userapi.com/impg/C8-zBwKOhx1XUGKSl29qxTY9Wu6isDaZF4aZMQ/PlSH0JOCfpE.jpg?size=570x807&quality=96&sign=a676a358eb3151db5032b8faad64f29b&c_uniq_tag=nM73LBVC36VROuHKd4DxvUmfPF-bhD6GjOV-gWRbUmk&type=album")

executor.start_polling(dp)


