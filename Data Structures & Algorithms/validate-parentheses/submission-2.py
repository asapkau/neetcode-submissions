class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif s[i] == ")":
                if not stack:
                    return False
                bracket = stack.pop()

                if bracket != "(":
                    return False
            elif s[i] == "]":
                if not stack:
                    return False
                bracket = stack.pop()

                if bracket != "[":
                    return False
            elif s[i] == "}":
                if not stack:
                    return False
                bracket = stack.pop()

                if bracket != "{":
                    return False
            else:
                return False
        return len(stack) == 0


        