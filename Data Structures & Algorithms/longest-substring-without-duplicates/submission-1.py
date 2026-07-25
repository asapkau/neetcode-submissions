class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()

        if not s:
            return 0
        
        l = 0
        maxLen = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            length = r - l + 1
            maxLen = max(maxLen, length)
        
        return maxLen
            
