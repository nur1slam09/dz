from aiogram import Bot, Dispatcher, types, executor
from logging import basicConfig, INFO
from bs4 import BeautifulSoup
import requests

bot = Bot(token = "7080382498:AAGqqqK7LjXRfqTQKDs_1YNiqif_nxn_pM0")
dp = Dispatcher(bot)
basicConfig(level=INFO)


@dp.message_handler(commands="start")
async def start(message:types.Message):
    await message.answer("HELLO")
    
@dp.message_handler(commands="parsing")
async def start(message:types.Message):
    await message.answer("start parsing")
    
    url = 'https://new.vizitka.kg/blog'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.find_all('div', class_='tp-product-tag-2')
    prices = soup.find_all('span', class_='tp-product-price-2 new-price')
    # print(titles).
    
    for title, price in zip(titles, prices):
        true_price = ''.join(price.text.split())
        await message.answer(f"{title.text} - {true_price} \n")  
        
executor.start_polling(dp)