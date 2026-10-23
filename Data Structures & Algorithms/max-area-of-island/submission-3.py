class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0

        def dfs(r,c):
            nonlocal area
            
            if r < 0 or r >= len(grid):
                return
            if c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] == 0:
                return
            if (r, c) in visited:
                return

            visited.add((r,c))
            area += 1
            
            dfs(r , c + 1)
            dfs(r + 1 , c)
            dfs(r , c - 1)
            dfs(r - 1 , c)
            return area
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = 0
                    currentArea = dfs(r, c)
                    maxArea = max(maxArea, currentArea)
        return maxArea
        