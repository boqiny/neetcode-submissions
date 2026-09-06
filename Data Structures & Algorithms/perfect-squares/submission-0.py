class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] := min # of perfect square to sum up to i
        # dp[i] = min(dp[i], dp[i-x**2] + 1)
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        ceil = math.floor(math.sqrt(n))
        for i in range(1, n+1):
            for x in range(1, ceil+1):
                if i - x**2 >= 0:
                    dp[i] = min(dp[i], dp[i-x**2] + 1)
        return dp[-1]
