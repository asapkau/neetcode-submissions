class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        used = set()


        def backtrack(index, diff):

            if diff == 0:
                res.append(comb.copy())
                return
            
            if diff < 0:
                return
            
            for i in range(index, len(nums)):
                comb.append(nums[i])
                
                backtrack(i, diff - nums[i])

                comb.pop()
                
            
        backtrack(0, target)
        return res

            
        