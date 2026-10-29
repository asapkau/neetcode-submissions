class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = set()


        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            #basecase
            for num in nums:
                if num in used:
                    continue
                used.add(num)
                path.append(num)

                

                #choice 1
                dfs()

                #choice 2

                used.remove(num)
                path.pop()

        dfs()
        return res
