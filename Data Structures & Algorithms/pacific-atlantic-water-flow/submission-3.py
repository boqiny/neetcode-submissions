class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(0,1), (0,-1), (-1,0), (1,0)]

        def bfs(starts):
            visited = set(starts)
            q = deque(starts)
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n
                            and (nr, nc) not in visited
                            and heights[nr][nc] >= heights[r][c]):
                                visited.add((nr,nc))
                                q.append((nr,nc))
            return visited
        
        pacific = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
        atlantic = [(m-1, j) for j in range(n)] + [(i, n-1) for i in range(m)]
        print(bfs(pacific) & bfs(atlantic))
        return [list(x) for x in bfs(pacific) & bfs(atlantic)]
