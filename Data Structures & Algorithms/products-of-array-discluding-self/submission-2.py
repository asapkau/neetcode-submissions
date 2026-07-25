class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        if not nums:
            return []
        for i in range(len(nums)):
            pre = 1
            post = 1

            for j in range(i):
                pre *= nums[j]

            for k in range(i+1, len(nums)):
                post *= nums[k]

            res.append(pre * post)
        return res
                


        