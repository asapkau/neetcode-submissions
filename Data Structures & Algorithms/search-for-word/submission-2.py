class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        
        rows, cols = len(board), len(board[0])
        visited = set()


        
        def dfs(row, col, index):
            if index == len(word):
                return True

            if (row < 0 or 
                row >= rows or 
                col < 0 or 
                col >= cols or 
                board[row][col] != word[index] or
                (row,col) in visited):
                return False
            
            visited.add((row, col))
            
            print(visited)
            print(index)
            
            found = (dfs(row, col + 1, index + 1) or
                dfs(row + 1, col, index + 1) or
                dfs(row, col - 1, index + 1) or
                dfs(row - 1, col, index + 1))
            
            visited.remove((row,col))
            return found

            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c , 0):
                        return True
        return False
        
        