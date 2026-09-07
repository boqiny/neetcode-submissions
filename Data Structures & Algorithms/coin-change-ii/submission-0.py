class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] := # of combinations that sum up to i
        # dp[i] += dp[i-x] for x in coins if i-x>=0
        dp = [0] * (amount + 1)
        dp[0] = 1
        for x in coins:
            for i in range(1, amount + 1):
                if i-x >= 0:
                    dp[i] += dp[i-x]
        return dp[-1]
