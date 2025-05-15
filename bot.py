# bot.py
from binance.client import Client
from binance.enums import *
from config import API_KEY, API_SECRET, BASE_URL
from logger import setup_logger

class BasicBot:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = BASE_URL
        self.logger = setup_logger()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=price
                )
            elif order_type == 'STOP_MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_STOP_MARKET,
                    stopPrice=price,
                    quantity=quantity
                )
            else:
                return "Invalid order type."

            self.logger.info(f"Order placed: {order}")
            return order

        except Exception as e:
            self.logger.error(f"Error placing order: {e}")
            return f"Failed to place order: {e}"
