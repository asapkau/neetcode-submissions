class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        result = []
        suff = 1
        pref = 1
        if not nums:
            return []
        
        for i in range(len(nums)):
            sufptr = i + 1
            
            while sufptr < len(nums):
                suff *= nums[sufptr]
                
                sufptr += 1
                
            suffix.append(suff)
            
            suff = 1
            
            prefPtr = i - 1

            while prefPtr >= 0:
                pref *= nums[prefPtr]
                prefPtr -= 1
            
            prefix.append(pref)
            pref = 1

            result.append(prefix[i]*suffix[i])
        return result

        