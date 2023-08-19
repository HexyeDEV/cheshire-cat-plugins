import requests
from cat.mad_hatter.decorators import tool, hook

@tool
def get_bitcoin(tool_input, cat):
    """Retrieves the current price of bitcoin in USD. Use it whenever needed to know the current price of bitcoin. Never get this information from long term memory. Input is always None."""
    r = requests.get("https://api.blockchain.com/v3/exchange/tickers/BTC-USD")
    p = r.json()["last_trade_price"]
    return f"${p}"

@tool
def get_ethereum(tool_input, cat):
    """Retrieves the current price of ethereum in USD. Use it whenever needed to know the current price of ethereum. Never get this information from long term memory. Input is always None."""
    r = requests.get("https://api.blockchain.com/v3/exchange/tickers/ETH-USD")
    p = r.json()["last_trade_price"]
    return f"${p}"

@tool
def get_litecoin(tool_input, cat):
    """Retrieves the current price of litecoin in USD. Use it whenever needed to know the current price of litecoin. Never get this information from long term memory. Input is always None."""
    r = requests.get("https://api.blockchain.com/v3/exchange/tickers/LTC-USD")
    p = r.json()["last_trade_price"]
    return f"${p}"

@tool
def get_doge(tool_input, cat):
    """Retrieves the current price of dogecoin in USD. Use it whenever needed to know the current price of dogecoin. Never get this information from long term memory. Input is always None."""
    r = requests.get("https://api.blockchain.com/v3/exchange/tickers/DOGE-USD")
    p = r.json()["last_trade_price"]
    return f"${p}"

@tool
def get_tron(tool_input, cat):
    """Retrieves the current price of tron in USD. Use it whenever needed to know the current price of tron. Never get this information from long term memory. Input is always None."""
    r = requests.get("https://api.blockchain.com/v3/exchange/tickers/TRX-USD")
    p = r.json()["last_trade_price"]
    return f"${p}"

@tool
def get_ripple(tool_input, cat):
    """Retrieves the current price of ripple in USD. Use it whenever needed to know the current price of ripple. Never get this information from long term memory. Input is always None."""
    r = requests.get("https://api.blockchain.com/v3/exchange/tickers/XRP-USD")
    p = r.json()["last_trade_price"]
    return f"${p}"

@tool
def get_bitcoin_cash(tool_input, cat):
    """Retrieves the current price of bitcoin cash in USD. Use it whenever needed to know the current price of bitcoin cash. Never get this information from long term memory. Input is always None."""
    r = requests.get("https://api.blockchain.com/v3/exchange/tickers/BCH-USD")
    p = r.json()["last_trade_price"]
    return f"${p}"

@tool
def get_stellar(tool_input, cat):
    """Retrieves the current price of stellar in USD. Use it whenever needed to know the current price of stellar. Never get this information from long term memory. Input is always None."""
    r = requests.get("https://api.blockchain.com/v3/exchange/tickers/XLM-USD")
    p = r.json()["last_trade_price"]
    return f"${p}"

@tool
def get_tether(tool_input, cat):
    """Retrieves the current price of tether in USD. Use it whenever needed to know the current price of tether. Never get this information from long term memory. Input is always None."""
    r = requests.get("https://api.blockchain.com/v3/exchange/tickers/USDT-USD")
    p = r.json()["last_trade_price"]
    return f"${p}"

@tool
def get_cardano(tool_input, cat):
    """Retrieves the current price of cardano in USD. Use it whenever needed to know the current price of cardano. Never get this information from long term memory. Input is always None."""
    r = requests.get("https://api.blockchain.com/v3/exchange/tickers/ADA-USD")
    p = r.json()["last_trade_price"]
    return f"${p}"
