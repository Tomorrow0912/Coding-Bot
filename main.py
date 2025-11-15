from src import get_price
from src import config

symbol = input("Enter ticker: ").strip()
if symbol == "":
    symbol = config.DEFAULT_TICKER

data=get_price.get_price_data(symbol)

print(data)
