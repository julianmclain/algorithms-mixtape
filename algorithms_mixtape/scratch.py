def maxProfit(prices) -> int:
    if not prices:
        return 0

    i = 0
    maxprofit = 0
    valley = prices[0]
    peak = prices[0]

    while i < len(prices) - 1:
        while i < len(prices) - 1 and prices[i] > prices[i + 1]:
            i += 1
        valley = prices[i]
        while i < len(prices) - 1 and prices[i] < prices[i + 1]:
            i += 1
        peak = prices[i]
        maxprofit += peak - valley

    return maxprofit


print(maxProfit([7, 1, 5, 3, 6, 4]))
