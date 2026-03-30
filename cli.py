import argparse
import os
from dotenv import load_dotenv

from bot.client import BinanceClient
from bot.orders import OrderService
from bot.logging_config import setup_logger

# Load environment variables
load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
BASE_URL = os.getenv("BINANCE_BASE_URL")


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    # Order arguments
    parser.add_argument("--symbol")
    parser.add_argument("--side", choices=["BUY", "SELL"])
    parser.add_argument("--type", choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float)
    parser.add_argument("--price", type=float)

    # Debug / utility commands
    parser.add_argument("--ping", action="store_true", help="Check Binance API connectivity")
    parser.add_argument("--account", action="store_true", help="Get futures account info")
    parser.add_argument("--open-orders", action="store_true", help="List open orders for symbol")
    parser.add_argument("--cancel-order-id", type=int, help="Cancel order by ID")

    args = parser.parse_args()

    logger = setup_logger()

    try:
        if not API_KEY or not API_SECRET:
            raise ValueError("API keys not found. Please configure your .env file")

        client = BinanceClient(API_KEY, API_SECRET, BASE_URL)
        service = OrderService(client, logger)

        # ---- Debug Commands ----

        if args.ping:
            print("🔄 Checking API connectivity...")
            print(client.ping())
            return

        if args.account:
            print("📊 Account Information")
            print(client.get_account())
            return

        if args.open_orders:
            if not args.symbol:
                raise ValueError("Symbol required for open orders")
            print("📂 Open Orders")
            print(client.get_open_orders(args.symbol))
            return

        if args.cancel_order_id:
            if not args.symbol:
                raise ValueError("Symbol required to cancel order")
            print("❌ Cancelling Order...")
            print(client.cancel_order(args.symbol, args.cancel_order_id))
            return

        # ---- Place Order ----

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