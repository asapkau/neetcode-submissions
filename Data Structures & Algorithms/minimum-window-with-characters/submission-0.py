from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)

        left = 0
        minWindow = float('inf')
        minSubString = ""
        for i in range(len(s)):
            if s[i] in need:
                need[s[i]] -= 1
            
            while all(count <= 0 for count in need.values()):
                if i - left + 1 < minWindow:
                    minWindow = i - left + 1
                    minStart = left
                    minEnd = i

                if s[left] in need:
                    need[s[left]] += 1
                
                left += 1

        if minWindow == float('inf'):
            return ""

        return s[minStart:minEnd + 1]

                
                    
            


        

                



        
        