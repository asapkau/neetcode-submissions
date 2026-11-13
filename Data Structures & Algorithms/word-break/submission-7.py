class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}

        def backtrack(i):
            if i == len(s):
                return True
            
            if i in memo:
                return memo[i]

            else:

                for word in wordDict:

                    if i + len(word) > len(s):
                        continue

                    matches = True

                    for index in range(len(word)):
                        if word[index] != s[i + index]:
                            matches = False
                            break
                        
                    if matches:
                        if backtrack(i + len(word)):
                            memo[i] = True
                            return True

            memo[i] = False
            return False

        return backtrack(0)

