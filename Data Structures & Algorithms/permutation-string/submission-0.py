class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}

        for c in s1:
            freq[c] = freq.get(c, 0) + 1

        for l in range((len(s2) - len(s1) + 1)):
            map = {}
            for r in range(len(s1)):
                map[s2[l + r]] = map.get(s2[l + r], 0) + 1
            if map == freq:
                return True
        return False
                

        