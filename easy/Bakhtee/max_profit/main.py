def maxProfit(prices) -> int:
    max_val = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[j] - prices[i] > max_val:
                max_val = prices[j] - prices[i]
    return max_val
