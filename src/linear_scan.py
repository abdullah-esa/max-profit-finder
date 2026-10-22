# src/linear_scan.py

def max_profit_linear(prices):
    """Linear pass on raw price list to find max profit, buy day, and sell day in O(N)."""
    min_price = float('inf')
    max_profit = 0
    best_buy_idx = 0
    best_sell_idx = 0
    min_idx = 0

    for i, price in enumerate(prices):
        if price < min_price:
            min_price = price
            min_idx = i

        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
            best_buy_idx = min_idx
            best_sell_idx = i

    return best_buy_idx, best_sell_idx, max_profit