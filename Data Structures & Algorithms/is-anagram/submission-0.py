class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHashMap = {}
        tHashMap = {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sHashMap[s[i]] = sHashMap.get(s[i], 0) + 1
            tHashMap[t[i]] = tHashMap.get(t[i], 0) + 1

        if sHashMap == tHashMap:
            return True
        return False
        