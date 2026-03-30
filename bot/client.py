from binance.client import Client


class BinanceClient:
    def __init__(self, api_key, api_secret, base_url):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = f"{base_url}/fapi"

    # MARKET ORDER
    def market_order(self, symbol, side, quantity):
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

    # LIMIT ORDER
    def limit_order(self, symbol, side, quantity, price):
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )

    # API connectivity test
    def ping(self):
        return self.client.ping()

    # Get futures account info
    def get_account(self):
        return self.client.futures_account()

    # Get open orders
    def get_open_orders(self, symbol):
        return self.client.futures_get_open_orders(symbol=symbol)

    # Cancel order
    def cancel_order(self, symbol, order_id):
        return self.client.futures_cancel_order(
            symbol=symbol,
            orderId=order_id
        )