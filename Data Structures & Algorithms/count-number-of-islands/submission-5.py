from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] != '1':
                    continue

                # found a new island
                count += 1

                q = deque([(i, j)])
                grid[i][j] = '0'   # mark when enqueue

                while q:
                    r, c = q.popleft()

                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc

                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == '1'
                        ):
                            grid[nr][nc] = '0'
                            q.append((nr, nc))

        return count