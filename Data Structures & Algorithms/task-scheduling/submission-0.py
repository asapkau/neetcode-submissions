from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        coolDown = deque()

        counter = Counter(tasks)

        for task, freq in counter.items():
            heapq.heappush(heap, (-freq, task))

        currTime = 0

        while heap or coolDown:
            currTime += 1

            # Bring cooled-down tasks back
            if coolDown and coolDown[0][2] <= currTime:
                remainingCount, task, readyTime = coolDown.popleft()
                heapq.heappush(heap, (remainingCount, task))

            # Run one available task
            if heap:
                remainingCount, task = heapq.heappop(heap)

                remainingCount += 1  # -3 -> -2

                if remainingCount != 0:
                    readyTime = currTime + n + 1
                    coolDown.append(
                        (remainingCount, task, readyTime)
                    )

        return currTime