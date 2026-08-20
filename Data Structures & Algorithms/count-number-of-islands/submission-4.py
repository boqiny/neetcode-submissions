from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS using queue
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != '1':
                    continue
                count += 1
                q = deque([(i,j)])
                while q:
                    cur = q.popleft()
                    r, c = cur[0], cur[1]
                    if  (
                           r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1'
                        ):
                        continue
                    grid[r][c] = '0'
                    for dr, dc in directions:
                        q.append((r+dr, c+dc))
        return count        
            

