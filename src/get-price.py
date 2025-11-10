import yfinance as yf
import config

try:
    symbol = input("Enter ticker: ").strip()
    if symbol == "":
        symbol = config.DEFAULT_TICKER
    Ticker = yf.Ticker(symbol)
    history = Ticker.history(period="1d", interval="15m")
    print(history["Close"])  # This prints all close prices in that period
    latest_close = history["Close"].iloc[-1]
    second_latest_close = history["Close"].iloc[-2]
    print(f"Latest close price: {latest_close}")
    print(f"Second latest close is: {second_latest_close}")
except Exception as e:
    print(f"error fetching data:{e}")
