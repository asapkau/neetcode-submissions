class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        

        def robbing(start, end):
            memo = {}

            def dfs(index):

                if index >= end:
                    return 0
                
                if index in memo:
                    return memo[index]
                else:
                    memo[index] = max(nums[index] + dfs(index + 2), dfs(index + 1))

                return memo[index]
            return dfs(start)
        return max(robbing(0, len(nums) - 1), robbing(1, len(nums)))
            
            


        
        