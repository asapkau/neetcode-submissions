class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]

            if diff in hashMap:
                return [hashMap[diff] + 1, i + 1]

            hashMap[numbers[i]] = i