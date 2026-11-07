class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        path = []
        dup = set()

        def backtrack(i):
            if i == len(nums):
                res.append(path.copy())
                return
            

            path.append(nums[i])
            backtrack(i + 1)

            path.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i + 1)

        backtrack(0)
        return res


            


        