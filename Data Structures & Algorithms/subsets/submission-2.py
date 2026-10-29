class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []


        def dfs(i):

            #basecase
            if i == len(nums):
                res.append(path.copy())
                return
            
            #choice 1 : include nums[i]
            path.append(nums[i])
            dfs(i + 1)

            #choice 2: exclude nums[i]
            path.remove(nums[i])
            dfs(i+1)
        
        dfs(0)
        return res
    