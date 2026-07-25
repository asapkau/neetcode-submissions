class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r,c):
            if (r,c) in visited or r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == "0":
                return
            visited.add((r,c))

            dfs(r+1,c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    dfs(row, col)
                    islands += 1
        return islands
                    


        