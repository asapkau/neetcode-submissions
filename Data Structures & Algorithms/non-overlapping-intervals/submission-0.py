class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        counter = 0
        
        intervals = sorted(intervals)

        current = intervals[0]

        for i in range(1, len(intervals)):
            nextInterval = intervals[i]

            if nextInterval[0] < current[1]:
                counter += 1
                if current[1] <= nextInterval[1]:
                    current = current
                else:
                    current = nextInterval
            else:
                current = nextInterval
        return counter

