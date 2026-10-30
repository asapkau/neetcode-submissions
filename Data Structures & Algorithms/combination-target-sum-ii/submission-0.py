class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, remaining):

            if remaining == 0:
                res.append(path.copy())
                return
            
            candidates.sort()
            
            for j in range(i, len(candidates)):

                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                candidate = candidates[j]

                if candidate > remaining:
                    continue

                path.append(candidate)

                dfs(j+1, remaining - candidate)

                path.pop()

                
        
        dfs(0,target)
        return res


        