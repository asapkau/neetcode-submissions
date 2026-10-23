from collections import deque



class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()
        visited = set()
        fresh = 0
        timeElapsed = 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2 and (r,c) not in visited:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            ROWS, COLS = len(grid), len(grid[0])

            for _ in range(len(q)):
                row, col = q.popleft()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and (nr, nc) not in visited
                        and grid[nr][nc] == 1
                    ):

                        fresh -= 1
                        visited.add((nr, nc))
                        q.append((nr,nc))
            timeElapsed += 1
        if fresh > 0:
            return -1

        return timeElapsed - 1




















        


        