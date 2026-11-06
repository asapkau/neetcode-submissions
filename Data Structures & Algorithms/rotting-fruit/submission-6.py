from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshFruit = 0
        q = deque()
        visited = set()
        timeElasped = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    freshFruit += 1
                
                if grid[row][col] == 2 and (row, col) not in visited:
                    q.append((row,col))
                
        while q and freshFruit > 0:

            ROWS, COLS = len(grid), len(grid[0])

            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            freshFruit -= 1
                            q.append((nr,nc))
            timeElasped += 1
        if freshFruit == 0:
            return timeElasped
        
        return -1






        