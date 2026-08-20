class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(starts):
            visited = [[False] * cols for _ in range(rows)]
            stack = []

            for r, c in starts:
                if not visited[r][c]:
                    visited[r][c] = True
                    stack.append((r, c))

            while stack:
                r, c = stack.pop()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and not visited[nr][nc]
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        visited[nr][nc] = True
                        stack.append((nr, nc))

            return visited

        pacific_starts = (
            [(r, 0) for r in range(rows)]
            + [(0, c) for c in range(cols)]
        )

        atlantic_starts = (
            [(r, cols - 1) for r in range(rows)]
            + [(rows - 1, c) for c in range(cols)]
        )

        pacific = dfs(pacific_starts)
        atlantic = dfs(atlantic_starts)

        res = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])

        return res