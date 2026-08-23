class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        visited = [[False] * cols for _ in range(rows)]
        
        def dfs(r, c, i) -> bool:
            if i == len(word):
                return True
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                visited[r][c] or
                board[r][c] != word[i]
            ):
                return False
            
            visited[r][c] = True

            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            
            # backtrack
            visited[r][c] = False

            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True

        return False

                        

                    



