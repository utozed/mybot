# bot.py

import time
from binance.client import Client

# Use your testnet API keys here
api_key = "xkH4hAfCyzcRwbj76s6fNQ1qCyYAXBIuZKEA9FGDh4tU8ZSmzIyHHS90JVR1C6ic"
secret_key = "DElmXpGWmwmIbi43Rjmqgnlrq2optY6nbrZV9hJke5Wtg2ioQG4Q87iSg8kQj5IJ"

# Connect to Binance Testnet
client = Client(api_key, secret_key)
client.API_URL = "https://testnet.binance.vision/api"  # Important for testnet

symbol = "XRPUSDT"

def get_price():
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])

def main():
    print("🚀 Signal Bot Started for", symbol)
    previous_price = get_price()

    while True:
        current_price = get_price()
        print(f"🔄 Current price: {current_price}")

        if current_price > previous_price:
            print("📈 Signal: BUY")
        elif current_price < previous_price:
            print("📉 Signal: SELL")
        else:
            print("⏸️ Signal: WAIT")

        previous_price = current_price
        time.sleep(10)  # Wait 10 seconds before next check

if __name__ == "__main__":
    main()
