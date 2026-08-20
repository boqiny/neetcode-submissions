class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        max_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue
                # DFS using stack
                stack = [(i,j)]
                grid[i][j] = 0
                count = 1
                while stack:
                    cur = stack.pop()
                    for dr, dc in directions:
                        r, c = cur[0] + dr, cur[1] + dc
                        if (0 <= r < rows and 0 <= c < cols and grid[r][c] != 0):
                            grid[r][c] = 0
                            stack.append((r,c))
                            count += 1
                max_count = max(max_count, count)
        return max_count
                
                    
