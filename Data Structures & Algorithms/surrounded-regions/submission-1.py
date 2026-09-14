class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        directions = [(0,1), (0,-1), (-1,0), (1,0)]

        q = deque()
        for i in range(m):
            for j in range(n):
                if (i in (0, m-1) or j in (0, n-1)) and board[i][j] == 'O':
                    board[i][j] = '#'
                    q.append((i, j))
        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    board[nr][nc] = '#'
                    q.append((nr,nc))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"
        

                