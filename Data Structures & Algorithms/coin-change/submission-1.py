class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[x] := minimum # of coins to reach amout x
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for x in range(1, amount + 1):
            for c in coins:
                if c <= x:
                    dp[x] = min(dp[x], 1 + dp[x-c])
        return -1 if dp[amount] == float('inf') else dp[amount]