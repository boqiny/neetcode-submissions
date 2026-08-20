class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0,1), (0,-1),(-1,0),(1,0)]
        # DFS using stack
        stack = []
        sheld = set()
        for r in range(rows):
            for c in (0, cols - 1):
                if board[r][c] == 'O':
                    stack.append((r,c))
                    sheld.add((r,c))
        for c in range(1, cols-1):
            for r in (0, rows - 1):
                if board[r][c] == 'O':
                    stack.append((r,c))
                    sheld.add((r,c))
        while stack:
            cur = stack.pop()
            for dr, dc in directions:
                r, c = dr + cur[0], dc + cur[1]
                if (0 <= r < rows and 0 <= c < cols and board[r][c] == 'O' and (r,c) not in sheld):
                    sheld.add((r,c))
                    stack.append((r,c))
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r,c) not in sheld:
                    board[r][c] = 'X'

        


