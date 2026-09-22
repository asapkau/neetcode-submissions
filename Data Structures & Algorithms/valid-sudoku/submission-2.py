class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check
        for row in board:
            hashSet = set()
            for val in row:

                if val == ".":
                    continue

                if val in hashSet:
                    return False

                hashSet.add(val)
        
        #col check
        for col in range(9):
            colSet = set()

            for r in range(9):
                colVal = board[r][col]

                if colVal == ".":
                    continue

                if colVal in colSet:
                    return False

                colSet.add(colVal)
        
        # box check
        for brow in range(0, 9, 3):
            for bcol in range(0, 9, 3):

                boxSet = set()

                for r in range(3):
                    for c in range(3):

                        boxVal = board[brow + r][bcol + c]

                        if boxVal == ".":
                            continue

                        if boxVal in boxSet:
                            return False

                        boxSet.add(boxVal)
        return True
                        

             
