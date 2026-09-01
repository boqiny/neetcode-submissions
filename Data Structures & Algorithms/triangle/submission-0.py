class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # memo = [[0] * len(triangle[r]) for r in range(len(triangle))]
        # INF = float("inf")
        # for r in range(len(triangle)):
        #     for c in range(len(triangle[r])):
        #         memo[r][c] = INF
        # # Min path sum from position (row, col) to the bottom of the triangle
        # def dfs(row, col) -> int: 
        #     if row >= len(triangle):
        #         return 0
        #     if memo[row][col] != INF:
        #         return memo[row][col]
        #     memo[row][col] = triangle[row][col] + min(dfs(row+1,col), dfs(row+1,col+1))
        #     return memo[row][col]
        
        # return dfs(0,0)
        
        # dp[row][col]` = minimum path sum from position `(row, col)` to the bottom
        n = len(triangle)
        dp = [[0] * len(triangle[r]) for r in range(n)]
        for col in range(len(triangle[n-1])):
            dp[n-1][col] = triangle[n-1][col]
        for row in range(n-2, -1, -1):
            for col in range(len(triangle[row])):
                dp[row][col] = triangle[row][col] + min(
                    dp[row+1][col],     # down-left
                    dp[row+1][col+1]    # down-right
                )
        return dp[0][0]



            
