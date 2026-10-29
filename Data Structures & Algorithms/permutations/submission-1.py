class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = set()

        def dfs():

            #base case : all perms exhausted
            if len(path) == len(nums):
                res.append(path.copy())
                return
            

            for n in nums:
                if n in used:
                    continue

                path.append(n)
                used.add(n)
            
                dfs()

                path.pop()
                used.remove(n)
        dfs()
        return res
        



            

        