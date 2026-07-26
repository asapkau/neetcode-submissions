class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check

        for row in range(9):
            rowSet = set()
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in rowSet:
                    return False
                rowSet.add(val)
        
        #col check

        for col in range(9):
            colSet = set()
            for row in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in colSet:
                    return False
                colSet.add(val)
        
        #box check

        for r in range(0,9,3):
            for c in range(0,9,3):
                boxSet = set()

                for row in range(r,r+3):
                    for col in range(c, c+3):
                        val = board[row][col]
                        if val == ".":
                            continue
                        if val in boxSet:
                            return False
                        boxSet.add(val)
        return True

        