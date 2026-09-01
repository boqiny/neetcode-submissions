class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left_min = prices[0]
        for i in range(1, len(prices)):
            left_min = min(prices[i-1], left_min)
            max_profit = max(max_profit, prices[i] - left_min)
        return max_profit