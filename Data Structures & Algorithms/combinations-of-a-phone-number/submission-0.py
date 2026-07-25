class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        

        def dfs(index, path):
            if index == len(digits):
                res.append(path)
                return
            
            for char in phone[digits[index]]:
                dfs(index + 1, path + char)
            
        dfs(0,"")
        return res
            

        



        