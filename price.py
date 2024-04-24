
import requests

def get_costco_stock_price():
    url = "https://query1.finance.yahoo.com/v8/finance/chart/COST"
    params = {
        "range": "1d",
        "interval": "1m"
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Extracting the current price
    current_price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]

    return current_price

if __name__ == "__main__":
    costco_price = get_costco_stock_price()
    print("Current price of Costco stock: $", costco_price)

