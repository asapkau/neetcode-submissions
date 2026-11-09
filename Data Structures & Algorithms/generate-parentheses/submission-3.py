class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(countOpen, countClosed):
            if countOpen == countClosed == n:
                res.append("".join(path))
                return

            
            if countOpen < n:
                path.append("(")
                backtrack(countOpen + 1, countClosed)
                path.pop()

            

            if countClosed < countOpen:
                path.append(")")
                backtrack(countOpen, countClosed + 1)
                path.pop()
            
        backtrack(0,0)
        return res


        