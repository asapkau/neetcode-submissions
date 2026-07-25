class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        if n == 0:
            return []
        
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

        # res = []
        # if not nums:
        #     return []
        # for i in range(len(nums)):
        #     pre = 1
        #     post = 1

        #     for j in range(i):
        #         pre *= nums[j]

        #     for k in range(i+1, len(nums)):
        #         post *= nums[k]

        #     res.append(pre * post)
        # return res
                


        