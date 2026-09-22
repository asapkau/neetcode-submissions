class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for word in s:
            if word.isalnum():
                l.append(word.lower())
        low, high = 0, len(l) - 1

        while low < high:
            if l[low] != l[high]:
                return False
            else:
                low += 1
                high -= 1
        return True
        

        