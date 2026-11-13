import heapq
from collections import Counter
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        heap = []
        coolDown = deque()
        counter = Counter(tasks)


        for tasks, freq in counter.items():
            heapq.heappush(heap, (-freq, tasks))
        
        currTime = 0

        while heap or coolDown:
            currTime += 1

            if coolDown and coolDown[0][2] <= currTime:
                remainingCount, task, readyTime = coolDown.popleft()
                heapq.heappush(heap, (remainingCount, task))

            if heap:
                remainingCount, task = heapq.heappop(heap)
                remainingCount += 1

                if remainingCount != 0:
                    readyTime = currTime + n + 1
                    coolDown.append((remainingCount, task, readyTime))
        
            

        return currTime       
        
        