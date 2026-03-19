import argparse
from bot.client import BinanceClient
from bot.orders import OrderService
from bot.logging_config import setup_logger

# 🔑 Replace with your actual testnet keys
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET_KEY"


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    logger = setup_logger()

    try:
        client = BinanceClient(API_KEY, API_SECRET)
        service = OrderService(client, logger)

        response = service.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n✅ Order Placed Successfully")
        print(response)

    except Exception as e:
        logger.error(str(e))
        print("❌ Error:", str(e))


if __name__ == "__main__":
    main()