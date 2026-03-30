from fastapi import FastAPI
import requests

app = FastAPI()

# 🔧 TOOL
def get_crypto_price(coin):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
        response = requests.get(url, timeout=5).json()
        return response.get(coin, {}).get("usd", None)
    except:
        return None

# 🤖 AGENT
def crypto_agent(user_input):
    coins = ["bitcoin", "ethereum", "dogecoin"]

    for coin in coins:
        if coin in user_input.lower():
            price = get_crypto_price(coin)

            if price:
                return f"💰 The current price of {coin} is ${price}. This data is fetched from an external API."

            return "⚠️ Could not fetch price."

    return "👉 Ask about Bitcoin, Ethereum, or Dogecoin."

# 🔗 API
@app.get("/")
def home(query: str):
    return {"response": crypto_agent(query)}
