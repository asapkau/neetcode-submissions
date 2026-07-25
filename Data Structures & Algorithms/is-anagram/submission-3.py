class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        if len(s) != len(t):
            return False
        for char in range(len(s)):
            if s[char] not in sMap:
                sMap[s[char]] = 1
            else:
                sMap[s[char]] += 1
            if t[char] not in tMap:
                tMap[t[char]] = 1
            else:
                tMap[t[char]] += 1
        
        return sMap == tMap