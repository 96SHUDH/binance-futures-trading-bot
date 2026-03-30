import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bot.validators import validate_inputs


def test_valid_market_order():
    # should pass without error
    validate_inputs("BTCUSDT", "BUY", "MARKET", 0.01, None)


def test_invalid_side():
    with pytest.raises(ValueError):
        validate_inputs("BTCUSDT", "INVALID", "MARKET", 0.01, None)


def test_invalid_quantity():
    with pytest.raises(ValueError):
        validate_inputs("BTCUSDT", "BUY", "MARKET", 0, None)


def test_limit_order_without_price():
    with pytest.raises(ValueError):
        validate_inputs("BTCUSDT", "BUY", "LIMIT", 0.01, None)


def test_valid_limit_order():
    validate_inputs("BTCUSDT", "SELL", "LIMIT", 0.01, 68000)