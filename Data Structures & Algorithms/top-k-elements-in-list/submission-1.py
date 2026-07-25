class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        array = []

        for num in nums:
            freqMap[num] = freqMap.get(num , 0) + 1
    
        sortedFreq = sorted(freqMap.items(), key = lambda x:x[1], reverse = True)
        print(sortedFreq[:k])

        for i in sortedFreq[:k]:
            array.append(i[0])
        return array

