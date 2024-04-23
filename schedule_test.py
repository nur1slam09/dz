import schedule, time, requests

def hello_world():
    print(f"Hello World {time.ctime()}")
    
# def backend_16_1B():
#     print(f"Здравствуйте, сегодня у вас урок в 19")

def get_btc_price():
    response = requests.get('https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
    price = ['price']
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"Цена биткоина на {current_time}: {price}$")

# schedule.every().monday.at('19:56').do(backend_16_1B)
schedule.every(1).seconds.do(get_btc_price)

def get_eth_price():
    response = requests.get('https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
    data = response.json()
    price = data['price']
    current_time = time.strftime

while True:
    schedule.run_pending()
    time.sleep(1)
    
    