from bot.validators import validate_inputs

class OrderService:
    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def place_order(self, symbol, side, order_type, quantity, price=None):
        validate_inputs(symbol, side, order_type, quantity, price)

        self.logger.info(f"Placing order: {symbol}, {side}, {order_type}")

        if order_type == "MARKET":
            response = self.client.market_order(symbol, side, quantity)
        else:
            response = self.client.limit_order(symbol, side, quantity, price)

        self.logger.info(f"Response: {response}")
        return response