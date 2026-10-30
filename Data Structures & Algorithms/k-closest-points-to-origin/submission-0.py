import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        counter = k

        for x,y in points:
            distanceFromOrigin = x**2 + y**2
            heapq.heappush(heap, (distanceFromOrigin, (x, y)))
        while counter > 0:
            distance, point = heapq.heappop(heap)
            res.append(list(point))
            counter -= 1
        
        return res
            
            
        