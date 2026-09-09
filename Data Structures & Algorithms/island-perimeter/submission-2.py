class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        perimeter = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        nr < 0 or nr >= m or
                        nc < 0 or nc >= n or
                        grid[nr][nc] == 0
                    ):
                        perimeter += 1

        return perimeter