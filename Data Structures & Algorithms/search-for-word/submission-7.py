class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(-1,0), (1,0), (0,1), (0,-1)] 
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c, i) -> bool:

            if i == len(word):
                return True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and board[nr][nc] == word[i]:
                    visited[nr][nc] = True
                    if dfs(nr, nc, i + 1):
                        return True
                    visited[nr][nc] = False
            
            return False
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    visited[r][c] = True
                    if dfs(r, c, 1):
                        return True
                    visited[r][c] = False
        return False
                
            