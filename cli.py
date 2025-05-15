# cli.py
from bot import BasicBot

def get_user_input():
    symbol = input("Enter symbol (e.g., BTCUSDT): ").strip().upper()
    side = input("Enter side (BUY or SELL): ").strip().upper()
    order_type = input("Enter order type (MARKET, LIMIT, STOP_MARKET): ").strip().upper()
    quantity = float(input("Enter quantity: ").strip())
    price = None
    if order_type in ['LIMIT', 'STOP_MARKET']:
        price = input("Enter price: ").strip()
        price = float(price)

    return symbol, side, order_type, quantity, price

if __name__ == '__main__':
    bot = BasicBot()
    symbol, side, order_type, quantity, price = get_user_input()
    result = bot.place_order(symbol, side, order_type, quantity, price)
    print("Order Result:\n", result)
