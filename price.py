def max_profit(prices):
    min_price = float('inf')  # Initialize to a very high value
    max_profit = 0  # Initialize to 0 as no profit is better than any negative profit
    
    for price in prices:
        if price < min_price:
            min_price = price  # Update min_price if the current price is lower
        elif price - min_price > max_profit:
            max_profit = price - min_price  # Update max_profit if current profit is higher
    
    return max_profit

# Test Case 1
prices1 = [7, 1, 5, 3, 6, 4]
print("Output:", max_profit(prices1))  # Output: 5

# Test Case 2
prices2 = [7, 6, 4, 3, 1]
print("Output:", max_profit(prices2))  # Output: 0

