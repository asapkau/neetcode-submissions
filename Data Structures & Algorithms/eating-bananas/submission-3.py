class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowestRate = 1
        maxRate = max(piles)
        minRate = max(piles)

        while lowestRate <= maxRate:
            midRate = (lowestRate + maxRate) // 2
            hoursNeeded = 0

            for benene in piles:
                hoursNeeded += math.ceil(benene / midRate)
                
            

            if hoursNeeded <= h:
                minRate = min(midRate, minRate)
                maxRate = midRate - 1
                
            elif hoursNeeded > h:
                lowestRate = midRate + 1
            
            
        return minRate