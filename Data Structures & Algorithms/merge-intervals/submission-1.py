class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals)

        
        current = intervals[0]

        for i in range(1, len(intervals)):
            nextInterval = intervals[i]

            if nextInterval[0] <= current[1]:
                current[1] = max(current[1],nextInterval[1])
            else:
                res.append(current)
                current = nextInterval
        res.append(current)
        return res
            

            
        