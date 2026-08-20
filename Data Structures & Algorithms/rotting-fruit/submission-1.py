from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        max_time = 0
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j,0))

        while q:
            cur = q.popleft()
            max_time = max(max_time, cur[2])
            for dr, dc in directions:
                r, c = dr + cur[0], dc + cur[1]
                if (0 <= r < rows and 0 <= c < cols and grid[r][c] == 1):
                    grid[r][c] = 2
                    q.append((r,c,cur[2]+1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return max_time
        

                    