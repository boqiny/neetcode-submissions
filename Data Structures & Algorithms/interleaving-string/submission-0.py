class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp[i][j] := s3[:i+j] can be represented by s1[:i] + s2[:j]
        if len(s1) + len(s2) != len(s3):
            return False
        m, n = len(s1), len(s2)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            if dp[i-1][0] and s1[i-1] == s3[i-1]:
                dp[i][0] = True
        
        for i in range(1, n+1):
            if dp[0][i-1] and s2[i-1] == s3[i-1]:
                dp[0][i] = True
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s2[j-1] == s3[i+j-1] and dp[i][j-1]:
                    dp[i][j] = True
                elif s1[i-1] == s3[i+j-1] and dp[i-1][j]:
                    dp[i][j] = True
        return dp[m][n]
                

        
    