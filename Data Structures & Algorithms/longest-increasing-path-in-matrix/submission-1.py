class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m, n = len(matrix), len(matrix[0])
        memo = {}

        def dfs(r,c) -> int:
            if (r, c) in memo:
                return memo[(r, c)]
            best = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            memo[(r, c)] = best
            return best
        
        longest = 0

        for r in range(m):
            for c in range(n):
                longest = max(longest, dfs(r, c))
        return longest

