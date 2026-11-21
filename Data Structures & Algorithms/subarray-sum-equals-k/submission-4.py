class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preFix = {0:1}
        currSum = 0
        count = 0
        #{2:2, 1:1, 4:1} [1,-1,3] k = 3 {1:1, 0:2, 3:1} {0:1, -1:2, -2:1}
        for i in range(len(nums)):
            currSum += nums[i]
            



            
            valcount = currSum - k
            if valcount in preFix:
                lol = preFix[currSum - k]
                count += lol
            preFix[currSum] = preFix.get(currSum, 0) + 1
        return count
                

            


        