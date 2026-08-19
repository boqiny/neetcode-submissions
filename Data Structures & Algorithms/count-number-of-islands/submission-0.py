class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1. start ->  dfs/bfs -> enumerate 4 directions -> check boundary -> continue search
        rows, cols = len(grid), len(grid[0])
        visited = [[0] * cols for _ in range(rows)]

        def dfs(r, c) -> None:
            if (r < 0 or r >= rows
            or c < 0 or c >= cols or visited[r][c] == 1 or grid[r][c] != '1'):
                return
            
            visited[r][c] = 1
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 0 and grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
            