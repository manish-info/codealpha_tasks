# Stock Portfolio Tracking Tool (Full Implementation)

## Backend (using Flask and a stock API like Alpha Vantage)

# 1. Install the required packages:
# pip install Flask requests

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your API key from Alpha Vantage or any stock API
API_KEY = 'YOUR_API_KEY'
API_URL = 'https://www.alphavantage.co/query'

# In-memory database for storing portfolio
portfolio = {}

# Route to add a stock to the portfolio
@app.route('/add_stock', methods=['POST'])
def add_stock():
    data = request.json
    symbol = data['symbol'].upper()
    quantity = data['quantity']
    purchase_price = data['purchase_price']

    if symbol in portfolio:
        portfolio[symbol]['quantity'] += quantity
        portfolio[symbol]['purchase_price'] = purchase_price
    else:
        portfolio[symbol] = {'quantity': quantity, 'purchase_price': purchase_price}

    return jsonify({'message': 'Stock added successfully', 'portfolio': portfolio})

# Route to remove a stock from the portfolio
@app.route('/remove_stock', methods=['POST'])
def remove_stock():
    data = request.json
    symbol = data['symbol'].upper()

    if symbol in portfolio:
        del portfolio[symbol]
        return jsonify({'message': 'Stock removed successfully', 'portfolio': portfolio})
    else:
        return jsonify({'error': 'Stock not found'}), 404

# Route to get the current portfolio with real-time data
@app.route('/get_portfolio', methods=['GET'])
def get_portfolio():
    result = {}
    total_value = 0

    for symbol, details in portfolio.items():
        response = requests.get(API_URL, params={
            'function': 'GLOBAL_QUOTE',
            'symbol': symbol,
            'apikey': API_KEY
        })
        data = response.json()

        if 'Global Quote' in data:
            current_price = float(data['Global Quote']['05. price'])
            quantity = details['quantity']
            purchase_price = details['purchase_price']
            total_stock_value = current_price * quantity

            result[symbol] = {
                'quantity': quantity,
                'purchase_price': purchase_price,
                'current_price': current_price,
                'total_stock_value': total_stock_value,
                'gain_loss': total_stock_value - (purchase_price * quantity)
            }

            total_value += total_stock_value

    return jsonify({'portfolio': result, 'total_portfolio_value': total_value})

if __name__ == '__main__':
    app.run(debug=True)
