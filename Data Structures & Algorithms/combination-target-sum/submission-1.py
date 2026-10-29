class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []


        def dfs(i, remaining):
            # Base case: remaining == 0

            if remaining == 0:
                res.append(path.copy())
                return

            # Base case: remaining < 0
            if remaining < 0:
                return


            for j in range(i, len(nums)):
                
                #choose nums[j]
                path.append(nums[j])

                # Recurse
                dfs(j, remaining - nums[j])

                # Backtrack

                path.pop()
            
        dfs(0, target)
        return res


        