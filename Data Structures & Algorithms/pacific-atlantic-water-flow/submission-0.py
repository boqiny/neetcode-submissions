class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        pacific = [[0] * cols for _ in range(rows)]
        atlantic = [[0] * cols for _ in range(rows)]
        # DFS using stack
        stack = []
        for i in range(rows):
            stack.append((i, 0))
            pacific[i][0] = 1
        for j in range(1, cols):
            stack.append((0, j))
            pacific[0][j] = 1

        while stack:
            cur = stack.pop()
            for dr, dc in directions:
                r, c = dr+cur[0], dc+cur[1]
                if (0 <= r < rows and 0 <= c < cols and pacific[r][c] == 0 and heights[r][c] >= heights[cur[0]][cur[1]]):
                    pacific[r][c] = 1
                    stack.append((r,c))

        print(pacific)

        for i in range(rows):
            stack.append((i, cols-1))
            atlantic[i][cols-1] = 1
        for j in range(cols-1):
            stack.append((rows-1, j))
            atlantic[rows-1][j] = 1
        while stack:
            cur = stack.pop()
            for dr, dc in directions:
                r, c = dr+cur[0], dc+cur[1]
                if (0 <= r < rows and 0 <= c < cols and atlantic[r][c] == 0 and heights[r][c] >= heights[cur[0]][cur[1]]):
                    atlantic[r][c] = 1
                    stack.append((r,c))
        print(atlantic)
        res = []
        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] == atlantic[i][j] == 1:
                    res.append([i,j])
        return res






