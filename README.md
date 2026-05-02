## Architecture

This project simulates an AI Agent using an Agent Development Kit (ADK) pattern.

- The agent function acts as the decision-making unit.
- A tool layer (MCP-style) connects to an external API (CoinGecko).
- The agent invokes the tool to retrieve real-time data.
- The final response is generated using the retrieved data.

This demonstrates tool usage and external data integration as required.

## Features

- 🚀 **Web-based UI** - Modern, responsive chat interface
- 💰 **Real-time Crypto Prices** - Query Bitcoin, Ethereum, or Dogecoin prices
- ⚡ **Fast Response** - Instant price lookups from CoinGecko API
- 📱 **Mobile Friendly** - Works on desktop, tablet, and mobile devices

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd crypto-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Agent

1. Start the FastAPI server:
```bash
uvicorn main:app --reload
```

2. Open your browser and navigate to:
```
http://localhost:8000
```

3. Start chatting with the crypto agent! Ask about Bitcoin, Ethereum, or Dogecoin prices.

### Using the API Directly

You can also query the API endpoint directly:
```bash
curl "http://localhost:8000/api/chat?query=What%20is%20the%20price%20of%20Bitcoin"
```

## Project Structure

```
crypto-agent/
├── main.py           # FastAPI backend & agent logic
├── index.html        # Web UI frontend
├── requirements.txt  # Python dependencies
├── Dockerfile        # Docker configuration
└── README.md        # This file
```

## Technologies Used

- **FastAPI** - Web framework
- **Uvicorn** - ASGI server
- **Requests** - HTTP client for API calls
- **CoinGecko API** - Real-time cryptocurrency data
- **HTML/CSS/JavaScript** - Frontend UI
