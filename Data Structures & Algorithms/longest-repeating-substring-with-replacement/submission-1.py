class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxLen = 0
        maxFreq = 0


        for h in range(len(s)):
            if s[h] in count:
                count[s[h]] += 1
            else:
                count[s[h]] = 1
            
            maxFreq = max(maxFreq, count[s[h]])

            if (h - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, h - l + 1)
            
        return maxLen




                
                




        