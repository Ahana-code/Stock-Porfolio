from flask import Flask, render_template, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import requests
import os

app = Flask(__name__)
app.secret_key = 'anisecretportfolio'  #Strong secret key

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Alpha Vantage API Key 
API_KEY = "FEBEKZHB9MJNG576."

# List of stock symbols to track
stocks =[
    {"name": "Apple", "symbol": "AAPL", "price": 232.62, "change": 1.5},
    {"name": "Tesla", "symbol": "TSLA", "price": 328.50, "change": -2.3},
    {"name": "Google", "symbol": "GOOGL", "price": 185.23, "change": 0.8},
    {"name": "Microsoft", "symbol": "MSFT", "price": 411.44, "change": -1.2},
    {"name": "Amazon", "symbol": "AMZN", "price": 232.76, "change": 3.6},
    {"name": "Meta (Facebook)", "symbol": "META", "price": 719.80, "change": -0.9},
    {"name": "Netflix", "symbol": "NFLX", "price": 1008.08, "change": 2.1},
    {"name": "NVIDIA", "symbol": "NVDA", "price": 132.80, "change": 4.5},
    {"name": "AMD", "symbol": "AMD", "price": 111.10, "change": -1.7},
    {"name": "Visa", "symbol": "V", "price": 350.72, "change": 0.5},
    {"name": "Johnson & Johnson", "symbol": "JNJ", "price": 156.13, "change": -0.4},
    {"name": "Alibaba", "symbol": "BABA", "price": 112.78, "change": 1.2}
]

# Function to fetch stock prices
def get_stock_prices():
    stock_data = []
    for stock in stocks:
        symbol = stock["symbol"]
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
        response = requests.get(url).json()
        price = response.get("Global Quote", {}).get("05. price", "N/A")
        stock_data.append({
            "name": stock["name"],
            "symbol": stock["symbol"],
            "price": price
        })
    return stock_data

@app.route("/")
def index():
    return render_template("index.html", stocks=stocks)

if __name__ == "__main__":
    app.run(debug=True)
