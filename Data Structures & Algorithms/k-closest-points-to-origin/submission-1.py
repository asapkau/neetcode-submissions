import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        for x, y in points:
            distance = x**2 + y**2
            heapq.heappush(heap, (distance, (x,y)))
        
        for i in range(k):
            distance, point = heapq.heappop(heap)
            res.append(point)
        
        return res
        