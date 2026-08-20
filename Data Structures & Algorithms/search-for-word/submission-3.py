class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        visited = [[False] * cols for _ in range(rows)]
        
        def dfs(r, c, i) -> bool:
            if i == len(word):
                return True
            if (
                r < 0 or r >= rows
                or c < 0 or c >= cols
                or board[r][c] != word[i]
            ):
                return False
            temp = board[r][c]
            board[r][c] = "#"
            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1):
                    return True
            board[r][c] = temp   # backtrack：恢复
            return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False

                        

                    



