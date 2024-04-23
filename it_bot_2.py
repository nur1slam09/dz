from aiogram import Bot, Dispatcher, types, executor
from config import token
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging, time, sqlite3, requests, datetime
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

bot = Bot(token=token)
memory = MemoryStorage()
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def start(message:types.Message):
    await message.answer("Валюта")
    
    url = "https://www.nbkr.kg/index.jsp?lang=RUS"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    usd = soup.find('td', class_="exrate").text
    rub = soup.find_all('td', class_="exrate")[1].text
    euro = soup.find_all('td', class_="exrate")[2].text
    kzt = soup.find_all('td', class_="exrate")[3].text
    
    await message.answer(f"Время: {time}\nВалюта:\nРубль - {rub}\nЕвро - {euro}\nДоллар - {usd}\nТенге - {kzt}\n")
