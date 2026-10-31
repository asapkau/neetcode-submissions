from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        c = k
        counter = Counter(nums)
        for val, freq in counter.items():
            heapq.heappush(heap,(-freq, val))
        
        while c > 0:
            element = heapq.heappop(heap)
            res.append(element[1])
            c -= 1
        return res
            


        