class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] = if s[j:i] is palindrome
        # if s[i] == s[j] and dp[i-1][j+1] (if exist) => dp[i][j] = True
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        # dp[0][0]
        # dp[1][0] dp[1][1]
        # dp[2][0] dp[2][1] dp[2][2]
        # dp[3][0] dp[3][1] dp[3][2] dp[3][3]
        # dp[4][0] dp[4][1] dp[4][2] dp[4][3] dp[4][4]
        for i in range(n):
            for j in range(i, -1, -1):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j] and (i - j < 2 or dp[i-1][j+1]):
                    dp[i][j] = True

        longest, l, r = 0, 0, 0

        for i in range(n):
            for j in range(n):
                if dp[i][j] == True:
                    if longest < i-j+1:
                        longest = i-j+1
                        l = j
                        r = i
        return s[l:r+1]

