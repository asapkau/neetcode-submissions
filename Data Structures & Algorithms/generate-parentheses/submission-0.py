class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return 
        
        res = []

        def dfs(currentStr, openCount, closeCount):
            if len(currentStr) == 2*n:
                res.append(currentStr)
                return
            
            if openCount < n:
                dfs(currentStr + "(", openCount + 1, closeCount)
            
            if closeCount < openCount:
                dfs(currentStr + ")", openCount, closeCount + 1)
        dfs("", 0, 0)
        return res

                
