import yfinance as yf
from . import config

def get_price_data(symbol):
    try:
        Ticker = yf.Ticker(symbol)
        history = Ticker.history(period="1d", interval="15m")
        print(history["Close"]) 
        latest_close = history["Close"].iloc[-1]
        second_latest_close = history["Close"].iloc[-2]
        print(f"Latest close price: {latest_close}")
        print(f"Second latest close is: {second_latest_close}")
    except Exception as e:
        print(f"error fetching data:{e}")
