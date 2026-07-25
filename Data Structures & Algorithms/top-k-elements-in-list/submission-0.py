class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        sortedFreq = sorted(freq.items(), key = lambda x: x[1] , reverse = True)



        result = []

        for i in sortedFreq:
            result.append(i[0])

        return result[:k]            
        