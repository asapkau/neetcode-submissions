"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda x:x.start)
        endTimes = []
        for i in range(len(intervals)):
            if endTimes:
                if intervals[i].start >= endTimes[0]:
                    heapq.heappush(endTimes, intervals[i].end)
                    heapq.heappop(endTimes)
                elif intervals[i].start < endTimes[0]:
                    heapq.heappush(endTimes, intervals[i].end)
            else:
                heapq.heappush(endTimes, intervals[i].end)
            
        return len(endTimes)
        