class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # dp[i] := 从第 i 颗石头开始、轮到谁先手，先手比后手最多能多得的分数
        n = len(stoneValue)
        s = stoneValue + [0, 0, 0]
        dp = [0] * (n + 3)
        for i in range(n - 1, -1, -1):
            take1 = s[i] - dp[i+1]
            take2 = s[i] + s[i+1] - dp[i+2]
            take3 = s[i] + s[i+1] + s[i+2] - dp[i+3]
            dp[i] = max(take1, take2, take3)
        if dp[i] > 0:
            return "Alice"
        elif dp[i] == 0:
            return "Tie"
        else:
            return "Bob"