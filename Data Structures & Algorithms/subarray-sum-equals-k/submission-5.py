class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        running_sum = 0
        result = 0

        for num in nums:
            running_sum += num

            target = running_sum - k

            if target in prefix_count:
                result += prefix_count[target]

            prefix_count[running_sum] = prefix_count.get(running_sum, 0) + 1

        return result
            


        