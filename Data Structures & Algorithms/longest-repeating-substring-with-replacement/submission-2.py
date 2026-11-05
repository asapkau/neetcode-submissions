class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxLen = 0
        maxFreq = 0

        for h in range(len(s)):
            freq[s[h]] = freq.get(s[h], 0) + 1
            maxFreq = max(maxFreq, freq[s[h]])

            if (h - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, h - l + 1)
        return maxLen


        
        



        