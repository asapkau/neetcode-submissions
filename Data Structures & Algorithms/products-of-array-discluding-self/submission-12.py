class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        post = [1] * len(nums)
        postProd = nums[len(nums)-1]
        
        for i in range(len(nums) - 2, -1, -1):
            tmp = nums[i]
            post[i] = postProd
            postProd *= tmp
        
        pre = [1] * len(nums)
        preProd = nums[0]

        for j in range(1, len(nums)):
            tmp = nums[j]
            pre[j] = preProd
            preProd *= tmp
        
        for k in range(len(nums)):
            res[k] = post[k] * pre[k]

        return res


        
        



        