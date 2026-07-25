class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        maxArea = 0
        visit = set()
        

        def dfs(r,c):
            currArea = 0
            if (r,c) in visit or r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            visit.add((r,c))
            currArea += 1

            currArea += dfs(r+1,c)
            currArea += dfs(r, c+1)
            currArea += dfs(r, c-1)
            currArea += dfs(r-1, c)

            return currArea

            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = dfs(r,c)
                    maxArea = max(area, maxArea)
        return maxArea
