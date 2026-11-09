class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        memo = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]
            


        return dfs(0)
            






        

        