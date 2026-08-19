class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS using stack
        rows, cols = len(grid), len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    stack = [(i,j)]
                    count += 1
                    while stack:
                        cur = stack.pop()
                        r, c = cur[0], cur[1]
                        if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1'):
                            continue
                        grid[r][c] = '0'
                        stack.append((r-1, c))
                        stack.append((r+1, c))
                        stack.append((r, c-1))
                        stack.append((r, c+1))
        return count
