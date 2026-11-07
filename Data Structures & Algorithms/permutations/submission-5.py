class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        used = set()

        def backtrack():

            if len(perm) == len(nums):
                res.append(perm.copy())
                return


            for num in nums:
                if num in used:
                    continue

                perm.append(num)
                used.add(num)
            
                backtrack()

                perm.pop()
                used.remove(num)

        backtrack()
        return res
                
