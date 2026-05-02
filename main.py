from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import requests
import os

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔧 TOOL
def get_crypto_price(coin):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true"
        response = requests.get(url, timeout=5).json()
        coin_data = response.get(coin, {})
        
        return {
            "price": coin_data.get("usd"),
            "change_24h": coin_data.get("usd_24h_change"),
            "market_cap": coin_data.get("usd_market_cap")
        }
    except:
        return None

# 🤖 AGENT
def crypto_agent(user_input):
    coins = ["bitcoin", "ethereum", "dogecoin"]

    for coin in coins:
        if coin in user_input.lower():
            data = get_crypto_price(coin)

            if data and data["price"]:
                price = data["price"]
                change_24h = data.get("change_24h", 0)
                
                # Determine trend emoji
                trend_emoji = "📈" if change_24h >= 0 else "📉"
                change_text = f"{change_24h:+.2f}%" if change_24h is not None else "N/A"
                
                return f"💰 {coin.capitalize()}: ${price:,.2f}\n{trend_emoji} 24h Change: {change_text}\nℹ️ Data from CoinGecko API"

            return "⚠️ Could not fetch price."

    return "👉 Ask about Bitcoin, Ethereum, or Dogecoin."

# 🔗 API Routes
@app.get("/api/chat")
def chat(query: str):
    return {"response": crypto_agent(query)}

# Serve the frontend
@app.get("/")
async def serve_frontend():
    return FileResponse("index.html", media_type="text/html")
