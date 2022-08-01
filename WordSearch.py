class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        word_len = len(word)
        
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        
        def dfs(curr_len, i, j):
            
            if curr_len == word_len:
                return True
            
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            
            if board[i][j]!= word[curr_len] or visited[i][j]:
                return False
            
            visited[i][j] = 1
            ans = dfs(curr_len+1, i+1, j) or dfs(curr_len+1, i, j+1) or dfs(curr_len+1, i, j-1) or dfs(curr_len+1, i-1, j)
            visited[i][j] = 0
            return ans
        
        for i in range(rows):
            for j in range(cols):
                if dfs(0, i, j):
                    return True
                
        return False