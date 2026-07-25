class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            if num in freqMap:
                freqMap[num] = freqMap.get(num, 0) + 1
            else:
                freqMap[num] = 1
        
        return sorted(freqMap, key=freqMap.get, reverse=True)[:k]

