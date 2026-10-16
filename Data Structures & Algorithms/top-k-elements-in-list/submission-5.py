class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        sortedItems = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)

        return [item[0] for item in sortedItems[:k]]