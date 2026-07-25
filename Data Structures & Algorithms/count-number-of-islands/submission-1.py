class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        islands = 0
        visit = set()


        def dfs(r,c):
            if (r,c) in visit or r >= rows or r < 0 or c >= cols or c < 0  or grid[r][c] == "0":
                return
            visit.add((r,c))

            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            
            
            

            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r, c)
                    islands += 1
        return islands
        
        