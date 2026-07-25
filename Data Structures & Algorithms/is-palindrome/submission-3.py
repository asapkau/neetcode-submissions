class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        
        low = 0
        high = len(s) - 1

        while low < high:
            if not s[low].isalnum():
                low += 1
                continue

            if not s[high].isalnum():
                high -= 1
                continue

            if s[low].lower() != s[high].lower():
                return False
            
            low += 1
            high -= 1
        return True
        