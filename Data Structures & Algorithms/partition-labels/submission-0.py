from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        res = []
        start = 0
        freq = Counter(s)
        openChar = 0
        seen = set()

        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                openChar += 1
            
            freq[s[i]] -= 1

            if freq[s[i]] == 0:
                openChar -= 1
            
            if openChar == 0:
                res.append(i - start + 1)
                start = i + 1
        return res






        