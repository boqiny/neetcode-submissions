class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[0][0] dp[0][1] dp[0][2] dp[0][3] dp[0][4]
        # x        dp[1][1] dp[1][2] dp[1][3] dp[1][4]
        # x        x        dp[2][2] dp[2][3] dp[2][4]
        # x        x        x        dp[3][3] dp[3][4]
        # x        x        x        x        dp[4][4]
        
        # dp[i][j] = if s[i:j] is palindrome
        # dp[i][j] = True if s[i] == s[j] and dp[i+1][j-1] (j-i >= 1)
        n = len(s)
        count = 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j or (s[i] == s[j] and (j-i < 2 or dp[i+1][j-1])):
                    dp[i][j] = True
                    count += 1
        return count
                