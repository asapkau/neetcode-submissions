class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        lowPtr = 0
        maxLength = 0

        for highPtr, letter in enumerate(s):
            if letter in hashMap:
                prevIndex = hashMap[letter]
                lowPtr = max(lowPtr, prevIndex + 1)

            hashMap[letter] = highPtr

            currentLength = highPtr - lowPtr + 1
            maxLength = max(maxLength, currentLength)

        return maxLength