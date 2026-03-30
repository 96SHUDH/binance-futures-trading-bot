from binance.client import Client

class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    # Market order
    def market_order(self, symbol, side, quantity):
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
    # Limit Order
    def limit_order(self, symbol, side, quantity, price):
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )
    # PING API (Check connection)
    def ping(self):
        return self.client.ping()
    
    #GET ACCOUNT INFO
    def get_account(self):
        return self.client.futures_account()
    
    # GET OPEN ORDERS
    def get_open_orders(self, symbol):
        return self.client.futures_get_open_orders(symbol=symbol)
    
    # CANCEL ORDER
    def cancel_order(self, symbol, order_id):
        return self.client.futures_cancel_order(
            symbol=symbol,
            orderId=order_id
        )