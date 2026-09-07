class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][state] = max profit can reach at ith day with j: hold, sold, rest
        n = len(prices)
        dp = [[float('-inf')] * 3 for _ in range(n)]
        dp[0][0] = -prices[0]   # hold: 第0天买入
        dp[0][1] = 0            # sold: 第0天没东西可卖，给0即可
        dp[0][2] = 0            # rest: 什么都没做
        for i in range(1, n):
                dp[i][0] = max(dp[i-1][2] - prices[i], dp[i-1][0])
                dp[i][1] = dp[i-1][0] + prices[i]
                dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[n-1])