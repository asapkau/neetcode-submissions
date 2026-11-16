from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshFruit = 0
        rotten = deque()
        visited = set()
        timeElapsed = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    freshFruit += 1
                    
                elif grid[row][col] == 2 and (row, col) not in visited:
                    rotten.append((row,col))

                visited.add((row,col))

        while rotten and freshFruit > 0:
            ROWS, COLS = len(grid), len(grid[0])


            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            for i in range(len(rotten)):
                r, c = rotten.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            freshFruit -= 1
                            rotten.append((nr, nc))
            timeElapsed += 1
        if freshFruit == 0:
            return timeElapsed
        return -1




                




        