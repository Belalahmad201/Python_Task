# Stock Profit Analyzer

prices = [7, 1, 5, 3, 6, 4]

min_price = prices[0]
max_profit = 0
buy_day = 0
sell_day = 0
temp_buy_day = 0

for i in range(1, len(prices)):

    # Find minimum buying price
    if prices[i] < min_price:
        min_price = prices[i]
        temp_buy_day = i

    # Calculate profit
    profit = prices[i] - min_price

    # Update maximum profit
    if profit > max_profit:
        max_profit = profit
        buy_day = temp_buy_day
        sell_day = i

print("Stock Prices:", prices)
print("Maximum Profit:", max_profit)
print("Buy on Day:", buy_day + 1)
print("Sell on Day:", sell_day + 1)