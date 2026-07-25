class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        if len(s) != len(t):
            return False

        for letter in range(len(s)):
            sMap[s[letter]] = sMap.get(s[letter], 0) + 1
            tMap[t[letter]] = tMap.get(t[letter], 0) + 1
        
        if sMap == tMap:
            return True
        else:
            return False
        