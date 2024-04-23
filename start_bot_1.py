# from aiogram import Bot, Dispatcher , types , executor
# from config import token

# bot = Bot(token=token)
# dp = Dispatcher(bot)

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.answer("Салам алейкум")
    
# @dp.message_handler(commands='help')
# async def start(message:types.Message):
#     await message.answer("Че надо черт?")
    
# @dp.message_handler(text='Привет')
# async def hello(message:types.Message):
#     await message.reply("че делаешь черт?")
    
# @dp.message_handler(commands='test')
# async def test(message:types.Message):
#     await message.answer_location(534, 976)
#     await message.answer_photo("https://sun9-50.userapi.com/impg/C8-zBwKOhx1XUGKSl29qxTY9Wu6isDaZF4aZMQ/PlSH0JOCfpE.jpg?size=570x807&quality=96&sign=a676a358eb3151db5032b8faad64f29b&c_uniq_tag=nM73LBVC36VROuHKd4DxvUmfPF-bhD6GjOV-gWRbUmk&type=album")

# executor.start_polling(dp)


import schedule
import time
import requests

def hello_world():
    print(f"Hello World {time.ctime()}")

def backend_16_1B():
    print("Здравствуйте, сегодня у вас урок в 19:00")

def get_btc_price():
    response = requests.get('https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
    if response.status_code == 200:
        btc_data = response.json()
        btc_price = float(btc_data['price'])
        print(f"Цена биткоина на {time.strftime('%H:%M:%S')} составляет {btc_price}$")
    else:
        print("Ошибка при получении данных о цене биткоина")

schedule.every().monday.at('19:56').do(backend_16_1B)
schedule.every().minute.do(get_btc_price)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    # schedule.every(5).seconds.do(hello_world)
# schedule.every(1).minutes.do(hello_world)
# schedule.every().day.at('19:47').do(hello_world)
# schedule.every().monday.at('19:47').do(hello_world)
# schedule.every().day.at("19:52", "Asia/Bishkek").do(hello_world)
