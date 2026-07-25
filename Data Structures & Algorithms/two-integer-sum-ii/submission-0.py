class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        
        low = 0
        high = len(numbers) - 1

        while low < high:
            res = numbers[low] + numbers[high] 
            if res == target:
                return([low + 1, high + 1])
            
            elif res > target:
                high -= 1
            
            elif res < target:
                low += 1
            
        return
        
        