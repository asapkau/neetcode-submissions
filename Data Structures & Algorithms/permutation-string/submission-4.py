class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        s2Map = {}

        for l in range(len(s1)):
            s1Map[s1[l]] = s1Map.get(s1[l], 0) + 1
        
        low = 0
        windowSize = len(s1)

        for high in range(len(s2)):
            if high - low + 1 > windowSize:
                s2Map[s2[low]] -= 1

                if s2Map[s2[low]] == 0:
                    del s2Map[s2[low]]
                
                low += 1
            if high - low + 1 <= windowSize:
                s2Map[s2[high]] = s2Map.get(s2[high], 0) + 1

                if s1Map == s2Map:
                    return True
        return False

            
