from collections import deque



class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        freshFruit = 0
        q = deque()
        visited = set()
        timeElapsed = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    freshFruit += 1
       
                
                if grid[r][c] == 2 and (r,c) not in visited:
                    q.append((r, c))
                
        while q and freshFruit > 0:

            ROWS, COLS = len(grid), len(grid[0]) 

            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc


                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            freshFruit -= 1
                            q.append((nr,nc))
            timeElapsed += 1
        if freshFruit == 0:
            return timeElapsed

        return -1







                    






















        


        