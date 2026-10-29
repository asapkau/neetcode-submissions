class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, remaining):

            if remaining == 0:
                res.append(path.copy())
                return
            
            for j in range(i, len(nums)):

                candidate = nums[j]

                if candidate > remaining:
                    continue

                path.append(candidate)

                dfs(j, remaining - candidate)

                path.pop()

                
        
        dfs(0,target)
        return res


        